const { google } = require('googleapis');
const https = require('https');

const SHEET_ID = process.env.SHEET_ID;

// ── Currículo completo de Jero (grado 2) ────────────────────────────
const CURRICULO = {
  MAT: [
    'Valor posicional hasta 4 cifras: Unidades, Decenas, Centenas y Unidades de Mil. Lectura y escritura de números en cifras y en palabras. Descomposición aditiva (ej: 1345 = 1000+300+40+5). Equivalencias: cuántas unidades hay en 3 centenas, cuántas decenas forman 1 centena.',
    'Comparación y orden de números hasta 4 cifras: mayor que, menor que e igual a. Número anterior, posterior y entre. Series numéricas ascendentes y descendentes de 2 en 2, de 5 en 5, de 10 en 10 y de 100 en 100. Números ordinales del primero al vigésimo.',
    'Adición hasta 4 dígitos con reagrupación en decenas y centenas simultáneamente. Términos: sumandos y total. Sumas verticales y horizontales. Problemas verbales con palabras clave: agrupar, reunir, en total.',
    'Sustracción hasta 4 dígitos con desagrupación consecutiva. Caso especial: restar a números con ceros intermedios (ej: 500-124). Términos: minuendo, sustraendo y diferencia. Prueba de la resta: sustraendo + diferencia = minuendo.',
    'Multiplicación: tablas del 2 al 9. Multiplicación como adición iterada (ej: 4+4+4+4+4 = 5x4). Arreglos rectangulares filas por columnas. Propiedad conmutativa (3x5 = 5x3). Palabras clave: el triple, el doble, repetir.',
    'División intuitiva: reparto en partes iguales. Mitad (dividir entre 2) y doble (multiplicar por 2). Problemas de repartir objetos en grupos iguales. Relación entre multiplicación y división básica.',
    'Resolución de problemas de un paso con enunciado verbal: identificar palabras clave para elegir la operación correcta entre suma, resta y multiplicación. Extraer datos y redactar respuesta completa.',
    'Resolución de problemas de dos pasos combinando suma y resta. Situaciones de la vida real con compras, frutas, juguetes. Identificar qué operación va primero.',
    'Geometría plana: círculo, triángulo, cuadrado, rectángulo, rombo y óvalo. Contar lados y vértices. Reconocer ángulos rectos y oblicuos. Clasificar figuras por número de lados.',
    'Cuerpos geométricos: cubo, esfera, cilindro, cono y pirámide. Diferencia entre figuras planas y sólidos tridimensionales. Clasificar en los que ruedan y los que no ruedan. Caras, aristas y vértices básico.',
    'Líneas rectas, curvas, abiertas y cerradas. Líneas paralelas y perpendiculares. Simetría: identificar eje de simetría y completar figuras simétricas.',
    'Medición de longitud: centímetros y metros. Uso correcto de la regla desde el cero. Comparar longitudes. Unidades arbitrarias vs estándar.',
    'El reloj analógico: aguja horaria corta y minutero largo. Horas en punto y medias horas. El calendario: días de la semana, meses del año. Problemas con fechas: si hoy es martes 15 qué día será el 18.',
    'Capacidad y masa: comparar objetos en una balanza. Qué recipiente almacena más líquido. Litro como unidad básica. Conceptos de más pesado, más liviano, lleno y vacío.',
    'Gráficas de barras sencillas: leer e interpretar datos. Tablas de conteo con palitos. Responder preguntas: cuál es el mayor, cuál el menor, cuántos más que, cuántos en total.',
    'Operaciones combinadas: elegir la operación correcta entre suma, resta y multiplicación según el contexto. Problemas mixtos con geometría y medidas.',
    'Valor posicional avanzado: descomposición y composición de números de 4 cifras. Forma desarrollada y compacta. Comparar y ordenar series de cuatro números de mayor a menor.',
    'Tablas del 6, 7, 8 y 9. Patrones de multiplicación. Problemas de multiplicación con contexto real. Verificar resultado con suma repetida.',
    'Números ordinales del primero al vigésimo en situaciones reales: carreras, filas, posiciones. Secuencias numéricas con patrones mixtos.',
    'Repaso integral: pensamiento numérico, operaciones con reagrupación, geometría, medidas y estadística. Problemas de dos pasos nivel grado 2 transición a grado 3.',
  ],
  LCA: [
    'Comprensión lectora literal: identificar personajes principales y secundarios, lugar y tiempo. Ordenar eventos cronológicamente usando conectores: primero, después, luego, al final.',
    'Comprensión lectora inferencial: deducir el propósito del texto (divertir, informar, instruir). Predecir resultados y deducir sentimientos o motivaciones de los personajes.',
    'Comprensión lectora crítica: opinión personal sustentada sobre la actitud de un personaje. Identificar la moraleja o enseñanza de una fábula. Distinguir realidad de fantasía en un cuento.',
    'La oración: sujeto (quién realiza la acción) y predicado (lo que se dice). Núcleo del sujeto (sustantivo) y núcleo del predicado (verbo). Identificar oraciones completas e incompletas.',
    'Conectores lógicos: aditivos (y, también, además), causales (porque, ya que), adversativos (pero, sin embargo), consecutivos (entonces, por eso). Usar conectores para unir oraciones y formar párrafos.',
    'Tipologías textuales: cuento/fábula (narrativo), poesía con rima, receta o instrucción (texto instructivo). Diferencias visuales y estructurales entre cada tipo.',
    'El sustantivo: propios (nombres, ciudades, apellidos — llevan mayúscula) y comunes (objetos, animales, cosas). Concordancia de género y número: detectar errores como "los gatas blancos".',
    'El adjetivo calificativo: asignar cualidades al sustantivo. Concordancia adjetivo-sustantivo en género y número. Describir personajes y objetos con adjetivos precisos.',
    'El verbo: identificar la acción o estado en una oración. Tiempos verbales: pasado (ayer corrí), presente (hoy corro) y futuro (mañana correré). Cambiar oraciones de un tiempo a otro.',
    'Artículos definidos e indefinidos: el, la, los, las, un, una, unos, unas. Pronombres personales: Yo, Tú, Él, Ella, Nosotros, Ellos. Sustituir sustantivos por pronombres correctamente.',
    'Sinónimos (palabras con significado similar: feliz/contento) y antónimos (palabras de significado opuesto: alto/bajo). Ampliar vocabulario y usarlos en oraciones.',
    'Segmentación silábica: dividir palabras en sílabas. Sílaba tónica: la que suena más fuerte. Base para reconocer palabras agudas, graves y esdrújulas.',
    'Uso de mayúsculas: al iniciar oración, después de punto, en nombres propios. Signos de puntuación: punto seguido, punto aparte, punto final, signos de interrogación ¿? y exclamación ¡!.',
    'Reglas ortográficas: M antes de B y P (tambor, campo). Sílabas trabadas: bl, br, cl, cr, fl, fr, pl, pr, gl, gr, tr, dr. Diferenciación b/v, c/s/z, h muda, ge-gi vs je-ji, ll vs y.',
    'Elementos del cuento: inicio (presentación de personajes y lugar), nudo (el problema) y desenlace (solución). Identificar cada parte en textos cortos.',
    'Lenguaje iconográfico: interpretar imágenes, pictogramas y señales de tránsito. Leer una historia narrada en viñetas o cómics sin texto y explicar qué sucede.',
    'Producción textual: ordenar oraciones desordenadas para formar un párrafo con sentido. Identificar la idea principal de un párrafo.',
    'Lectura de texto corto informativo (2 a 4 párrafos) y respuesta a preguntas literales e inferenciales de selección múltiple.',
    'Campo semántico y familia de palabras: agrupar palabras por tema (animales, colores, alimentos). Identificar palabras que no pertenecen al grupo.',
    'Repaso integral: comprensión lectora, gramática aplicada, ortografía y tipos de texto. Preguntas mixtas nivel grado 2 transición a grado 3.',
  ],
  ING: [
    'Numbers 1 to 50: reading and writing in English. Counting objects in images. Identifying quantities. Ordinal numbers: first, second, third, fourth, fifth.',
    'Family members: mother, father, brother, sister, baby, grandmother, grandfather, uncle, aunt, cousin. Describing family using "This is my..." and possessive adjectives my/your/his/her.',
    'School objects: pencil, pen, notebook, eraser, ruler, sharpener, book, chair, desk, backpack. Classroom commands: Open, Close, Listen, Look, Draw, Circle, Write, Stand up, Sit down.',
    'The house and its rooms: bedroom, bathroom, kitchen, living room, garden, door, window. Describing what is in each room using There is / There are.',
    'Animals: pets (dog, cat, fish, bird, rabbit), farm animals (cow, horse, pig, sheep, chicken), wild animals (lion, elephant, monkey, giraffe, tiger). Classifying animals by habitat.',
    'Colors (red, blue, green, yellow, orange, purple, black, white, pink, brown) and shapes (circle, square, triangle, rectangle). Sizes: big/small, tall/short, long/short. Describing objects.',
    'Clothes and weather: T-shirt, pants, skirt, shoes, jacket, hat, socks, dress. Weather: sunny, rainy, windy, cloudy, cold, hot. Connecting weather to appropriate clothing.',
    'The verb To Be present tense: I am, You are, He/She/It is, We are, They are. Affirmative and negative forms. Completing sentences based on images.',
    'Demonstrative pronouns: This is (near) and That is (far). Plural: These are / Those are. Identifying and describing nearby and distant objects.',
    'Expressing likes and dislikes: I like... / I do not like... Applied to food, fruits, animals and activities. Asking and answering: Do you like...? Yes, I do / No, I do not.',
    'Quantifiers and existence: There is (one) and There are (many). Identifying quantities in images. Using a/an with singular nouns.',
    'Possessive adjectives: My, Your, His, Her, Our, Their. Using them to indicate ownership in short sentences and descriptions.',
    'Greetings and personal introduction: Hello, Good morning, Good afternoon, Goodbye. What is your name? How old are you? How are you today? Responding fluently.',
    'Reading short descriptions: 2 to 3 line paragraphs describing a person, animal or object. Answering literal comprehension questions in multiple choice format.',
    'Body parts: head, eyes, ears, nose, mouth, neck, shoulders, arms, hands, fingers, legs, feet. Using "I have..." and "He/She has..." to describe.',
    'Food and drinks: apple, banana, orange, mango, rice, bread, milk, water, juice, egg, cheese. Healthy vs unhealthy food. I eat / I drink vocabulary.',
    'Action verbs in present: run, jump, swim, fly, eat, sleep, play, read, write, draw. Using He/She + verb + s (He runs, She swims).',
    'Prepositions of place: in, on, under, next to, behind, in front of. Describing where objects are in a room using images.',
    'Simple questions: What color is...? How many...? Where is...? What is this? Forming short answers correctly.',
    'Review and mixed assessment: vocabulary fields, verb To Be, likes and dislikes, There is/are, possessives, reading comprehension. Level A1.1 exit exam.',
  ],
  NAT: [
    'Seres vivos e inertes: características de los seres vivos (nacen, crecen, se nutren, respiran, se reproducen y mueren). Diferencia con objetos inertes naturales (rocas, agua) y artificiales (juguetes, ropa).',
    'Las plantas: partes y funciones. Raíz (absorción y fijación), tallo (soporte y transporte), hojas (respiración y fotosíntesis), flores y frutos (reproducción). Necesidades: agua, luz, aire y nutrientes.',
    'Los animales según su alimentación: herbívoros (plantas), carnívoros (carne) y omnívoros (ambos). Ejemplos cotidianos de cada grupo. Identificar de qué se alimenta un animal por sus características físicas.',
    'Los animales según su hábitat y desplazamiento: terrestres (caminan, corren, reptan), acuáticos (nadan) y aéreos (vuelan). Animales que viven en dos medios (anfibios básico).',
    'Animales vertebrados e invertebrados: vertebrados tienen huesos internos (mamíferos, aves, peces, reptiles, anfibios). Invertebrados no tienen huesos (insectos, gusanos, arañas). Clasificar por cubierta corporal: pelos, plumas, escamas, piel desnuda.',
    'Ciclos de vida: la mariposa (huevo, oruga, crisálida, adulto) y la rana (huevo, renacuajo, rana joven, adulto). Comparar etapas y cambios en cada ciclo.',
    'Los cinco sentidos: órganos y funciones. Ojos/visión, oídos/audición, lengua/gusto, nariz/olfato, piel/tacto. Funciones de protección y adaptación. Cuidado de los órganos de los sentidos.',
    'El cuerpo humano: tres zonas. Cabeza (cara, cráneo), tronco (pecho, abdomen, espalda) y extremidades superiores e inferiores. Órganos internos básicos: corazón, pulmones, estómago.',
    'Hábitos saludables: alimentos saludables (frutas, verduras, proteínas) vs no saludables (dulces, ultraprocesados). Higiene corporal: lavado de manos, cepillado de dientes. Ejercicio y sueño adecuado.',
    'Estados de la materia: sólido (forma y volumen definidos), líquido (toma la forma del recipiente) y gaseoso (sin forma ni volumen definidos, se expande). Ejemplos cotidianos de cada estado.',
    'Cambios de estado: fusión (sólido a líquido: hielo que se derrite), evaporación (líquido a gas: agua que hierve), condensación (gas a líquido: vapor que forma gotas). Causa: cambio de temperatura.',
    'Propiedades de los objetos: textura (suave, áspero, rugoso), peso (pesado, liviano) y flexibilidad (rígido, elástico). Propiedades ópticas: transparente (vidrio), translúcido (papel mantequilla) y opaco (madera).',
    'Fuentes de luz: naturales (Sol, estrellas, luciérnagas) y artificiales (bombillo, linterna, pantalla). El sonido como resultado de vibración. Ruidos fuertes vs suaves. Fuentes de sonido.',
    'El planeta Tierra: agua (ríos, mares, lagos), suelo (tierra, rocas, montañas) y aire (atmósfera). Importancia de cada recurso para la vida. Cómo cuidarlos.',
    'El día y la noche: presencia del Sol define el día (luz y calor), ausencia define la noche. Actividades diurnas y nocturnas de animales y personas.',
    'El clima y el tiempo atmosférico: soleado, lluvioso, nublado, ventoso, frío, caliente. Cómo el clima afecta la vestimenta, las actividades y los seres vivos.',
    'La cadena alimenticia básica: productor (plantas), consumidor primario (herbívoro), consumidor secundario (carnívoro) y descomponedor (hongos, bacterias). Construir cadenas simples.',
    'Fuerzas básicas: empujar y jalar para mover objetos. Concepto intuitivo de gravedad (los objetos caen). Flotación: por qué algunos objetos flotan y otros se hunden.',
    'Los recursos naturales: renovables (agua, aire, plantas, animales) y no renovables (petróleo, carbón, minerales). Acciones para cuidar el medio ambiente: ahorro de agua, no contaminar, reciclar.',
    'Repaso integral: seres vivos, cuerpo humano, materia y energía, tierra y universo. Preguntas de pensamiento científico: clasificar, comparar y explicar relaciones causa-efecto. Nivel grado 2 transición a grado 3.',
  ],
  SOC: [
    'El tiempo histórico personal: pasado (ayer, antes), presente (hoy, ahora) y futuro (mañana, después). Secuenciar eventos de la vida propia. Cambios físicos desde bebé hasta hoy.',
    'La familia: tipos de familia (nuclear, extensa, monoparental). Roles y responsabilidades de cada miembro. Lazos de parentesco: padres, abuelos, tíos, primos. Árbol genealógico básico.',
    'Evolución de objetos y costumbres: cómo han cambiado el teléfono, el transporte, la vivienda y la comunicación a lo largo del tiempo. Comparar el antes y el ahora.',
    'Símbolos patrios de Colombia: la bandera (significado de los colores amarillo, azul y rojo), el escudo y el himno nacional. Fechas conmemorativas básicas.',
    'Orientación espacial: derecha, izquierda, adelante, atrás, arriba, abajo, dentro, fuera. Los cuatro puntos cardinales (Norte, Sur, Este, Oeste). El Sol sale por el Este y se oculta por el Oeste.',
    'Lectura de planos sencillos: interpretar el diseño de una casa o salón. Convenciones y símbolos básicos en un mapa (cruz roja = hospital, libro = biblioteca). Noción general de qué es un mapa.',
    'Paisaje rural vs paisaje urbano: campo (naturaleza, cultivos, animales de granja, casas alejadas) vs ciudad (edificios, tráfico, comercio, pavimento). Características y diferencias.',
    'El barrio y la comunidad: lugares representativos (parque, hospital, colegio, tienda, iglesia, estación de policía). Normas de vecindad: respetar el descanso, no botar basura en zonas comunes.',
    'Profesiones y oficios: médicos, bomberos, policías, profesores, agricultores, tenderos, recolectores de basura. Función social de cada profesión. Herramientas que usan.',
    'Estructura de autoridad básica: máxima autoridad en la casa (padres), en el colegio (rector/director) y en la ciudad (alcalde). Por qué son necesarias las autoridades.',
    'Los derechos de los niños: derecho a la vida, al nombre/identidad, a estudiar, a jugar y a la salud. La Convención de los Derechos del Niño básica.',
    'Los deberes de los niños: respetar a los mayores, estudiar, cuidar sus cosas y el entorno. Relación entre derechos y deberes: para tener derechos hay que cumplir deberes.',
    'Normas de convivencia: pedir la palabra, escuchar al otro, usar palabras amables (por favor, gracias, disculpa). Manual de convivencia en el colegio y espacios virtuales.',
    'Resolución pacífica de conflictos: el diálogo como herramienta principal. Pasos para resolver un problema sin agresión: escuchar, hablar, llegar a un acuerdo.',
    'Educación vial: el semáforo (rojo=pare, amarillo=precaución, verde=siga) para peatones y conductores. La cebra peatonal. Comportamiento seguro al transitar por la vía pública.',
    'Cuidado del medio ambiente: ahorro del agua, apagar luces innecesarias, clasificación de residuos (reciclaje básico: papel, plástico, vidrio, orgánico). Por qué debemos cuidar el planeta.',
    'Medios de transporte: terrestres (carro, bus, bicicleta, tren), acuáticos (barco, canoa) y aéreos (avión, helicóptero). Evolución histórica del transporte.',
    'Medios de comunicación: teléfono, televisión, radio, periódico, internet. Cómo han cambiado en el tiempo. Uso responsable de las tecnologías.',
    'La vivienda: tipos de casas (casa, apartamento, cabaña, choza). Partes del hogar y su función. Materiales de construcción: ladrillo, madera, cemento, paja.',
    'Repaso integral: pensamiento histórico, espacial, organización social y formación ciudadana. Preguntas mixtas de análisis y aplicación. Nivel grado 2 transición a grado 3.',
  ],
};

const NOMBRES_MATERIA = {
  MAT: 'Matemáticas',
  LCA: 'Lengua Castellana',
  ING: 'Inglés',
  NAT: 'Ciencias Naturales',
  SOC: 'Ciencias Sociales',
};

// ── Materias que REQUIEREN un texto/situación base antes de las preguntas ──
// Para estas materias, el prompt le pide a la IA que genere el texto primero
// y que CADA pregunta incluya ese texto en el campo "contexto".
const MATERIAS_CON_TEXTO_BASE = {
  // LCA lecciones de comprensión lectora (1, 2, 3, 15, 18): necesitan cuento/fábula
  LCA: {
    leccionesConTexto: [1, 2, 3, 15, 18],
    tipoTexto: (leccion) => {
      if (leccion === 15) return 'cuento corto de 3 párrafos con inicio, nudo y desenlace claros';
      if (leccion === 18) return 'texto informativo corto (3 párrafos) sobre un tema de ciencias o naturaleza';
      if (leccion === 2)  return 'fábula corta con moraleja al final';
      if (leccion === 3)  return 'fábula corta con moraleja al final';
      return 'cuento corto de 3 párrafos con personajes, lugar y eventos en orden';
    },
    instruccionesExtra: (leccion) => {
      if (leccion <= 3 || leccion === 15 || leccion === 18) {
        return `
IMPORTANTE para esta lección:
- PRIMERO genera un "${MATERIAS_CON_TEXTO_BASE.LCA.tipoTexto(leccion)}" apropiado para niños de 7-8 años
- El cuento/texto debe tener entre 120 y 180 palabras, lenguaje simple y una trama clara
- TODAS las preguntas deben referirse EXCLUSIVAMENTE a ese texto que generaste
- El campo "contexto" de CADA pregunta debe contener el texto completo tal cual lo generaste
- Las preguntas deben evaluar comprensión lectora real: personajes, eventos, inferencias, secuencia`;
      }
      return '';
    },
  },
};

function necesitaTextoBase(mat, leccion) {
  const config = MATERIAS_CON_TEXTO_BASE[mat];
  if (!config) return false;
  return config.leccionesConTexto.includes(leccion);
}

function getAuth() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  return new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
}

function callOpenAI(prompt) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      model: 'gpt-4o-mini',
      max_tokens: 4000,
      temperature: 0.7,
      messages: [{ role: 'user', content: prompt }],
    });
    const options = {
      hostname: 'api.openai.com',
      path: '/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
        'Content-Length': Buffer.byteLength(body),
      },
    };
    const req = https.request(options, (r) => {
      let data = '';
      r.on('data', chunk => data += chunk);
      r.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          resolve(parsed.choices?.[0]?.message?.content || '');
        } catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function sheetExiste(sheets, nombre) {
  const meta = await sheets.spreadsheets.get({ spreadsheetId: SHEET_ID });
  return meta.data.sheets.some(s => s.properties.title === nombre);
}

async function crearHoja(sheets, nombre) {
  await sheets.spreadsheets.batchUpdate({
    spreadsheetId: SHEET_ID,
    requestBody: { requests: [{ addSheet: { properties: { title: nombre } } }] },
  });
}

// ── Construir el prompt según la materia y la lección ────────────────
function buildPrompt(grado, mat, leccion, tema) {
  const conTexto = necesitaTextoBase(mat, leccion);
  const config = MATERIAS_CON_TEXTO_BASE[mat];
  const instrExtra = conTexto && config ? config.instruccionesExtra(leccion) : '';

  // Sección extra del JSON si hay contexto
  const campoContexto = conTexto
    ? `\n      "contexto": "TEXTO COMPLETO del cuento/texto aquí (el MISMO en todas las preguntas)",`
    : '';

  const instrContexto = conTexto
    ? `
⚠️ REGLA CRÍTICA PARA ESTA LECCIÓN:
Esta es una lección de COMPRENSIÓN LECTORA. Debes:
1. Inventar UN SOLO texto narrativo/informativo de 120-180 palabras, apropiado para niños de 7-8 años
2. Escribir ese texto completo en el campo "contexto" de CADA pregunta (siempre el mismo texto)
3. Que TODAS las preguntas sean sobre ese texto específico, no sobre temas generales
4. El texto debe incluir: nombres de personajes, lugar, acciones claras y orden de eventos
${instrExtra}`
    : '';

  return `Eres un profesor experto creando preguntas de examen para un niño de 7 años (grado ${grado} Colombia).

TEMA: ${tema}
MATERIA: ${NOMBRES_MATERIA[mat] || mat}
${instrContexto}

Genera EXACTAMENTE 15 preguntas de selección múltiple. Reglas OBLIGATORIAS:
1. Lenguaje claro y simple para niño de 7-8 años, pero las preguntas deben evaluar COMPRENSIÓN REAL
2. 4 opciones (A, B, C, D), UNA sola correcta
3. Dificultad progresiva: preguntas 1-5 reconocimiento básico, 6-10 aplicación directa, 11-15 razonamiento
4. Sin LaTeX ni símbolos matemáticos especiales. Usar texto plano: 3/4, raiz(16), 2x3
5. Distractores CREÍBLES: errores típicos que cometen los niños
6. Incluir al menos 2 preguntas con situaciones de la vida real
7. Respuestas distribuidas: A×4, B×4, C×4, D×3 sin patrón visible
8. Devuelve ÚNICAMENTE JSON válido, sin texto adicional, sin bloques de código markdown

Formato JSON exacto:
{
  "preguntas": [
    {
      "pregunta": "texto de la pregunta",${campoContexto}
      "opciones": { "A": "opción a", "B": "opción b", "C": "opción c", "D": "opción d" },
      "respuesta": "B",
      "explicacion": "explicación breve en 2 oraciones para el niño de 7 años"
    }
  ]
}`;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'Método no permitido' });

  const { grado, materia, leccion } = req.body;
  if (!grado || !materia || !leccion) {
    return res.status(400).json({ ok: false, error: 'Faltan grado, materia o leccion' });
  }

  const mat = materia.toUpperCase();
  const lNum = parseInt(leccion);
  const lStr = String(lNum).padStart(2, '0');
  const sheetName = `G${grado}_${mat}_L${lStr}`;
  const tema = CURRICULO[mat]?.[lNum - 1];

  if (!tema) {
    return res.status(400).json({ ok: false, error: `No hay tema definido para ${mat} lección ${lNum}` });
  }

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    // Verificar si la hoja ya existe y tiene contenido
    const existe = await sheetExiste(sheets, sheetName);
    if (existe) {
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: `${sheetName}!A2:I20`,
        valueRenderOption: 'UNFORMATTED_VALUE',
      });
      if ((r.data.values || []).length > 0) {
        return res.json({ ok: true, sheetName, generado: false, mensaje: 'Ya existía' });
      }
    }

    // Construir prompt según materia y lección
    const prompt = buildPrompt(grado, mat, lNum, tema);

    // Llamar a OpenAI
    const raw = await callOpenAI(prompt);
    let parsed;
    try {
      const clean = raw.replace(/```json|```/g, '').trim();
      parsed = JSON.parse(clean);
    } catch (e) {
      return res.status(500).json({ ok: false, error: 'OpenAI devolvió JSON inválido', raw });
    }

    const preguntas = parsed.preguntas || [];
    if (preguntas.length < 10) {
      return res.status(500).json({ ok: false, error: `Solo ${preguntas.length} preguntas generadas`, raw });
    }

    // ── Para lecciones con texto base: anteponer el contexto al enunciado ──
    // El campo "contexto" se inyecta al inicio de la pregunta con un separador visual
    // que el frontend mostrará como bloque destacado.
    // Formato: "📖 TEXTO:\n{contexto}\n\n❓ PREGUNTA:\n{pregunta}"
    // Si el frontend ya soporta el campo "contexto" puedes manejarlo allá,
    // pero embebido en la pregunta es compatible con el Sheet tal como está.
    const conTexto = necesitaTextoBase(mat, lNum);

    const rows = preguntas.map(p => {
      let enunciado = p.pregunta || '';

      if (conTexto && p.contexto) {
        // Embeber el texto del cuento en el enunciado para que el Sheet lo almacene
        // El frontend detecta el separador "📖" y lo muestra en un bloque especial
        enunciado = `📖 ${p.contexto}\n\n❓ ${p.pregunta}`;
      }

      return [
        enunciado,
        p.opciones?.A || '',
        p.opciones?.B || '',
        p.opciones?.C || '',
        p.opciones?.D || '',
        (p.respuesta || 'A').toUpperCase(),
        '',              // G: imagen
        '',              // H: video
        p.explicacion || '',  // I: explicación popup
      ];
    });

    // Crear hoja si no existía
    if (!existe) await crearHoja(sheets, sheetName);

    // Escribir en el Sheet
    await sheets.spreadsheets.values.update({
      spreadsheetId: SHEET_ID,
      range: `${sheetName}!A2:I${rows.length + 1}`,
      valueInputOption: 'RAW',
      requestBody: { values: rows },
    });

    return res.json({
      ok: true,
      sheetName,
      generado: true,
      total: preguntas.length,
      tema,
      conTextoBase: conTexto,
    });

  } catch (e) {
    console.error('Error generar-leccion:', e);
    return res.status(500).json({ ok: false, error: e.message });
  }
};
