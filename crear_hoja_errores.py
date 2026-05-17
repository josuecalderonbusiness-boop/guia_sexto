"""
crear_hoja_errores.py
Crea la hoja 'Errores' en Google Sheets con sus encabezados.
Ejecutar UNA sola vez desde PowerShell:
  python crear_hoja_errores.py

Requiere: pip install google-auth google-auth-oauthlib google-api-python-client
"""

import json, os, sys

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    print("ERROR: Instala dependencias con:")
    print("  pip install google-auth google-auth-oauthlib google-api-python-client")
    sys.exit(1)

# ── CONFIGURACIÓN ──────────────────────────────────────────────────────────
KEY_PATH   = r'C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json'
SHEET_ID   = '136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg'
HOJA_NOMBRE = 'Errores'
# ───────────────────────────────────────────────────────────────────────────

creds = service_account.Credentials.from_service_account_file(
    KEY_PATH,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
service = build('sheets', 'v4', credentials=creds)
ss = service.spreadsheets()

# 1. Verificar si la hoja ya existe
meta = ss.get(spreadsheetId=SHEET_ID).execute()
hojas_existentes = [s['properties']['title'] for s in meta['sheets']]

if HOJA_NOMBRE in hojas_existentes:
    print(f"✅ La hoja '{HOJA_NOMBRE}' ya existe. No se creó de nuevo.")
else:
    # 2. Crear la hoja
    ss.batchUpdate(
        spreadsheetId=SHEET_ID,
        body={'requests': [{'addSheet': {'properties': {'title': HOJA_NOMBRE}}}]}
    ).execute()
    print(f"✅ Hoja '{HOJA_NOMBRE}' creada.")

# 3. Agregar encabezados si fila 1 está vacía
valores = ss.values().get(
    spreadsheetId=SHEET_ID,
    range=f'{HOJA_NOMBRE}!A1:D1'
).execute().get('values', [])

if not valores or not valores[0]:
    ss.values().update(
        spreadsheetId=SHEET_ID,
        range=f'{HOJA_NOMBRE}!A1:D1',
        valueInputOption='RAW',
        body={'values': [['Codigo', 'Dia', 'Materia', 'Errores']]}
    ).execute()
    print(f"✅ Encabezados agregados: Codigo | Dia | Materia | Errores")
else:
    print(f"✅ Encabezados ya existían: {valores[0]}")

print(f"\n🎉 LISTO — hoja '{HOJA_NOMBRE}' lista para usar.")
print(f"   Ahora haz: git add . && git commit -m 'api: errores multi-dispositivo' && git push")
