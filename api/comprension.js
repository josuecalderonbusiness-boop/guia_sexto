const { google } = require('googleapis');
const https = require('https');

const SHEET_ID = process.env.SHEET_ID;

// ── Configuración por nivel ─────────────────────────────────────────────
const PROMPTS = {
  1: `Eres un experto en pedagogía. Genera un texto de comprensión lectora ORIGINAL para evaluación.

TEXTO:
- Tipo: informativo o narrativo
- Para: estudiantes de GRADO 6 (11-12 años) — nivel 6to, NO primaria
- Extensión: entre 250 y 350 palabras
- Temas posibles: animales curiosos, inventos históricos, tradiciones colombianas, fenómenos naturales, deportes, alimentación, curiosidades científicas, personajes históricos relevantes
- Estilo: oraciones claras, vocabulario propio de 6to grado, párrafos de 3-5 líneas
- Debe incluir datos específicos, cifras o hechos concretos que el lector deba retener

PREGUNTAS (exactamente 10 de selección múltiple):
- Tipo: comprensión literal (¿qué dice el texto?) e inferencial básica (¿qué significa?, ¿para qué?)
- 4 opciones por pregunta (A, B, C, D), una sola correcta
- Opciones incorrectas plausibles (no obviamente falsas)
- Distribución de respuestas: sin patrón visible (no ABCDABCD, mezcla aleatoria)
- Cada pregunta incluye explicación pedagógica breve de por qué esa es la correcta`,

  2: `Eres un experto en pedagogía. Genera un texto de comprensión lectora ORIGINAL de nivel intermedio.

TEXTO:
- Tipo: expositivo o informativo de nivel medio-alto
- Para: estudiantes de 6to grado con buena capacidad lectora
- Extensión: entre 450 y 600 palabras
- Temas: historia mundial, biología, anatomía humana, geografía, datos científicos fascinantes, descubrimientos importantes, civilizaciones antiguas, el cuerpo humano, el universo
- Estilo: vocabulario técnico con contexto claro, párrafos de desarrollo, datos concretos y cifras, estructura introducción-desarrollo-conclusión
- Debe incluir números, fechas o estadísticas específicas para retener

PREGUNTAS (exactamente 10 de selección múltiple):
- Tipo: comprensión literal, inferencial, identificación de idea principal, vocabulario en contexto, 1-2 de valoración
- 4 opciones (A, B, C, D), una sola correcta, opciones plausibles
- Sin patrón en distribución de respuestas
- Cada pregunta incluye explicación pedagógica breve`,

  3: `Eres un experto en pedagogía. Genera un texto de comprensión lectora ORIGINAL de alta complejidad.

TEXTO:
- Tipo: científico profundo, filosófico o argumentativo
- Para: estudiantes avanzados de 6to grado, alta capacidad lectora
- Extensión: entre 650 y 800 palabras
- Temas: filosofía del conocimiento, teorías científicas (relatividad, evolución, mecánica cuántica básica), inteligencia artificial y ética, dilemas morales, pensamiento crítico, paradojas lógicas, cosmología, la conciencia humana
- Estilo: vocabulario avanzado, argumentación estructurada, ideas abstractas con ejemplos concretos, requiere concentración sostenida
- Debe invitar a la reflexión y al análisis crítico

PREGUNTAS (exactamente 10 de selección múltiple):
- Tipo: análisis crítico, inferencia profunda, identificación de argumentos, valoración del punto de vista del autor, reflexión
- 4 opciones (A, B, C, D), opciones muy plausibles que requieren haber leído bien
- Alta dificultad, sin patrón en respuestas
- Cada pregunta incluye explicación pedagógica profunda`,
};

const JSON_INSTRUCCION = `

Responde ÚNICAMENTE con JSON puro — sin markdown, sin bloques de código, solo el JSON:
{
  "titulo": "Título del texto",
  "texto": "El texto completo. Separa los párrafos con \\n\\n",
  "preguntas": [
    {
      "pregunta": "¿Pregunta aquí?",
      "opciones": ["opción A", "opción B", "opción C", "opción D"],
      "respuesta": 1,
      "explicacion": "Explicación pedagógica de por qué esa respuesta es correcta..."
    }
  ]
}

IMPORTANTE: "opciones" es un array de 4 strings. "respuesta" es el índice numérico (0=primera, 1=segunda, 2=tercera, 3=cuarta).`;

// ── Helpers ─────────────────────────────────────────────────────────────
function getSheets() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  const auth = new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
  return google.sheets({ version: 'v4', auth });
}

function callOpenAI(prompt) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      model: 'gpt-4o-mini',
      max_tokens: 4000,
      temperature: 0.85,
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

async function crearHojaConEncabezados(sheets, nombre) {
  await sheets.spreadsheets.batchUpdate({
    spreadsheetId: SHEET_ID,
    requestBody: { requests: [{ addSheet: { properties: { title: nombre } } }] },
  });
  await sheets.spreadsheets.values.update({
    spreadsheetId: SHEET_ID,
    range: `${nombre}!A1:E1`,
    valueInputOption: 'RAW',
    requestBody: { values: [['ID', 'Titulo', 'Texto', 'Preguntas_JSON', 'Fecha']] },
  });
}

// ── Handler principal ────────────────────────────────────────────────────
module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  const sheets = getSheets();
  const nivelNum = parseInt(req.method === 'GET' ? req.query.nivel : (req.body || {}).nivel) || 1;
  const hoja = `Comprension_N${nivelNum}`;

  if (![1, 2, 3].includes(nivelNum))
    return res.status(400).json({ ok: false, error: 'Nivel inválido (1, 2 o 3)' });

  // ── GET: siguiente texto no hecho por el alumno ──────────────────────
  if (req.method === 'GET') {
    const nombre = req.query.nombre || '';
    try {
      const existe = await sheetExiste(sheets, hoja);
      if (!existe) return res.json({ ok: true, generar: true, total_banco: 0, hechos: 0 });

      const bancoRes = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: `${hoja}!A2:E1000`,
      });
      const banco = (bancoRes.data.values || []).filter(r => r && r[0]);
      if (!banco.length) return res.json({ ok: true, generar: true, total_banco: 0, hechos: 0 });

      const resRes = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: 'Resultados!A:B',
      });
      const resultados = resRes.data.values || [];
      const prefijo = `Comprension_N${nivelNum}_`;
      const hechoSet = new Set(
        resultados
          .filter(r => r[0] === nombre && String(r[1]).startsWith(prefijo))
          .map(r => String(r[1]).replace(prefijo, ''))
      );

      const siguiente = banco.find(row => !hechoSet.has(row[0]));
      if (siguiente) {
        let preguntas = [];
        try { preguntas = JSON.parse(siguiente[3]); } catch (e) {}
        return res.json({
          ok: true,
          id: siguiente[0],
          titulo: siguiente[1],
          texto: siguiente[2],
          preguntas,
          es_nuevo: false,
          total_banco: banco.length,
          hechos: hechoSet.size,
        });
      }

      return res.json({ ok: true, generar: true, total_banco: banco.length, hechos: hechoSet.size });

    } catch (e) {
      console.error('comprension GET error:', e);
      return res.status(500).json({ ok: false, error: e.message });
    }
  }

  // ── POST: generar texto nuevo con IA y guardarlo en Sheets ───────────
  if (req.method === 'POST') {
    try {
      const raw = await callOpenAI(PROMPTS[nivelNum] + JSON_INSTRUCCION);
      let data;
      try {
        const clean = raw.replace(/```json\n?|```\n?/g, '').trim();
        data = JSON.parse(clean);
      } catch (e) {
        return res.status(500).json({ ok: false, error: 'OpenAI devolvió JSON inválido', raw });
      }

      if (!data.titulo || !data.texto || !Array.isArray(data.preguntas) || data.preguntas.length < 8) {
        return res.status(500).json({ ok: false, error: `Respuesta incompleta: ${data.preguntas?.length || 0} preguntas generadas` });
      }

      const existe = await sheetExiste(sheets, hoja);
      if (!existe) await crearHojaConEncabezados(sheets, hoja);

      const id = 'T' + Date.now();

      await sheets.spreadsheets.values.append({
        spreadsheetId: SHEET_ID,
        range: `${hoja}!A:E`,
        valueInputOption: 'RAW',
        requestBody: {
          values: [[
            id,
            data.titulo,
            data.texto,
            JSON.stringify(data.preguntas),
            new Date().toLocaleString('es-CO'),
          ]],
        },
      });

      return res.json({
        ok: true,
        id,
        titulo: data.titulo,
        texto: data.texto,
        preguntas: data.preguntas,
        es_nuevo: true,
      });

    } catch (e) {
      console.error('comprension POST error:', e);
      return res.status(500).json({ ok: false, error: e.message });
    }
  }

  return res.status(405).json({ ok: false, error: 'Method not allowed' });
};
