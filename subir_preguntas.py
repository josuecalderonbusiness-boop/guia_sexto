"""
Sube las preguntas de Matemáticas Día 1 al Google Sheet.
Ejecutar desde la carpeta guia_sexto con:
  python subir_preguntas.py
"""
import json, sys, os

# ── instalar dependencias si faltan ──────────────────────────────────
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    import openpyxl
except ImportError:
    os.system(f"{sys.executable} -m pip install google-api-python-client google-auth openpyxl")
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    import openpyxl

# ── CONFIG — ajusta estas rutas si es necesario ──────────────────────
JSON_PATH  = r"C:\Users\JC\Downloads\examen-ninos-fd3bf54ba69e.json"
EXCEL_PATH = r"C:\guia_sexto\MAT1_sin_LaTeX.xlsx"   # o donde lo tengas
SHEET_ID   = "136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg"
HOJA       = "Dia1_MAT"
# ────────────────────────────────────────────────────────────────────

print("📖 Leyendo Excel...")
wb = openpyxl.load_workbook(EXCEL_PATH)
ws = wb.active
rows = []
for row in ws.iter_rows(min_row=2, values_only=True):
    if row[1]:
        rows.append([
            str(row[1] or ''),
            str(row[2] or ''),
            str(row[3] or ''),
            str(row[4] or ''),
            str(row[5] or ''),
            str(row[6] or 'A'),
        ])
print(f"   {len(rows)} preguntas encontradas")

print("🔑 Autenticando con Google...")
creds = service_account.Credentials.from_service_account_file(
    JSON_PATH,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
service = build('sheets', 'v4', credentials=creds)

print(f"📤 Subiendo a hoja '{HOJA}'...")
service.spreadsheets().values().update(
    spreadsheetId=SHEET_ID,
    range=f'{HOJA}!A2:F26',
    valueInputOption='USER_ENTERED',
    body={'values': rows}
).execute()

print(f"✅ ¡Listo! {len(rows)} preguntas subidas a {HOJA}")
print(f"   Abre: https://guia-sexto.vercel.app")
