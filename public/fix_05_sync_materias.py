import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
raw = open(path, 'rb').read()
has_crlf = b'\r\n' in raw
content = raw.decode('utf-8').replace('\r\n', '\n')
applied = 0

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 1 — sincronizarCompletadosDesdeSheets
# Regex acepta tanto "G2 Lección 1" como "G2_L1"
# matKey busca por MATERIAS_JERO.nombre + aliases legacy
# ══════════════════════════════════════════════════════════════════════════════
OLD1 = (
    "const matchLec = String(r.dia).match(/G2 Lecci[o\u00f3]n\\s*(\\d+)/i);\n"
    "      if (!matchLec) return;\n"
    "      const lecNum = parseInt(matchLec[1]);\n"
    "      const matKey = Object.keys(NOMBRES_G2).find(k => NOMBRES_G2[k] === r.materia);"
)

NEW1 = (
    "const matchLec = String(r.dia).match(/G2[ _]L(?:ecci[o\u00f3]n\\s*)?(\\d+)/i);\n"
    "      if (!matchLec) return;\n"
    "      const lecNum = parseInt(matchLec[1]);\n"
    "      const matKey = Object.keys(MATERIAS_JERO).find(k => MATERIAS_JERO[k].nombre === r.materia)\n"
    "        || {'Ciencias Naturales':'NAT','Ciencias Sociales':'SOC','Cs. Sociales':'SOC',\n"
    "            'Ciencias Nat.':'NAT','Cs. Nat.':'NAT','Lengua Castellana':'LCA'}[r.materia];"
)

if OLD1 in content:
    content = content.replace(OLD1, NEW1, 1)
    applied += 1
    print('  \u2705 Patch 1: sincronizarCompletados — regex + matKey corregidos')
else:
    print('  \u274c Patch 1: anchor no encontrado')

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 2 — sincronizarProgresoJeroDesdeSheets
# Quitar gate de codigo → usar nombre (igual que la función general)
# ══════════════════════════════════════════════════════════════════════════════
OLD2 = 'async function sincronizarProgresoJeroDesdeSheets() {\n  if (!estado.codigo) return;'
NEW2 = 'async function sincronizarProgresoJeroDesdeSheets() {\n  if (!estado.nombre) return;'

if OLD2 in content:
    content = content.replace(OLD2, NEW2, 1)
    applied += 1
    print('  \u2705 Patch 2: gate estado.codigo \u2192 estado.nombre')
else:
    print('  \u274c Patch 2: anchor no encontrado')

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 3 — sincronizarProgresoJeroDesdeSheets
# Regex acepta "G2_L1" además de "G2 Lección 1"
# matKey usa MATERIAS_JERO + aliases legacy (igual que Patch 1)
# ══════════════════════════════════════════════════════════════════════════════
OLD3 = (
    "const NOMBRES_JERO = { MAT:'Matem\u00e1ticas', LCA:'Lengua Castellana', ING:'Ingl\u00e9s',"
    " NAT:'Ciencias Naturales', SOC:'Ciencias Sociales' };\n"
    "      const matKey = Object.keys(NOMBRES_JERO).find(k => NOMBRES_JERO[k] === r.materia);"
)

NEW3 = (
    "const matKey = Object.keys(MATERIAS_JERO).find(k => MATERIAS_JERO[k].nombre === r.materia)\n"
    "        || {'Ciencias Naturales':'NAT','Ciencias Sociales':'SOC','Cs. Sociales':'SOC',\n"
    "            'Ciencias Nat.':'NAT','Cs. Nat.':'NAT','Lengua Castellana':'LCA'}[r.materia];"
)

if OLD3 in content:
    content = content.replace(OLD3, NEW3, 1)
    applied += 1
    print('  \u2705 Patch 3: sincronizarProgreso — NOMBRES_JERO reemplazado por lookup flexible')
else:
    print('  \u274c Patch 3: anchor no encontrado')
    # debug
    idx = content.find('const NOMBRES_JERO')
    if idx >= 0:
        print(f'    (encontrado en pos {idx}):')
        print('   ', repr(content[idx:idx+150]))

if has_crlf:
    content = content.replace('\n', '\r\n')
open(path, 'wb').write(content.encode('utf-8'))
total = 3
print(f'\n{applied}/{total} patches aplicados {"✅" if applied == total else "⚠️  revisa errores"}')
