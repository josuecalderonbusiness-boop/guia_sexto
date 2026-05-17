import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'api', 'generar-leccion.js')

CONTENIDO = r'''const { google } = require('googleapis');
const https = require('https');

const SHEET_ID = process.env.SHEET_ID;

// ── Currículo completo de Jero (grado 2) ────────────────────────────
const CURRICULO = {
  MAT: [
    'Números del 1 al 100: lectura, escritura y valor posicional (unidades y decenas)',
    'Sumas sin llevar hasta 100',
    'Sumas con llevadas hasta 100',
    'Restas sin prestar hasta 100',
    'Restas con préstamo hasta 100',
    'Problemas de suma y resta de un paso con enunciado verbal',
    'Secuencias numéricas: contar de 2 en 2, de 5 en 5 y de 10 en 10',
    'Comparación de números: mayor que, menor que e igual a',
    'Introducción a la multiplicación: el doble y el triple',
    'Tablas del 2, 3, 4 y 5',
    'Reparto en partes iguales: concepto de división intuitiva',
    'Figuras geométricas planas: círculo, triángulo, cuadrado y rectángulo',
    'Cuerpos geométricos: cubo, esfera, cilindro y cono',
    'Medición de longitud: centímetros y metros con regla',
    'El reloj: horas en punto y medias horas',
    'El calendario: días, semanas y meses',
    'Gráficas de barras sencillas: leer e interpretar datos',
    'Problemas de dos pasos con suma y resta combinadas',
    'Números ordinales del primero al décimo',
    'Repaso general y problemas mixtos nivel grado 2',
  ],
  LCA: [
    'Lectura de sílabas simples y palabras cortas (2 a 3 sílabas)',
    'Sílabas trabadas: bl, br, cl, cr, fl, fr, pl, pr, gl, gr, tr, dr',
    'Sustantivos propios y comunes: identificación y uso de mayúscula',
    'El artículo: el, la, los, las, un, una, unos, unas',
    'Género y número de sustantivos y adjetivos: concordancia básica',
    'El verbo: identificar la acción en una oración. Pasado, presente y futuro',
    'Construcción de oraciones con sujeto y predicado',
    'Los signos de puntuación: punto, coma, signos de interrogación y exclamación',
    'Uso de mayúscula al iniciar oración y en nombres propios',
    'Sinónimos y antónimos: vocabulario básico',
    'Comprensión lectora literal: personajes, lugar y secuencia de eventos',
    'Comprensión lectora inferencial: deducir sentimientos y enseñanzas de fábulas',
    'Tipos de texto: cuento, poema y receta. Diferencias básicas',
    'Partes del cuento: inicio, nudo y desenlace',
    'Conectores lógicos básicos: y, pero, porque, entonces',
    'La oración: identificar si está completa o le falta algo',
    'Uso de la M antes de B y P: regla ortográfica',
    'Diferenciación b/v, c/s/z en palabras cotidianas',
    'Lectura de un texto corto y respuesta a preguntas de selección múltiple',
    'Producción escrita: ordenar oraciones para formar un párrafo con sentido',
  ],
  ING: [
    'Greetings and farewells: Hello, Good morning, Good afternoon, Goodbye, How are you?',
    'Numbers 1 to 20: reading and writing in English',
    'Numbers 21 to 50: reading and counting',
    'Colors: red, blue, green, yellow, orange, purple, black, white, pink, brown',
    'School objects: pencil, pen, eraser, ruler, book, notebook, backpack, desk, chair',
    'Family members: mother, father, brother, sister, grandmother, grandfather',
    'Animals: dog, cat, fish, bird, rabbit, cow, horse, pig, lion, elephant',
    'The verb To Be: I am, You are, He/She/It is — affirmative and negative',
    'Classroom commands: Open, Close, Listen, Look, Draw, Circle, Write',
    'Parts of the body: head, eyes, ears, nose, mouth, hands, feet',
    'Fruits and food: apple, banana, orange, mango, rice, bread, milk, water',
    'Clothes: T-shirt, pants, shoes, jacket, hat, skirt, socks',
    'Weather: sunny, rainy, cloudy, windy, hot, cold',
    'Likes and dislikes: I like... / I do not like...',
    'This is / That is: demonstrative pronouns',
    'There is / There are: existence of one or many things',
    'Shapes and sizes: circle, square, triangle, rectangle, big, small, tall, short',
    'My house: bedroom, bathroom, kitchen, living room, garden',
    'Possessive adjectives: my, your, his, her',
    'Simple questions: What is your name? How old are you? What color is...?',
  ],
  NAT: [
    'Seres vivos e inertes: características que diferencian a los seres vivos de los objetos',
    'Las plantas: partes (raíz, tallo, hojas, flor, fruto) y sus funciones',
    'Necesidades de las plantas: agua, luz solar, aire y nutrientes del suelo',
    'Los animales según su alimentación: herbívoros, carnívoros y omnívoros',
    'Los animales según su hábitat: terrestres, acuáticos y aéreos',
    'Ciclo de vida de la mariposa: huevo, oruga, crisálida y mariposa adulta',
    'Los cinco sentidos: órganos y funciones (ojos, oídos, nariz, lengua, piel)',
    'El cuerpo humano: cabeza, tronco y extremidades',
    'Hábitos saludables: alimentación, higiene, ejercicio y sueño',
    'Los estados de la materia: sólido, líquido y gaseoso con ejemplos cotidianos',
    'Cambios de estado: fusión (hielo a agua) y evaporación (agua a vapor)',
    'Fuentes de luz: naturales (el Sol) y artificiales (bombillo, linterna)',
    'El día y la noche: relación con la presencia y ausencia del Sol',
    'El clima: días soleados, lluviosos, nublados y ventosos',
    'Los recursos naturales: agua, suelo y aire. Cómo cuidarlos',
    'Propiedades de los objetos: textura, peso y flexibilidad',
    'Objetos transparentes, translúcidos y opacos',
    'El sonido: vibración, ruidos fuertes y suaves, fuentes de sonido',
    'La cadena alimenticia básica: productor, consumidor y descomponedor',
    'Repaso general: preguntas integradas de ciencias naturales grado 2',
  ],
  SOC: [
    'La familia: tipos de familia, roles y responsabilidades de cada miembro',
    'Árbol genealógico: parentesco (abuelos, tíos, primos)',
    'El paso del tiempo: pasado, presente y futuro. Antes, ahora y después',
    'Historia personal: cómo he cambiado desde bebé hasta hoy',
    'La vivienda: tipos de casas y partes del hogar',
    'El barrio y la comunidad: lugares representativos (parque, hospital, colegio, tienda)',
    'Normas de convivencia en la familia, el colegio y el barrio',
    'Paisaje rural y paisaje urbano: diferencias y características',
    'Orientación espacial: derecha, izquierda, arriba, abajo, dentro, fuera',
    'Los puntos cardinales: Norte, Sur, Este y Oeste. El Sol como referencia',
    'Lectura de planos sencillos: convenciones y símbolos básicos en un mapa',
    'Las profesiones y oficios: ¿qué hacen y cómo ayudan a la comunidad?',
    'Medios de transporte: terrestres, acuáticos y aéreos. Evolución histórica',
    'Medios de comunicación: teléfono, televisión, internet. Cambios en el tiempo',
    'Los derechos de los niños: derecho a la educación, salud, juego e identidad',
    'Los deberes de los niños: respetar, estudiar, cuidar el entorno',
    'Resolución pacífica de conflictos: el diálogo como herramienta',
    'Símbolos patrios de Colombia: bandera, escudo e himno',
    'Educación vial: semáforo, cebra peatonal y normas de tránsito básicas',
    'Cuidado del medio ambiente: ahorro del agua, reciclaje y no botar basura',
  ],
};

const NOMBRES_MATERIA = {
  MAT: 'Matemáticas',
  LCA: 'Lengua Castellana',
  ING: 'Inglés',
  NAT: 'Ciencias Naturales',
  SOC: 'Ciencias Sociales',
};

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
      max_tokens: 3000,
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

  const prompt = `Eres un profesor experto creando preguntas de examen para un niño de ${grado === 2 ? '7' : '11'} años (grado ${grado} Colombia).

TEMA: ${tema}
MATERIA: ${NOMBRES_MATERIA[mat] || mat}

Genera EXACTAMENTE 15 preguntas de selección múltiple. Reglas OBLIGATORIAS:
1. Lenguaje MUY simple, máximo 20 palabras por pregunta
2. 4 opciones (A, B, C, D), UNA sola correcta
3. Dificultad progresiva: preguntas 1-5 fáciles, 6-10 medias, 11-15 difíciles
4. Sin LaTeX ni símbolos matemáticos especiales. Usar texto plano: 3/4, raiz(16), 2x3
5. Distractores (respuestas incorrectas) creíbles, no absurdos
6. Respuestas distribuidas: aproximadamente A×4, B×4, C×4, D×3 sin patrón visible
7. Devuelve ÚNICAMENTE JSON válido, sin texto adicional, sin bloques de código

Formato JSON exacto:
{
  "preguntas": [
    {
      "pregunta": "texto de la pregunta",
      "opciones": { "A": "opción a", "B": "opción b", "C": "opción c", "D": "opción d" },
      "respuesta": "B",
      "explicacion": "explicación breve en 2 oraciones para el niño"
    }
  ]
}`;

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    // Verificar si la hoja ya existe (ya fue generada antes)
    const existe = await sheetExiste(sheets, sheetName);
    if (existe) {
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: `${sheetName}!A2:H20`,
        valueRenderOption: 'UNFORMATTED_VALUE',
      });
      if ((r.data.values || []).length > 0) {
        return res.json({ ok: true, sheetName, generado: false, mensaje: 'Ya existía' });
      }
    }

    // Generar con OpenAI
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

    // Crear hoja si no existe
    if (!existe) await crearHoja(sheets, sheetName);

    // Escribir preguntas en el Sheet
    const rows = preguntas.map(p => [
      p.pregunta || '',
      p.opciones?.A || '',
      p.opciones?.B || '',
      p.opciones?.C || '',
      p.opciones?.D || '',
      (p.respuesta || 'A').toUpperCase(),
      '',           // imagen (vacío — se puede agregar después)
      p.explicacion || '',
    ]);

    await sheets.spreadsheets.values.update({
      spreadsheetId: SHEET_ID,
      range: `${sheetName}!A2:H${rows.length + 1}`,
      valueInputOption: 'RAW',
      requestBody: { values: rows },
    });

    return res.json({
      ok: true,
      sheetName,
      generado: true,
      total: preguntas.length,
      tema,
    });

  } catch (e) {
    console.error('Error generar-leccion:', e);
    return res.status(500).json({ ok: false, error: e.message });
  }
};
''';

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(CONTENIDO)

print('✅ api/generar-leccion.js creado')
print('   → Currículo completo: 20 lecciones × 5 materias = 100 lecciones')
print('   → Genera preguntas con GPT-4o-mini y las guarda en el Sheet')
print('   → Detecta si ya existe para no regenerar')
