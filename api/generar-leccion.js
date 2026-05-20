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
    'Estructura de la oración: sujeto (quién realiza la acción) y predicado (lo que se dice del sujeto). Núcleo del sujeto (sustantivo) y núcleo del predicado (verbo). Identificar oraciones completas e incompletas. Separar sujeto y predicado en oraciones simples.',
    'Conectores lógicos: aditivos (y, también, además), causales (porque, ya que), adversativos (pero, sin embargo), consecutivos (entonces, por eso). Usar conectores para unir oraciones y formar párrafos con coherencia.',
    'Tipologías textuales: cuento y fábula (narrativo — tiene personajes, problema y solución), poesía (tiene rima y ritmo), receta e instrucción (texto instructivo — tiene pasos en orden). Identificar cada tipo por sus características visuales y estructurales.',
    'El sustantivo: propios (nombres de personas, ciudades, apellidos — llevan mayúscula) y comunes (objetos, animales, cosas). Concordancia de género (masculino/femenino) y número (singular/plural). Detectar errores como "los gatas blancos".',
    'El adjetivo calificativo: palabras que describen cualidades del sustantivo (grande, peludo, rápido). Concordancia adjetivo-sustantivo en género y número. Describir personajes y objetos con adjetivos precisos y variados.',
    'El verbo: palabras que indican acción o estado. Tiempos verbales: pasado (ayer corrí), presente (hoy corro), futuro (mañana correré). Cambiar oraciones de un tiempo a otro. Identificar el verbo en una oración.',
    'Artículos definidos (el, la, los, las) e indefinidos (un, una, unos, unas). Pronombres personales: Yo, Tú, Él, Ella, Nosotros, Ellos. Sustituir sustantivos por pronombres correctamente en oraciones.',
    'Sinónimos: palabras con significado similar (feliz/contento, rápido/veloz). Antónimos: palabras de significado opuesto (alto/bajo, frío/caliente). Ampliar vocabulario y usar sinónimos y antónimos en oraciones propias.',
    'Segmentación silábica: dividir palabras en sílabas (ca-mi-sa, ma-ri-po-sa). Contar sílabas de una palabra. Sílaba tónica: la que suena más fuerte. Base para reconocer palabras agudas, graves y esdrújulas.',
    'Uso de mayúsculas: al iniciar oración, después de punto, en nombres propios. Signos de puntuación: punto seguido (separa ideas en un párrafo), punto aparte, punto final. Signos de interrogación ¿? y exclamación ¡! con su entonación.',
    'Regla de la M antes de B y P: tambor, campo, sombra,impresora. Sílabas trabadas con l y r: bl, br, cl, cr, fl, fr, pl, pr, gl, gr, tr, dr. Escritura correcta de palabras con estas combinaciones.',
    'Diferenciación ortográfica: b/v (barco/vaca), c/s/z (casa/silla/zapato), h muda (huevo, hijo), ge-gi vs je-ji (gente/jinete), ll vs y (llave/yoyo). Palabras cotidianas con cada caso.',
    'Lenguaje iconográfico: interpretar imágenes, pictogramas y señales de tránsito sencillas. Leer una historia narrada en viñetas o cómics sin texto y explicar qué sucede. Relacionar imagen con mensaje.',
    'Producción textual: ordenar oraciones desordenadas para formar un párrafo con sentido. Identificar la idea principal de un párrafo. Completar textos con las palabras correctas.',
    'Repaso: sujeto y predicado, conectores y tipologías textuales. Preguntas mixtas aplicando los temas de las lecciones 1 a 3.',
    'Repaso: sustantivos, adjetivos, verbos, artículos y pronombres. Preguntas mixtas de gramática aplicada a oraciones y textos cortos.',
    'Repaso: sinónimos, antónimos, silabas y acentuación intuitiva. Preguntas mixtas de vocabulario y fonética.',
    'Repaso: ortografía completa. Mayúsculas, puntuación, M antes de B y P, sílabas trabadas y diferenciación b/v/c/s/z/h. Detectar y corregir errores en textos.',
    'Repaso: lenguaje iconográfico y producción textual. Leer imágenes, ordenar párrafos y completar textos.',
    'Evaluación integral LCA: gramática, ortografía, producción textual y tipologías textuales. Preguntas mixtas nivel grado 2 transición a grado 3.',
  ],
  ING: [
    'INGLÉS — Saludos y despedidas. Vocabulario: Hello, Hi, Good morning, Good afternoon, Good evening, Goodbye, Bye, See you. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: traducción de saludo (¿Cómo se dice Buenos días?), completar la frase (Good ___, how are you?), elegir el saludo correcto según la hora del día, traducir despedidas.',
    'INGLÉS — Presentarse. Frases clave: What is your name? My name is... How are you? I am fine / I am good / I am happy. Nice to meet you. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: completar diálogos (What is your ___? My ___ is Jero.), traducir frases de presentación, elegir la respuesta correcta a How are you?',
    'INGLÉS — Útiles escolares. Vocabulario: pencil, pen, book, notebook, eraser, ruler, sharpener, backpack, desk, chair. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice lápiz en inglés?, completar I have a ___ (pencil/book/eraser), traducir listas de útiles.',
    'INGLÉS — El salón de clase. Vocabulario: classroom, teacher, student, board, door, window, table. Comandos: Open your book, Close the door, Listen, Look, Sit down, Stand up. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: traducir comandos, completar The ___ writes on the board, identificar qué significa cada comando.',
    'INGLÉS — Familia básica. Vocabulario: mother, father, brother, sister, baby, family. Frase clave: This is my mother / father / brother / sister. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice mamá en inglés?, completar This is my ___, traducir oraciones sobre la familia.',
    'INGLÉS — Familia extendida. Vocabulario: grandmother, grandfather, uncle, aunt, cousin, parents, grandparents. Frases: She is my grandmother. He is my uncle. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: traducir miembros de la familia, completar He is my ___, ¿cómo se dice abuela?',
    'INGLÉS — Describir la familia con adjetivos. Vocabulario: tall, short, big, small, old, young, funny, kind, happy. Frases: My mother is tall. My brother is funny. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: completar My father is ___ con adjetivo en inglés, traducir descripciones, elegir el opuesto (tall → ___)',
    'INGLÉS — Verbo To Be con personas. Formas: I am, You are, He is, She is. Frases: She is my sister. He is my father. I am happy. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: completar con la forma correcta (My sister ___ tall), traducir oraciones, elegir I am / He is / She is, corregir errores (My mother are kind).',
    'INGLÉS — Repaso: saludos, presentación, útiles, salón de clase y familia completa. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: traducción directa español→inglés, completar diálogos cortos, identificar el intruso en grupo de palabras, corregir errores.',
    'INGLÉS — Colores. Vocabulario: red, blue, green, yellow, orange, purple, pink, black, white, brown. Frases: The apple is red. The sky is blue. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿De qué color es...? (en inglés), completar The banana is ___, traducir colores, elegir el color correcto.',
    'INGLÉS — Números del 1 al 20. Vocabulario: one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice el número 7?, escribir en inglés el número indicado, completar la secuencia (one, two, ___, four).',
    'INGLÉS — Animales. Vocabulario: dog, cat, bird, fish, rabbit, horse, cow, lion, elephant, monkey. Frases: It is a dog. The cat is small. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice perro?, completar It is a ___, traducir oraciones con animales.',
    'INGLÉS — Comida y bebida. Vocabulario: apple, banana, orange, bread, milk, water, juice, egg, rice, chicken. Frases: I eat an apple. I drink milk. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice manzana?, completar I eat ___ / I drink ___, traducir oraciones de comida.',
    'INGLÉS — Partes del cuerpo. Vocabulario: head, eyes, ears, nose, mouth, hands, arms, legs, feet, hair. Frases: I have two eyes. My nose is small. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice nariz?, completar I have two ___, traducir partes del cuerpo.',
    'INGLÉS — Repaso integral: colores, números 1-20, animales, comida, partes del cuerpo y familia. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: traducción directa, completar oraciones, identificar el intruso, corregir errores, diálogos cortos.',
    'INGLÉS — Verbos de acción. Vocabulario: run, jump, eat, sleep, play, read, write, draw, swim, walk. Frases: I play. She runs. He sleeps. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice correr?, completar I ___ every day, traducir oraciones con verbos.',
    'INGLÉS — La casa. Vocabulario: house, bedroom, bathroom, kitchen, living room, garden, door, window. Frases: I sleep in the bedroom. We eat in the kitchen. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Cómo se dice cocina?, completar I sleep in the ___, traducir oraciones.',
    'INGLÉS — Ropa y clima. Vocabulario: shirt, pants, shoes, jacket, hat, dress. Clima: sunny, rainy, cold, hot. Frase: It is cold. I wear a jacket. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: ¿Qué ropa usas cuando hace frío?, completar It is ___ I wear a ___, traducir prendas.',
    'INGLÉS — Preguntas básicas. What is this? What color is it? How many? Is it a dog? Yes it is / No it is not. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Tipos de pregunta: completar preguntas, elegir la respuesta correcta, traducir preguntas y respuestas cortas.',
    'INGLÉS — Evaluación integral A1.1: saludos, familia, colores, números, animales, comida, cuerpo, verbos, casa. INSTRUCCIONES EN ESPAÑOL, RESPUESTAS EN INGLÉS. Traducción, completar, corregir errores y diálogos cortos.',
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
// LCA ya no tiene lecciones de comprensión lectora — eso quedó en los Cuentos
const MATERIAS_CON_TEXTO_BASE = {};

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
// Obtener temas de lecciones anteriores para el repaso (máx 3 temas)
function temasRepaso(mat, leccionActual) {
  const curriculum = CURRICULO[mat] || [];
  const anteriores = curriculum.slice(0, leccionActual - 1);
  if (!anteriores.length) return [];
  // Tomar hasta 3 lecciones anteriores de forma aleatoria
  const mezclados = anteriores.sort(() => Math.random() - 0.5);
  return mezclados.slice(0, Math.min(3, mezclados.length));
}

function buildPrompt(grado, mat, leccion, tema) {
  const conTexto = necesitaTextoBase(mat, leccion);
  const config = MATERIAS_CON_TEXTO_BASE[mat];
  const instrExtra = conTexto && config ? config.instruccionesExtra(leccion) : '';

  // Sistema Duolingo: repaso solo si hay lecciones anteriores
  const temasAnteriores = leccion > 1 ? temasRepaso(mat, leccion) : [];
  const hayRepaso = temasAnteriores.length > 0;

  const bloqueRepaso = hayRepaso ? `
BLOQUE DE REPASO (preguntas 11 a 15):
Las últimas 5 preguntas deben repasar temas ya vistos en lecciones anteriores.
Distribuye las 5 preguntas entre estos temas anteriores:
${temasAnteriores.map((t, i) => `- Tema anterior ${i + 1}: ${t.substring(0, 120)}...`).join('\n')}
Estas preguntas deben ser más cortas y directas que las del tema nuevo.` : '';

  const estructuraPreguntas = hayRepaso
    ? `ESTRUCTURA OBLIGATORIA de las 15 preguntas:
- Preguntas 1 a 5: TEMA NUEVO — reconocimiento básico y ejemplos directos
- Preguntas 6 a 10: TEMA NUEVO — aplicación y razonamiento con situaciones reales
- Preguntas 11 a 15: REPASO — temas de lecciones anteriores (más cortas y directas)
${bloqueRepaso}`
    : `ESTRUCTURA de las 15 preguntas:
- Preguntas 1 a 5: reconocimiento básico y ejemplos directos
- Preguntas 6 a 10: aplicación directa con contexto real
- Preguntas 11 a 15: razonamiento y situaciones más elaboradas`;

  const campoContexto = conTexto
    ? `\n      "contexto": "TEXTO COMPLETO del cuento aquí (el MISMO en todas las preguntas del bloque nuevo)",`
    : '';

  const instrContexto = conTexto ? `
⚠️ REGLA CRÍTICA: Esta lección usa COMPRENSIÓN LECTORA.
1. Inventa UN SOLO texto de 120-180 palabras para niños de 7-8 años
2. Pon ese texto completo en el campo "contexto" de las preguntas 1 a 10 (tema nuevo)
3. Las preguntas 11-15 de repaso NO llevan contexto
4. El texto debe tener personajes con nombre, lugar y acciones claras
${instrExtra}` : '';

  const reglasIngles = mat === 'ING' ? `
REGLAS ESPECIALES PARA INGLÉS — CUMPLIMIENTO OBLIGATORIO:
- El niño está en nivel PRINCIPIANTE (equivalente a Duolingo Etapa 2, Sección 1)
- TODAS las preguntas, instrucciones y opciones van en ESPAÑOL
- Solo las palabras/frases EN INGLÉS que el niño debe reconocer o traducir van en inglés
- NUNCA escribas preguntas largas en inglés. Ejemplo correcto: "¿Cómo se dice 'perro' en inglés?"
- Opciones correctas e incorrectas son palabras sueltas en inglés (dog / cat / bird / fish)
- Las explicaciones van 100% en español, simples para un niño de 7 años
- Máximo 6 palabras en inglés por pregunta
- Formato de pregunta ideal: "¿Qué significa [palabra en inglés]?" o "¿Cómo se dice [palabra en español] en inglés?"
` : '';

  return `Eres un profesor experto creando preguntas de examen para un niño de 7 años (grado ${grado} Colombia).

TEMA NUEVO DE ESTA LECCIÓN: ${tema}
MATERIA: ${NOMBRES_MATERIA[mat] || mat}
${instrContexto}
${reglasIngles}
${estructuraPreguntas}

REGLAS OBLIGATORIAS para todas las preguntas:
1. Lenguaje claro y simple para niño de 7-8 años
2. 4 opciones (A, B, C, D), UNA sola correcta
3. Sin LaTeX ni símbolos especiales. Usar texto plano: 3/4, raiz(16), 2x3
4. Distractores CREÍBLES: errores típicos que cometen los niños
5. Respuestas distribuidas: A×4, B×4, C×4, D×3 sin patrón visible
6. Devuelve ÚNICAMENTE JSON válido, sin texto adicional ni bloques markdown

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
