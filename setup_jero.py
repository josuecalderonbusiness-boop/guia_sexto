from google.oauth2 import service_account
from googleapiclient.discovery import build

SHEET_ID = '136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg'
KEY_FILE  = r'C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json'

creds   = service_account.Credentials.from_service_account_file(
    KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=creds)
sheets  = service.spreadsheets()

# ── 1. Agregar columna "grado" en Usuarios ───────────────────────────
print('1/2  Actualizando hoja Usuarios...')
sheets.values().update(
    spreadsheetId=SHEET_ID,
    range='Usuarios!A1:C4',
    valueInputOption='RAW',
    body={'values': [
        ['codigo',    'nombre', 'grado'],
        ['TOMAS2026', 'Tomas',  '6'],
        ['JERO2026',  'Jero',   '2'],
        ['ADMIN2026', 'Admin',  'admin'],
    ]}
).execute()
print('     ✅ Usuarios actualizado  (columna C = grado)')

# ── 2. Crear hojas vacías para Jero ──────────────────────────────────
HOJAS_JERO = ['G2_MAT_L01', 'G2_LCA_L01', 'G2_ING_L01', 'G2_NAT_L01', 'G2_SOC_L01']

# Obtener hojas existentes
meta = sheets.get(spreadsheetId=SHEET_ID).execute()
existentes = {s['properties']['title'] for s in meta['sheets']}

requests = []
for nombre in HOJAS_JERO:
    if nombre not in existentes:
        requests.append({'addSheet': {'properties': {'title': nombre}}})
        print(f'     + Creando hoja: {nombre}')
    else:
        print(f'     ~ Ya existe:    {nombre}')

if requests:
    sheets.batchUpdate(
        spreadsheetId=SHEET_ID,
        body={'requests': requests}
    ).execute()

print('2/2  ✅ Hojas de Jero listas')
print()
print('Todo listo. Tomas no fue tocado.')
print('Ahora puedes correr el deploy normal.')
