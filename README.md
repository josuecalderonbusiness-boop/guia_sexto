# 🎓 Examen Ninos

App de exámenes interactiva para niños, con preguntas desde Google Sheets y progresión por días.

## Variables de entorno en Vercel

Agrega estas dos variables en tu proyecto de Vercel (Settings → Environment Variables):

| Variable | Valor |
|---|---|
| `SHEET_ID` | `136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg` |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | El contenido completo del archivo JSON que bajaste |

> ⚠️ Para `GOOGLE_SERVICE_ACCOUNT_JSON`: abre el archivo JSON, selecciona TODO el contenido y pégalo como valor de la variable.

## Primer uso: configurar el Sheet

Después de deployar, visita una vez:
```
https://tu-app.vercel.app/api/setup
```
Esto crea automáticamente todas las hojas en el Google Sheet:
- `Dia1_MAT`, `Dia1_BIO`, `Dia1_QUI`, `Dia1_SOC`, `Dia1_LEN`
- `Dia2_MAT` ... hasta `Dia6_LEN`
- `Resultados`

## Cómo cargar preguntas

En cada hoja (ej. `Dia1_MAT`) el formato es:

| A: Pregunta | B: Opción A | C: Opción B | D: Opción C | E: Opción D | F: Respuesta Correcta |
|---|---|---|---|---|---|
| ¿Cuánto es 2+2? | 3 | 4 | 5 | 6 | B |

- La fila 1 es el encabezado (ya creado por /api/setup)
- Filas 2 a 26 = hasta 25 preguntas por examen
- La columna F acepta A, B, C o D

## Estructura del proyecto

```
examen-ninos/
├── api/
│   ├── preguntas.js   → GET /api/preguntas?dia=1&materia=MAT
│   ├── guardar.js     → POST /api/guardar
│   └── setup.js       → GET /api/setup (solo 1 vez)
├── public/
│   └── index.html     → La app completa
├── package.json
└── vercel.json
```

## Deploy

```bash
npm i -g vercel
vercel --prod
```
