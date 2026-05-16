# 📋 GUIA DE FORMATO — COMO PEDIR Y RECIBIR UN EXAMEN NUEVO

## Como iniciar el chat

Escribe exactamente esto al inicio de cada chat nuevo:

```
Vamos a crear las preguntas de [MATERIA] Dia [N].
Recuerda el sistema: guia-sexto.vercel.app
Genera el Excel con 28 preguntas, minimo 5 imagenes, sin patron en respuestas.
```

---

## Lo que Claude debe entregar EN ORDEN

### 1. ARCHIVO EXCEL
- Nombre: `Dia[N]_[MATERIA].xlsx` (ej: `Dia1_BIO.xlsx`)
- 28 preguntas con las 9 columnas del sistema
- Respuestas distribuidas A×7 B×7 C×7 D×7 SIN patron visible
- URLs de imagen completas en columna I desde el inicio
- Explicacion popup en columna H

---

### 2. SCRIPT POWERSHELL PARA SUBIR AL SHEET

Siempre en este formato — solo cambian ARCHIVO y HOJA:

```powershell
python -c "
import openpyxl
from google.oauth2 import service_account
from googleapiclient.discovery import build
creds = service_account.Credentials.from_service_account_file(
    r'C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=creds)
wb = openpyxl.load_workbook(r'C:\Users\Usuario\Downloads\ARCHIVO.xlsx')
ws = wb.active
rows = []
for r in ws.iter_rows(min_row=3, max_row=30, values_only=True):
    if r[1]:
        rows.append([str(r[1] or ''),str(r[2] or ''),str(r[3] or ''),str(r[4] or ''),str(r[5] or ''),str(r[6] or ''),str(r[8] or '')])
service.spreadsheets().values().update(
    spreadsheetId='136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg',
    range='HOJA!A2:G35', valueInputOption='RAW',
    body={'values': rows}).execute()
print('LISTO', len(rows), 'preguntas subidas a HOJA')
"
```

> Cambiar `ARCHIVO.xlsx` y `HOJA` (ej: `Dia1_BIO`)

---

### 3. PROMPTS DE IMAGENES PARA GEMINI

Un bloque por cada imagen en este formato exacto:

```
PREGUNTA [N] — pregunta_[NN].jpg
Carpeta: C:\guia_sexto\public\imagenes\[materia]\dia[N]\
URL Sheet: https://guia-sexto.vercel.app/imagenes/[materia]/dia[N]/pregunta_[NN].jpg

PROMPT GEMINI:
[descripcion detallada en español de lo que debe mostrar la imagen]
```

---

### 4. SCRIPT COMPRIMIR IMAGENES

```python
# Abrir C:\guia_sexto\comprimir.py y cambiar la carpeta:

from PIL import Image
import os

carpeta = r'C:\guia_sexto\public\imagenes\bio\dia1'  # CAMBIAR

for nombre in os.listdir(carpeta):
    if nombre.lower().endswith('.png'):
        ruta_png = os.path.join(carpeta, nombre)
        img = Image.open(ruta_png)
        if img.width > 1200:
            img = img.resize((1200, int(img.height * (1200/img.width))), Image.LANCZOS)
        nombre_jpg = os.path.splitext(nombre)[0] + '.jpg'
        ruta_jpg = os.path.join(carpeta, nombre_jpg)
        img.convert('RGB').save(ruta_jpg, 'JPEG', quality=75)
        os.remove(ruta_png)
        print('OK:', nombre_jpg, '— PNG borrado')

print('LISTO')
```

Correr con:
```powershell
python C:\guia_sexto\comprimir.py
```

---

### 5. COMANDOS GIT PARA PUBLICAR

```powershell
cd C:\guia_sexto
git add .
git commit -m "imagenes [materia] dia[N]"
git push
```

---

## Flujo completo de un dia nuevo

```
1.  Claude genera el Excel → descargar a Descargas
2.  Crear hoja en Google Sheet con nombre exacto (ej: Dia1_BIO)
3.  Correr script PowerShell → preguntas al Sheet
4.  Generar imagenes con Gemini usando los prompts
5.  Crear carpeta si no existe:
    mkdir C:\guia_sexto\public\imagenes\bio\dia1
6.  Guardar imagenes con el nombre exacto en la carpeta
7.  Abrir comprimir.py → cambiar carpeta → guardar
8.  python C:\guia_sexto\comprimir.py
9.  Verificar pesos: dir C:\guia_sexto\public\imagenes\bio\dia1
    (ideal: 50-200 KB por imagen)
10. git add . → git commit → git push
11. Esperar 2 minutos → Vercel publica automaticamente
12. Verificar URL en navegador:
    https://guia-sexto.vercel.app/imagenes/bio/dia1/pregunta_03.jpg
```

---

## Convencion de nombres de imagenes

| Materia | Formato del nombre | Ejemplo |
|---------|-------------------|---------|
| LEN | `pregunta_03.jpg` | minuscula, guion bajo, cero si numero < 10 |
| MAT | `PREGUNTA3.jpg` | mayuscula, sin guion, sin cero |
| BIO | `pregunta_03.jpg` | igual que LEN |
| QUI | `pregunta_03.jpg` | igual que LEN |
| SOC | `pregunta_03.jpg` | igual que LEN |

> El nombre del archivo debe coincidir EXACTAMENTE con la URL del Sheet. Un caracter diferente da error 404.

---

## Datos fijos del sistema (nunca cambian)

| Dato | Valor |
|------|-------|
| Sheet ID | `136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg` |
| JSON key | `C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json` |
| URL produccion | `https://guia-sexto.vercel.app` |
| Carpeta proyecto | `C:\guia_sexto\` |
| Rama GitHub | `main` |

---

## Secuencias de respuestas YA USADAS (no repetir)

```
Dia1_LEN: B A D C A D B C D A C B A D C B D A B C A D C B D A C B
Dia2_LEN: C A D B A C D B C D A B D C A B D A C B A D B C A D C B
Dia3_LEN: D B A C D A B C A D C B A C D B C A D B B C A D C B D A
Dia4_LEN: A C D B C A D B A C B D C A B D A D C B D B A C B D C A
Dia5_LEN: C D A B D C A B D A C B A D B C B A D C C B D A B C A D
Dia6_LEN: B D C A D B A C B D A C D B C A C D A B A C D B C A B D
```

Generar siempre una secuencia NUEVA con A×7 B×7 C×7 D×7 sin patron visible ni rachas largas de la misma letra.

---

## Estructura de carpetas de imagenes

```
C:\guia_sexto\public\imagenes\
├── mat\
│   └── dia5\ (unico dia MAT con imagenes)
├── len\
│   ├── dia1\ (pregunta_17, pregunta_24)
│   ├── dia2\ (pregunta_03, 08, 14, 19, 25)
│   ├── dia3\ (pregunta_04, 09, 15, 21, 26)
│   ├── dia4\ (pregunta_03, 07, 13, 18, 24)
│   ├── dia5\ (pregunta_02, 06, 11, 17, 22, 27)
│   └── dia6\ (pregunta_04, 09, 15, 21, 26)
├── bio\  (pendiente)
├── qui\  (pendiente)
└── soc\  (pendiente)
```
