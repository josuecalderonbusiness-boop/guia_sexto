# 🎓 Examen Ninos — Estado del Sistema

**Fecha:** 15 de mayo de 2026  
**URL producción:** https://guia-sexto.vercel.app  
**Repositorio:** GitHub → `guia-sexto` (conectado a Vercel, deploy automático en push a `main`)

---

## 📁 Estructura del proyecto

```
C:\guia_sexto\
├── api/
│   ├── preguntas.js      → GET /api/preguntas?dia=1&materia=MAT
│   ├── guardar.js        → POST /api/guardar
│   ├── resultados.js     → GET /api/resultados?nombre=Tomas
│   ├── setup.js          → GET /api/setup (solo correr 1 vez)
│   ├── login.js          → POST /api/login
│   └── progreso.js       → GET/POST/DELETE /api/progreso
├── public/
│   ├── index.html        → App completa (toda la UI en un solo archivo)
│   └── imagenes/
│       ├── mat/
│       │   └── dia5/
│       │       ├── PREGUNTA3.jpg
│       │       ├── PREGUNTA7.jpg
│       │       ├── PREGUNTA12.jpg
│       │       ├── PREGUNTA13.jpg
│       │       ├── PREGUNTA16.jpg
│       │       ├── PREGUNTA21.jpg
│       │       ├── PREGUNTA24.jpg
│       │       └── PREGUNTA25.jpg
│       └── len/
│           ├── dia1/
│           │   ├── pregunta_17.jpg
│           │   └── pregunta_24.jpg
│           ├── dia2/
│           │   ├── pregunta_03.jpg
│           │   ├── pregunta_08.jpg
│           │   ├── pregunta_14.jpg
│           │   ├── pregunta_19.jpg
│           │   └── pregunta_25.jpg
│           └── dia3/
│               ├── pregunta_04.jpg
│               ├── pregunta_09.jpg
│               ├── pregunta_15.jpg
│               ├── pregunta_21.jpg
│               └── pregunta_26.jpg
├── comprimir.py          → Script reutilizable para comprimir imagenes PNG a JPG
├── package.json          → dependencia: googleapis
└── vercel.json           → rewrites: /api/* y /(.*) → /public/$1
```

---

## 🗄️ Google Sheets

**ID del Sheet:** `136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg`  
**URL:** https://docs.google.com/spreadsheets/d/136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg

### Hojas existentes

| Hoja | Propósito | Columnas |
|------|-----------|----------|
| `Dia1_MAT` a `Dia6_MAT` | Preguntas de Matematicas por dia | A:Pregunta, B:OpA, C:OpB, D:OpC, E:OpD, F:Respuesta(A/B/C/D), G:Imagen(URL), H:Video(URL YouTube) |
| `Dia1_BIO` a `Dia6_BIO` | Preguntas de Biologia | Mismo formato |
| `Dia1_QUI` a `Dia6_QUI` | Preguntas de Quimica | Mismo formato |
| `Dia1_SOC` a `Dia6_SOC` | Preguntas de Cs. Sociales | Mismo formato |
| `Dia1_LEN` a `Dia6_LEN` | Preguntas de Lenguaje | Mismo formato |
| `Resultados` | Historial de examenes completados | Fecha, Nombre, Dia, Materia, Puntaje, Total, Porcentaje, Respuestas |
| `Usuarios` | Codigos de acceso | A:Codigo, B:Nombre |
| `Progreso` | Examenes en curso (guardado automatico) | Codigo, Dia, Materia, Idx, Puntaje, Total, Respuestas(JSON) |

### Preguntas cargadas (estado actual)

| Dia | MAT | BIO | QUI | SOC | LEN |
|-----|-----|-----|-----|-----|-----|
| 1 | ✅ 25 preguntas | ⬜ | ⬜ | ⬜ | ✅ 28 preguntas |
| 2 | ✅ 28 preguntas | ⬜ | ⬜ | ⬜ | ✅ 28 preguntas |
| 3 | ✅ 28 preguntas | ⬜ | ⬜ | ⬜ | ✅ 28 preguntas |
| 4 | ✅ 28 preguntas | ⬜ | ⬜ | ⬜ | ⬜ |
| 5 | ✅ 28 preguntas | ⬜ | ⬜ | ⬜ | ⬜ |
| 6 | ✅ 28 preguntas | ⬜ | ⬜ | ⬜ | ⬜ |

---

## 🔐 Credenciales y variables de entorno

### Vercel Environment Variables (Settings → Environment Variables)
```
SHEET_ID = 136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg
GOOGLE_SERVICE_ACCOUNT_JSON = {contenido completo del JSON}
```

### Google Cloud
- **Proyecto:** `examen-ninos`
- **Service Account:** `examen-ninos-sheets@examen-ninos.iam.gserviceaccount.com`
- **JSON key:** `C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json`
- **API habilitada:** Google Sheets API

---

## 🖥️ Como funciona la app

### Flujo del usuario
1. Entra a https://guia-sexto.vercel.app
2. Escribe su **codigo de acceso** (ej. `ADMIN2026`) — verificado contra hoja `Usuarios`
3. Ve la pantalla de inicio con los 6 dias y 5 materias
4. Si tiene un examen a medias → aparece banner verde "Examen en progreso" con boton Continuar
5. Elige dia y materia → empieza el examen
6. Cada pregunta tiene **2 intentos** — al primer fallo puede volver a intentar; al segundo se revela la respuesta
7. Si hay imagen → aparece encima de la pregunta (servida desde `/imagenes/len/dia1/pregunta_17.jpg`)
8. Si hay video YouTube → aparece boton rojo antes de responder
9. Al terminar → ve puntaje, porcentaje, detalle de respuestas y mensaje motivacional
10. El resultado se guarda automaticamente en hoja `Resultados`
11. Al completar todas las materias de un dia → se desbloquea el dia siguiente

### Logica de dias
- El progreso de dias completados se guarda en **localStorage** del navegador (`examen_estado`)
- El progreso de examen en curso se guarda en **Google Sheets** hoja `Progreso`
- Al terminar un examen → se borra de `Progreso` automaticamente

---

## 📤 Como subir preguntas nuevas

### Script PowerShell reutilizable
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
    body={'values':rows}).execute()
print('LISTO', len(rows), 'preguntas subidas')
"
```

- Cambiar `ARCHIVO.xlsx` por el nombre del archivo en Descargas
- Cambiar `HOJA` por ej. `Dia1_LEN`, `Dia4_QUI`, etc.
- El Excel generado tiene 9 columnas: Tema | Pregunta | OpA | OpB | OpC | OpD | Respuesta | Explicacion(popup) | URL_Imagen
- El script sube: r[1]=Pregunta, r[2-5]=Opciones, r[6]=Respuesta, r[8]=ImagenURL

> ⚠️ IMPORTANTE: siempre usar `valueInputOption='RAW'` para que la letra de respuesta no se interprete como formula

---

## 🖼️ Como agregar imagenes

### Flujo completo
1. Generar imagen con **Gemini** usando el prompt del Excel (ultima fila en color naranja)
2. Guardar en la carpeta correcta
3. Crear la carpeta si no existe:
```powershell
mkdir C:\guia_sexto\public\imagenes\len\dia4
```
4. Comprimir con `comprimir.py` (convierte PNG a JPG y borra el PNG original)
5. Push a GitHub → Vercel publica en ~2 minutos

### Script comprimir.py (C:\guia_sexto\comprimir.py)
```python
from PIL import Image
import os

carpeta = r'C:\guia_sexto\public\imagenes\len\dia1'  # cambiar por la carpeta correcta

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
```powershell
python C:\guia_sexto\comprimir.py
```

### Convencion de nombres de archivo
- **Lenguaje:** `pregunta_03.jpg` (minuscula, guion bajo, numero con cero si es menor a 10)
- **Matematicas:** `PREGUNTA3.jpg` (mayuscula, sin guion, sin cero)
- El nombre del archivo debe coincidir EXACTAMENTE con la URL guardada en columna G del Sheet

### URLs resultantes
```
https://guia-sexto.vercel.app/imagenes/len/dia1/pregunta_17.jpg
https://guia-sexto.vercel.app/imagenes/len/dia2/pregunta_03.jpg
https://guia-sexto.vercel.app/imagenes/mat/dia5/PREGUNTA3.jpg
```

### Push a GitHub
```powershell
cd C:\guia_sexto
git add .
git commit -m "imagenes lenguaje dia3"
git push
```

---

## 🎬 Como agregar videos

1. Copiar URL de YouTube (ej. `https://youtu.be/XXXXXXX`)
2. Pegar en columna **H** del Sheet como texto plano
3. Si Sheets lo convierte en hipervinculo, usar script:
```powershell
python -c "
from google.oauth2 import service_account
from googleapiclient.discovery import build
creds = service_account.Credentials.from_service_account_file(r'C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json',scopes=['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=creds)
service.spreadsheets().values().update(
    spreadsheetId='136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg',
    range='Dia1_LEN!H2', valueInputOption='RAW',
    body={'values': [['https://youtu.be/XXXXXXX']]}).execute()
print('LISTO')
"
```

---

## 👥 Como agregar usuarios

En el Sheet → hoja `Usuarios` → agregar fila:
| Codigo | Nombre |
|--------|--------|
| NUEVO2026 | Nombre del nino |

El codigo es case-insensitive.

---

## 🚀 Deploy

```powershell
cd C:\guia_sexto
git add .
git commit -m "descripcion del cambio"
git push
```
Vercel redeploya automaticamente en ~2 minutos.

---

## 📋 Pendiente

- [ ] Cargar preguntas de LEN dias 4, 5 y 6
- [ ] Subir imagenes de LEN dia 3 (5 imagenes — ver prompts en Dia3_LEN.xlsx)
- [ ] Cargar preguntas de BIO, QUI, SOC para los 6 dias
- [ ] Agregar videos de YouTube por tema en columna H
- [ ] Crear codigos de acceso para cada estudiante en hoja Usuarios
- [ ] Implementar popup de explicacion en la app (columna H del Excel → mostrar despues de responder)
- [ ] Verificar que hoja Resultados acumula bien al terminar cada examen
