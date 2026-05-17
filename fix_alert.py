import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'public', 'index.html')

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

patches = []

# ── PATCH 1: corregir alert con salto de línea real ─────────────────
OLD1 = "alert('Aún no hay errores guardados en la nube para este refuerzo.\n¿Ya hiciste este examen en el otro dispositivo? Asegúrate de que tenga internet al terminar.');"
NEW1 = "alert('Aún no hay errores guardados en la nube para este refuerzo. ¿Ya hiciste este examen en el otro dispositivo? Asegúrate de que tenga internet al terminar.');"

if OLD1 in src:
    src = src.replace(OLD1, NEW1)
    patches.append('PATCH 1 ✅ alert multilínea corregido')
else:
    # Intentar con regex por si el salto de línea varía
    nuevo, n = re.subn(
        r"alert\('Aún no hay errores guardados en la nube para este refuerzo\.\s*¿Ya hiciste este examen en el otro dispositivo\? Asegúrate de que tenga internet al terminar\.'\);",
        "alert('Aún no hay errores guardados en la nube para este refuerzo. ¿Ya hiciste este examen en el otro dispositivo? Asegúrate de que tenga internet al terminar.');",
        src
    )
    if n:
        src = nuevo
        patches.append('PATCH 1 ✅ alert multilínea corregido (regex)')
    else:
        patches.append('PATCH 1 ❌ no encontrado — revisar línea 1230 manualmente')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

ok = sum(1 for p in patches if '✅' in p)
print(f'\nfix_alert.py — {ok}/{len(patches)} patches aplicados')
for p in patches:
    print(' ', p)
print()
if ok == len(patches):
    print('Listo. Corre: git add . && git commit -m "fix alert js" && git push')
