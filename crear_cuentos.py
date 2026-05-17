import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file(
    r'C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets'])

service = build('sheets', 'v4', credentials=creds)
SHEET_ID = '136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg'

# Crear la hoja Cuentos
service.spreadsheets().batchUpdate(
    spreadsheetId=SHEET_ID,
    body={'requests': [{'addSheet': {'properties': {'title': 'Cuentos'}}}]}
).execute()

# Encabezados
encabezados = [[
    'Serie', 'Capitulo', 'Titulo', 'Color',
    'Bloque1texto', 'Bloque1img',
    'Bloque2texto', 'Bloque2img',
    'Bloque3texto', 'Bloque3img',
    'Bloque4texto', 'Bloque4img',
    'Bloque5texto', 'Bloque5img',
    'Preguntas'
]]

service.spreadsheets().values().update(
    spreadsheetId=SHEET_ID,
    range='Cuentos!A1:O1',
    valueInputOption='RAW',
    body={'values': encabezados}
).execute()

# Fila de ejemplo para que veas el formato
ejemplo = [[
    'El Portal Olvidado',           # Serie
    '1',                            # Capitulo
    'La llave que nadie perdió',    # Titulo
    '#0F0F2E',                      # Color (fondo oscuro azul misterio)
    'Aquí va el primer bloque del cuento. Puedes escribir 2-3 párrafos aquí.',  # Bloque1texto
    '',                             # Bloque1img (URL de Gemini)
    'Aquí va el segundo bloque. La historia continúa...',  # Bloque2texto
    '',                             # Bloque2img
    '',                             # Bloque3texto
    '',                             # Bloque3img
    '',                             # Bloque4texto
    '',                             # Bloque4img
    '',                             # Bloque5texto
    '',                             # Bloque5img
    json.dumps([                    # Preguntas JSON
        {
            "pregunta": "¿Qué encontró el personaje al inicio del cuento?",
            "opciones": {"A": "Una llave", "B": "Un mapa", "C": "Una puerta", "D": "Un libro"},
            "respuesta": "A",
            "explicacion": "Al inicio del cuento el personaje encontró una llave misteriosa que nadie recordaba haber perdido."
        },
        {
            "pregunta": "¿Cómo se sintió el personaje al encontrarlo?",
            "opciones": {"A": "Feliz", "B": "Asustado", "C": "Curioso", "D": "Enojado"},
            "respuesta": "C",
            "explicacion": "El personaje sintió curiosidad porque el objeto era muy extraño y misterioso."
        }
    ], ensure_ascii=False)
]]

service.spreadsheets().values().update(
    spreadsheetId=SHEET_ID,
    range='Cuentos!A2:O2',
    valueInputOption='RAW',
    body={'values': ejemplo}
).execute()

print('✅ Hoja Cuentos creada con encabezados y fila de ejemplo')