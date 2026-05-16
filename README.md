# 🧠 Brainy — App de Exámenes Interactiva

App educativa para niños de grado 6, con preguntas desde Google Sheets, progresión por días, refuerzo con IA y mascota Brainy.

**URL:** https://brainykids.online  
**Alternativa:** https://guia-sexto.vercel.app

---

## Variables de entorno en Vercel

Agrega estas variables en Settings → Environment Variables:

| Variable | Valor |
|---|---|
| `SHEET_ID` | `136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg` |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Contenido completo del archivo JSON de Google Cloud |
| `OPENAI_API_KEY` | Key de platform.openai.com (modelo gpt-4o-mini) |

---

## Estructura del proyecto

```
brainy/
├── api/
│   ├── preguntas.js   → GET /api/preguntas?dia=1&materia=MAT
│   ├── guardar.js     → POST /api/guardar
│   ├── resultados.js  → GET /api/resultados?nombre=Tomas
│   ├── setup.js       → GET /api/setup (solo 1 vez)
│   ├── login.js       → POST /api/login
│   ├── progreso.js    → GET/POST/DELETE /api/progreso
│   └── explicar.js    → POST /api/explicar (IA via OpenAI)
├── public/
│   ├── index.html           → App completa
│   ├── favicon.png          → Favicon Brainy
│   └── imagenes/
│       └── logos/
│           ├── brainy.png         → Logo texto
│           └── brainy_mascota.png → Mascota
├── package.json
└── vercel.json
```

---

## Funcionalidades

### Examen
- Login con codigo de acceso verificado en Google Sheets
- 6 dias × 5 materias (MAT, BIO, QUI, SOC, LEN)
- 25-28 preguntas por examen con seleccion multiple A/B/C/D
- Imagenes y videos YouTube por pregunta
- Guardado automatico de progreso en Sheets
- Desbloqueo de dias al completar todas las materias

### Refuerzo IA ✨
- Al terminar con errores → boton "🔁 Corrige tus errores con IA"
- Al responder mal en examen → boton "🤖 ¿Por qué era esa?"
- OpenAI GPT-4o-mini genera explicacion personalizada en lenguaje de niño
- Boton "Continuar →" aparece solo despues de leer la explicacion
- Auto-avance en 15 segundos si no toca el boton
- Comparacion de puntaje original vs refuerzo
- Se guarda en Sheets como sesion de refuerzo

### Admin
- Dashboard con estadisticas globales
- Perfil por alumno con barras de progreso
- Analisis de falencias del grupo
- Gestion de usuarios (agregar/eliminar codigos)

---

## Como cargar preguntas

En cada hoja (ej. `Dia1_MAT`) el formato es:

| A: Pregunta | B: Opción A | C: Opción B | D: Opción C | E: Opción D | F: Respuesta | G: URL Imagen | H: URL Video |
|---|---|---|---|---|---|---|---|
| ¿Cuánto es 2+2? | 3 | 4 | 5 | 6 | B | https://... | https://youtu.be/... |

---

## Deploy

```powershell
cd C:\guia_sexto
git add .
git commit -m "descripcion"
git push
```

Vercel redeploya en ~2 minutos automaticamente.
