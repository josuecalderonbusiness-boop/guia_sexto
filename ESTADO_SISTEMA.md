# 🧠 Brainy — Estado del Sistema

**Fecha última actualización:** 16 de mayo de 2026  
**Nombre de la app:** Brainy (antes "Mis Exámenes")  
**URL producción:** https://brainykids.online  
**URL alternativa:** https://guia-sexto.vercel.app  
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
│   ├── progreso.js       → GET/POST/DELETE /api/progreso
│   └── explicar.js       → POST /api/explicar (explicaciones IA via OpenAI)
├── public/
│   ├── index.html        → App completa (toda la UI en un solo archivo)
│   ├── favicon.png       → Favicon de Brainy
│   └── imagenes/
│       ├── logos/
│       │   ├── brainy.png         → Logo texto "BRAINY"
│       │   └── brainy_mascota.png → Mascota cerebro con birrete
│       ├── mat/
│       │   └── dia5/
│       │       ├── PREGUNTA3.jpg ... PREGUNTA25.jpg
│       └── len/
│           ├── dia1/ (pregunta_17, pregunta_24)
│           ├── dia2/ (pregunta_03, 08, 14, 19, 25)
│           └── dia3/ (pregunta_04, 09, 15, 21, 26)
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

### Usuarios registrados

| Codigo | Nombre | Rol |
|--------|--------|-----|
| TOMAS2026 | Tomas | Alumno |
| JERO2026 | Jero | Alumno |
| ADMIN2026 | Admin | Administrador |

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
OPENAI_API_KEY = sk-... (key nombre: guia-sexto en platform.openai.com)
```

### Google Cloud
- **Proyecto:** `examen-ninos`
- **Service Account:** `examen-ninos-sheets@examen-ninos.iam.gserviceaccount.com`
- **JSON key:** `C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json`
- **API habilitada:** Google Sheets API

### OpenAI
- **Cuenta:** platform.openai.com → josue calderon
- **Key activa:** nombre `guia-sexto` (creada 16 mayo 2026)
- **Saldo disponible:** ~$3.24 USD
- **Modelo usado:** `gpt-4o-mini` (muy económico — ~$0.01 por 1000 explicaciones)
- **⚠️ IMPORTANTE:** Si creas una nueva key, actualiza `OPENAI_API_KEY` en Vercel y haz redeploy

### Dominio
- **Dominio:** brainykids.online (comprado en Namecheap)
- **DNS configurado en Namecheap:**
  - A Record `@` → `216.198.79.1`
  - CNAME `www` → `4d8beaf5e973a3ec.vercel-dns-017.com`
- **Dominio agregado en Vercel:** Settings → Domains

---

## 🖥️ Como funciona la app

### Flujo del usuario
1. Entra a https://brainykids.online
2. Escribe su **codigo de acceso** (ej. `TOMAS2026`) — verificado contra hoja `Usuarios`
3. Ve la pantalla de inicio con los 6 dias y 5 materias
4. Si tiene un examen a medias → aparece banner verde "Examen en progreso" con boton Continuar
5. Elige dia y materia → empieza el examen
6. Al responder mal → aparece boton morado **"🤖 ¿Por qué era esa?"**
   - Si lo toca → Claude/OpenAI genera explicacion personalizada en lenguaje de niño
   - Aparece boton verde **"Continuar →"** para pasar a la siguiente pregunta
   - Si no lo toca → pasa automaticamente en 15 segundos
7. Si hay imagen → aparece encima de la pregunta
8. Si hay video YouTube → aparece boton rojo antes de responder
9. Al terminar → ve puntaje, porcentaje, detalle de respuestas y mensaje motivacional
10. Si tuvo errores → aparece boton **"🔁 Corrige tus errores con IA"**
11. El resultado se guarda automaticamente en hoja `Resultados`
12. Al completar todas las materias de un dia → se desbloquea el dia siguiente

### Sistema de Refuerzo IA (nuevo - 16 mayo 2026)
- Al terminar un examen con errores → boton "🔁 Corrige tus errores con IA"
- En el menu principal → boton de refuerzo por cada materia con errores previos
- En el refuerzo:
  1. Muestra la pregunta que fallo con la respuesta incorrecta anterior
  2. **Claude/OpenAI explica** por que estaba mal y da un tip para recordarlo
  3. El nino responde de nuevo la misma pregunta
  4. Al terminar → compara puntaje nuevo vs original
  5. Se guarda en Sheets como `"Dia X (Refuerzo)"`
- Los errores se guardan en **localStorage** con clave `errores_DIA_MATERIA`

### Logica de dias
- El progreso de dias completados se guarda en **localStorage** del navegador (`examen_estado`)
- El progreso de examen en curso se guarda en **Google Sheets** hoja `Progreso`
- Al terminar un examen → se borra de `Progreso` automaticamente

---

## 🤖 API de explicaciones IA (api/explicar.js)

Endpoint: `POST /api/explicar`

**Body:**
```json
{
  "pregunta": "texto de la pregunta",
  "opciones": { "A": "...", "B": "...", "C": "...", "D": "..." },
  "elegida": "C",
  "correcta": "A"
}
```

**Respuesta:**
```json
{ "ok": true, "explicacion": "texto generado por GPT-4o-mini" }
```

**Costo:** ~$0.0001 por explicacion. Con 5 alumnos haciendo refuerzo diario = menos de $0.50/mes.

---

## 🎨 Identidad visual — Brainy

- **Nombre:** Brainy
- **Mascota:** Cerebro cartoon verde con birrete de graduacion, ojos grandes, sonrisa amigable
- **Logo texto:** "BRAINY" en letras redondeadas purpura a azul
- **Favicon:** Cerebro mascota (icono circular)
- **Archivos:**
  - `public/imagenes/logos/brainy.png` → logo texto
  - `public/imagenes/logos/brainy_mascota.png` → mascota completa
  - `public/favicon.png` → favicon
- **Herramienta usada:** Gemini para generar, CorelDRAW para editar
- **Quitar fondo:** remove.bg

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
- ⚠️ IMPORTANTE: siempre usar `valueInputOption='RAW'`

---

## 🖼️ Como agregar imagenes

### Flujo completo
1. Generar imagen con **Gemini** usando el prompt del Excel (ultima fila en color naranja)
2. Guardar en la carpeta correcta
3. Comprimir con `comprimir.py`
4. Push a GitHub → Vercel publica en ~2 minutos

### Convencion de nombres
- **Lenguaje/BIO/QUI/SOC:** `pregunta_03.jpg` (minuscula, guion bajo, cero si numero < 10)
- **Matematicas:** `PREGUNTA3.jpg` (mayuscula, sin guion, sin cero)

---

## 🚀 Deploy

```powershell
cd C:\guia_sexto
git add .
git commit -m "descripcion del cambio"
git push
```
Vercel redeploya automaticamente en ~2 minutos. Disponible en brainykids.online y guia-sexto.vercel.app.

---

## 📋 Pendiente

- [ ] Cargar preguntas de LEN dias 4, 5 y 6
- [ ] Subir imagenes de LEN dia 3 (5 imagenes — ver prompts en Dia3_LEN.xlsx)
- [ ] Cargar preguntas de BIO, QUI, SOC para los 6 dias
- [ ] Agregar videos de YouTube por tema en columna H
- [ ] Quitar fondo a brainy.png y brainy_mascota.png con remove.bg
- [ ] Animacion de celebracion con mascota Brainy al terminar examen con buena nota
- [ ] Implementar popup de explicacion en la app (columna H del Excel → mostrar despues de responder)

---

## ✅ Historial de cambios — 16 mayo 2026

- ✅ Sistema de refuerzo IA completo (errores → explicacion OpenAI → reintento → comparacion)
- ✅ Boton "🤖 ¿Por qué era esa?" en examen normal al responder mal
- ✅ Boton "Continuar →" aparece solo despues de leer la explicacion
- ✅ Auto-avance en 15 segundos si no toca el boton de explicacion
- ✅ api/explicar.js con OpenAI GPT-4o-mini como backend
- ✅ OPENAI_API_KEY configurada en Vercel
- ✅ Nombre cambiado a **Brainy**
- ✅ Logo, mascota y favicon de Brainy integrados
- ✅ Dominio brainykids.online configurado y funcionando
- ✅ DNS configurado en Namecheap apuntando a Vercel
