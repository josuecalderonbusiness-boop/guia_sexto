# 📚 METODOLOGIA DE PREGUNTAS — EXAMEN NINOS
## Guia de Referencia para Generacion de Bancos de Preguntas

**Proyecto:** Plataforma de evaluacion interactiva para sexto grado  
**URL:** https://guia-sexto.vercel.app  
**Sistema:** Preguntas de seleccion multiple (A/B/C/D), una sola respuesta correcta  
**Formato de entrega:** Excel (.xlsx) generado con Python/openpyxl — 9 columnas

---

## ⚙️ REGLAS TECNICAS DEL SISTEMA

Antes de generar cualquier pregunta, respetar estas reglas sin excepcion:

1. **Sin LaTeX** — No usar simbolos matematicos especiales. Usar texto plano: `raiz(16)`, `3/4`, `2^3`
2. **Sin patron en respuestas** — La secuencia de respuestas correctas debe ser completamente aleatoria, sin alternancia visible. Ver seccion de distribucion abajo.
3. **Enunciado en una sola celda** — Los sub-ejercicios se separan con `/` o numerados `1)... 2)... 3)...`
4. **Opciones completas** — Cada opcion debe ser autocontenida, sin depender de leer las otras
5. **Texto limpio** — Sin simbolos raros, sin comillas dobles dentro de celdas, sin saltos de linea innecesarios
6. **28 preguntas por examen** — Nunca menos de 25
7. **Respuestas incorrectas creibles** — Los distractores deben ser errores tipicos del nivel, no absurdos obvios
8. **Minimo 5 imagenes por examen** — Obligatorio en dias 3, 4, 5 y 6. Minimo 2 en dias 1 y 2.
9. **Cada pregunta tiene explicacion popup** — Columna H del Excel, texto pedagogico para mostrar despues de responder

---

## 🔀 DISTRIBUCION DE RESPUESTAS SIN PATRON

### El problema a evitar
Los estudiantes son audaces y detectan patrones. Si la respuesta siempre esta en C, o alterna ABCDABCD, lo notaran y no estudiaran de verdad.

### La solucion
Al generar el Excel con Python, se define una SECUENCIA manual de 28 letras con estas reglas:
- A x7, B x7, C x7, D x7 — distribucion perfecta e igual
- Sin alternancia visible (no ABAB, no CDCD, no ABCDABCD)
- Sin rachas largas de la misma letra (maximo 2 seguidas de vez en cuando)
- Cada examen usa una secuencia diferente a los demas

### Ejemplo de secuencias validas usadas
```
Dia 1 LEN: B A D C A D B C D A C B A D C B D A B C A D C B D A C B
Dia 2 LEN: C A D B A C D B C D A B D C A B D A C B A D B C A D C B
Dia 3 LEN: D B A C D A B C A D C B A C D B C A D B B C A D C B D A
```

### Como funciona tecnicamente
Las opciones de cada pregunta se REORDENAN para que la correcta caiga en la posicion asignada por la secuencia:

```python
def ordenar_opciones(opciones_4, letra_destino):
    # opciones_4[0] es SIEMPRE la respuesta correcta
    # opciones_4[1], [2], [3] son los distractores
    idx = ord(letra_destino) - ord('A')  # A=0, B=1, C=2, D=3
    correcta = opciones_4[0]
    incorrectas = list(opciones_4[1:])
    incorrectas.insert(idx, correcta)    # insertar correcta en posicion destino
    return incorrectas
```

Esto garantiza que la respuesta correcta siempre caiga en la letra asignada por la secuencia, sin importar en que posicion fue escrita originalmente.

---

## 📅 ESTRUCTURA DE DIFICULTAD POR DIA

| Dia | Nivel | Enfoque |
|-----|-------|---------|
| 1 | Basico — Reconocimiento | Identificacion primaria, reglas, mecanicas simples |
| 2 | Medio-Bajo — Aplicacion directa | Textos cortos, ejercicios directos, aplicacion de reglas |
| 3 | Medio — Procesos con pasos | Analisis encadenado, textos mas largos, justificacion |
| 4 | Medio-Alto — Contexto y narrativa | Situaciones reales, relaciones entre textos, inferencia |
| 5 | Alto — Razonamiento y graficos | Tablas, diagramas, analisis de errores, soporte visual |
| 6 | Desafio final — Fusion | Dos temas combinados, casos limite, excepciones avanzadas |

---

## 🖼️ REGLAS PARA IMAGENES

### Cantidad minima por examen
- Dias 1 y 2: minimo 2 imagenes
- Dias 3, 4, 5 y 6: minimo 5 imagenes

### Como se declaran en el Excel
- El enunciado incluye la etiqueta: `[MIRA EL GRAFICO EN TU PANTALLA]`
- La columna I del Excel contiene la URL completa lista para usar:
```
https://guia-sexto.vercel.app/imagenes/len/dia2/pregunta_08.jpg
```

### Convencion de nombres de archivo
- **Lenguaje:** `pregunta_03.jpg` (minuscula, guion bajo, numero con cero si es menor a 10)
- **Matematicas:** `PREGUNTA3.jpg` (mayuscula, sin guion, sin cero)
- Carpeta en disco: `C:\guia_sexto\public\imagenes\[materia]\dia[N]\`

### Flujo de trabajo para imagenes (siempre el mismo)
1. Copiar el prompt de la ultima fila del Excel (fila de notas en color naranja)
2. Pegar el prompt en **Gemini** para generar la imagen
3. Guardar la imagen en la carpeta correcta con el nombre exacto
4. Modificar `comprimir.py` con la carpeta correcta y ejecutar:
   ```powershell
   python C:\guia_sexto\comprimir.py
   ```
5. Hacer push:
   ```powershell
   cd C:\guia_sexto
   git add .
   git commit -m "imagenes lenguaje diaN"
   git push
   ```
6. En 2 minutos Vercel publica y las URLs del Sheet funcionan

### Tipos de imagen mas utiles por tipo de pregunta

| Tipo de pregunta | Imagen ideal |
|-----------------|--------------|
| Idea principal | Diagrama de parrafo con 3 zonas en color (verde=idea principal, azul=ideas secundarias, naranja=cierre) |
| Intencion comunicativa | Tarjetas de texto (noticia, poema, receta, carta) con etiquetas |
| Generos literarios | Fragmentos de texto de cada genero con etiquetas de identificacion |
| Tipos de narrador | Tres fragmentos con pronombres destacados en color |
| Ortografia | Parrafo con palabras subrayadas, verde=correcto, rojo=error |
| Campo lexico | Mapa mental con palabra central y ramas de palabras relacionadas |
| Partes del texto | Texto dividido en secciones con colores y etiquetas |
| Figuras literarias | Verso resaltado con etiqueta de la figura literaria |
| Conectores logicos | Parrafo con conectores destacados en color con su tipo |
| Comprension lectora | Texto informativo corto tipo enciclopedia o articulo |

---

## 📐 ESTRUCTURA DEL EXCEL GENERADO

### Columnas (9 en total)

| Col | Contenido | Nota |
|-----|-----------|------|
| A | Tema | Ej: "Generos Literarios", "Ortografia" |
| B | Enunciado de la Pregunta | Incluye [MIRA EL GRAFICO] si tiene imagen |
| C | Opcion A | Autocontenida |
| D | Opcion B | Autocontenida |
| E | Opcion C | Autocontenida |
| F | Opcion D | Autocontenida |
| G | Respuesta Correcta | Solo la letra: A, B, C o D |
| H | Explicacion popup | Texto pedagogico para mostrar despues de responder |
| I | URL Imagen | URL completa o vacio si no tiene imagen |

### Lo que se sube al Sheet (7 columnas)
El script de PowerShell lee el Excel y sube:
- r[1] = Pregunta → columna A del Sheet
- r[2] = Opcion A → columna B del Sheet
- r[3] = Opcion B → columna C del Sheet
- r[4] = Opcion C → columna D del Sheet
- r[5] = Opcion D → columna E del Sheet
- r[6] = Respuesta → columna F del Sheet
- r[8] = URL Imagen → columna G del Sheet

> La columna H (explicacion popup) del Excel NO se sube al Sheet todavia.
> Queda pendiente implementar el popup en el codigo de la app (index.html).

---

## 🎯 TIPOS DE PREGUNTA DISPONIBLES

### ✅ TIPO 1 — BLOQUE MULTIEJERCICIO
**Que es:** Agrupa 3 a 5 sub-ejercicios rapidos en un solo enunciado. El nino los resuelve todos y compara con las opciones.
**Cuando usarlo:** Clasificaciones multiples, operaciones, identificacion de varias palabras.
**Cuantas por examen:** 3 a 5

---

### ✅ TIPO 2 — EL INTRUSO
**Que es:** 4 elementos donde 3 cumplen una propiedad y 1 la rompe. Identificar el que no pertenece.
**Cuando usarlo:** Clasificaciones, generos, clases de palabras, campos lexicos.
**Cuantas por examen:** 2 a 3

---

### ✅ TIPO 3 — VERDADERO O FALSO CON ARGUMENTO
**Que es:** Un personaje ficticio hace una afirmacion. El nino elige la justificacion correcta del error o la confirmacion.
**Cuando usarlo:** Conceptos mal entendidos frecuentemente, reglas que se confunden.
**Cuantas por examen:** 2 a 3

---

### ✅ TIPO 4 — CON IMAGEN [MIRA EL GRAFICO EN TU PANTALLA]
**Que es:** El enunciado referencia una imagen que aparece en pantalla. La columna I tiene la URL completa.
**Cuando usarlo:** Comprension de diagramas, textos visuales, tablas, mapas mentales, poemas con figuras.
**Cuantas por examen:** minimo 2 en dias 1-2, minimo 5 en dias 3-6

---

### ✅ TIPO 5 — EMPAREJAMIENTO
**Que es:** Lista de elementos que deben relacionarse con sus definiciones, generos, tipos o pares.
**Cuando usarlo:** Vocabulario, transformaciones, tipos de narrador, intenciones comunicativas.
**Cuantas por examen:** 2 a 3

---

### ✅ TIPO 6 — ANALISIS DE ERROR
**Que es:** Se muestra un procedimiento o texto incorrecto y el estudiante identifica el fallo o lo corrige.
**Cuando usarlo:** Ortografia, concordancia verbal, estructura de parrafo, jerarquia de operaciones.
**Cuantas por examen:** 2 a 3

---

### ✅ TIPO 7 — PREGUNTA DE LECTURA
**Que es:** Parrafo corto (2-5 lineas) seguido de una pregunta de comprension, inferencia o identificacion.
**Cuando usarlo:** Lenguaje, Ciencias Sociales, Biologia, situaciones narradas.
**Cuantas por examen:** 3 a 6 (especialmente en Lenguaje)

---

### ✅ TIPO 8 — CON VIDEO [YOUTUBE]
**Que es:** La columna H del Sheet tiene URL de YouTube. Aparece boton rojo antes de responder.
**Cuando usarlo:** Temas abstractos o dificiles de visualizar sin apoyo audiovisual.
**Cuantas por examen:** opcional segun tema

---

## 📊 DISTRIBUCION RECOMENDADA POR EXAMEN (28 preguntas)

| Tipo | Dias 1-2 | Dias 3-4 | Dias 5-6 |
|------|----------|----------|----------|
| Reconocimiento directo | 8-10 | 4-6 | 2-3 |
| Bloque Multiejercicio | 3-4 | 3-4 | 3-4 |
| El Intruso | 2-3 | 2 | 2 |
| V/F con Argumento | 2-3 | 2-3 | 2-3 |
| Analisis de Error | 1-2 | 2-3 | 3-4 |
| Pregunta de Lectura | 2-3 | 4-5 | 5-6 |
| Con Imagen | 2 min | 5 min | 6-7 |
| Con Video | opcional | opcional | opcional |
| **Total** | **28** | **28** | **28** |

---

## 🗂️ COMO GENERAR UN EXAMEN NUEVO

### Lo que se necesita antes de generar
1. **Materia:** MAT / BIO / QUI / SOC / LEN
2. **Dia:** 1 al 6
3. **Lista de temas** del curriculo de esa materia
4. **Nivel del dia:** ver tabla de dificultad arriba

### Lo que se entrega siempre
- Archivo Excel `.xlsx` con 28 preguntas listas
- Respuestas sin patron — nueva secuencia aleatoria unica para cada examen
- URLs de imagen completas en columna I (listas para pegar en la carpeta y hacer push)
- Prompts para Gemini de cada imagen en la ultima fila del Excel (color naranja)
- Script de PowerShell listo para subir al Sheet

### Script de subida al Sheet (el mismo siempre)
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
> Cambiar `ARCHIVO.xlsx` por el nombre del archivo y `HOJA` por ej. `Dia4_LEN`

---

## 📋 TEMAS POR MATERIA

### 🔢 MATEMATICAS (MAT) — Completa dias 1-6 ✅
Numeros Romanos, Raiz Cuadrada, Operaciones con Enteros, Ecuaciones Lineales, Racionales e Irracionales, Poligonos, Transformaciones, Triangulos, Jerarquia de Operaciones, Criterios de Divisibilidad, MCM y MCD, Perimetro y Area, Estadistica y Probabilidad, Potenciacion

### 📖 LENGUAJE (LEN) — Dias 1-3 completos ✅ | Dias 4-6 pendientes ⬜

**Temas principales:**
- Comprension lectora
- Generos literarios (narrativo, lirico, dramatico)
- Partes del texto (introduccion, desarrollo, conclusion)
- Tipos de narrador (primera persona, omnisciente, testigo, segunda persona)
- Clases de palabras: sustantivo, adverbio, verbo, adjetivo, pronombre, preposicion
- Subgeneros narrativos: cuento, novela, fabula, mito, leyenda
- Textos dramaticos: actos, escenas, acotaciones, monologo, dialogo
- Enunciado, oracion y parrafo
- Idea principal e ideas secundarias
- Campo lexico
- Ortografia y acentuacion (agudas, graves, esdrujulas)

**Temas puente (aparicion ligera — no son el centro pero deben saberse):**
- Sinonimos, antonimos, homonimas
- Conectores logicos (adicion, oposicion, consecuencia, causa)
- Intencion comunicativa (informativa, apelativa, poetica, expresiva)
- Figuras literarias basicas (personificacion, metafora, hiperbole)

### 🌿 BIOLOGIA (BIO) — Pendiente ⬜
Celula, Tejidos y Organos, Sistemas del cuerpo humano, Ecosistemas, Cadenas alimenticias, Fotosintesis, Reproduccion, Clasificacion de seres vivos, Genetica basica, Microorganismos, Biomas, Evolucion basica, Salud e higiene, Ciclos del agua y nutrientes

### ⚗️ QUIMICA (QUI) — Pendiente ⬜
Materia y propiedades, Estados de la materia, Cambios fisicos y quimicos, Mezclas y soluciones, Elementos y compuestos, Tabla periodica basica, Atomos y moleculas, Reacciones quimicas, Acidos y bases, Metales y no metales, Combustion, Oxidacion, Densidad, Energia quimica

### 🌍 CIENCIAS SOCIALES (SOC) — Pendiente ⬜
Mapas y coordenadas geograficas, Regiones naturales de Colombia, Clima y relieve, Continentes y oceanos, Cultura y diversidad, Historia de Colombia, Constitucion politica basica, Derechos humanos, Economia basica, Migraciones, Medio ambiente, Gobierno y democracia, Civilizaciones antiguas, Conflictos mundiales basicos

---

## 🚀 ESTADO ACTUAL DEL BANCO DE PREGUNTAS

| Materia | D1 | D2 | D3 | D4 | D5 | D6 |
|---------|----|----|----|----|----|----|
| MAT | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LEN | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ |
| BIO | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| QUI | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| SOC | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
