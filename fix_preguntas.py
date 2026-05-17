import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'api', 'preguntas.js')

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

patches = []

# ── PATCH 1: aceptar parámetros grado y leccion además de dia/materia
OLD1 = "  const { dia, materia } = req.query;\n  if (!dia || !materia) {\n    return res.status(400).json({ error: 'Faltan parámetros dia y materia' });\n  }\n\n  const sheetName = `Dia${dia}_${materia.toUpperCase()}`;"

NEW1 = "  const { dia, materia, grado, leccion } = req.query;\n\n  // Modo Jero (grado 2): G2_MAT_L01\n  // Modo Tomas (grado 6): Dia1_MAT\n  let sheetName;\n  if (grado && leccion) {\n    const lNum = String(leccion).padStart(2, '0');\n    sheetName = `G${grado}_${(materia||'').toUpperCase()}_L${lNum}`;\n  } else {\n    if (!dia || !materia) {\n      return res.status(400).json({ error: 'Faltan parámetros dia y materia' });\n    }\n    sheetName = `Dia${dia}_${materia.toUpperCase()}`;\n  }"

if OLD1 in src:
    src = src.replace(OLD1, NEW1)
    patches.append('PATCH 1 ✅ soporta grado+leccion y dia+materia')
else:
    patches.append('PATCH 1 ❌ no encontrado')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\npreguntas.js — {sum(1 for p in patches if "✅" in p)}/{len(patches)} patches aplicados')
for p in patches:
    print(' ', p)
