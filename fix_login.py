import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'api', 'login.js')

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

patches = []

# ── PATCH 1: leer columna C (grado) en login normal ─────────────────
OLD1 = "      const r = await sheets.spreadsheets.values.get({\n        spreadsheetId: SHEET_ID,\n        range: 'Usuarios!A:B',\n      });\n      const rows = r.data.values || [];\n      const encontrado = rows.find(row => row[0] && row[0].trim().toUpperCase() === codigo);\n      if (!encontrado) {\n        return res.json({ ok: false, error: 'Código no encontrado. Pídele el código a tu profe.' });\n      }\n      return res.json({ ok: true, nombre: encontrado[1] || codigo, codigo, esAdmin: false });"

NEW1 = "      const r = await sheets.spreadsheets.values.get({\n        spreadsheetId: SHEET_ID,\n        range: 'Usuarios!A:C',\n      });\n      const rows = r.data.values || [];\n      const encontrado = rows.find(row => row[0] && row[0].trim().toUpperCase() === codigo);\n      if (!encontrado) {\n        return res.json({ ok: false, error: 'Código no encontrado. Pídele el código a tu profe.' });\n      }\n      const grado = encontrado[2] ? parseInt(encontrado[2]) || encontrado[2] : null;\n      return res.json({ ok: true, nombre: encontrado[1] || codigo, codigo, esAdmin: false, grado });"

if OLD1 in src:
    src = src.replace(OLD1, NEW1)
    patches.append('PATCH 1 ✅ login normal devuelve grado desde columna C')
else:
    patches.append('PATCH 1 ❌ no encontrado — revisa login.js')

# ── PATCH 2: agregar usuario con grado ──────────────────────────────
OLD2 = "      await sheets.spreadsheets.values.append({\n        spreadsheetId: SHEET_ID,\n        range: 'Usuarios!A:B',\n        valueInputOption: 'RAW',\n        requestBody: { values: [[codigo.toUpperCase(), nombre]] },\n      });"

NEW2 = "      const gradoNuevo = body.adminAgregar.grado || '';\n      await sheets.spreadsheets.values.append({\n        spreadsheetId: SHEET_ID,\n        range: 'Usuarios!A:C',\n        valueInputOption: 'RAW',\n        requestBody: { values: [[codigo.toUpperCase(), nombre, String(gradoNuevo)]] },\n      });"

if OLD2 in src:
    src = src.replace(OLD2, NEW2)
    patches.append('PATCH 2 ✅ agregar usuario guarda grado en columna C')
else:
    patches.append('PATCH 2 ❌ no encontrado')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\nlogin.js — {sum(1 for p in patches if "✅" in p)}/{len(patches)} patches aplicados')
for p in patches:
    print(' ', p)
