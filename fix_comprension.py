import os

HERE  = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, 'public', 'index.html')

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

ok = 0
T  = 9

def p(num, desc, old, new):
    global html, ok
    if old not in html:
        print(f'P{num}/{T} ❌  {desc}  — ancla no encontrada')
        return
    html = html.replace(old, new, 1)
    ok  += 1
    print(f'P{num}/{T} ✅  {desc}')

# ════════════════════════════════════════════════════════════════════════
# PATCH 1 — CSS
# ════════════════════════════════════════════════════════════════════════
p(1, 'CSS comprensión lectora',
"  .mejora-badge { font-family:'Fredoka One',cursive; font-size:1.3rem; padding:12px 28px; border-radius:50px; display:inline-block; margin:12px 0; }\n</style>",
"""  .mejora-badge { font-family:'Fredoka One',cursive; font-size:1.3rem; padding:12px 28px; border-radius:50px; display:inline-block; margin:12px 0; }
  /* ── COMPRENSIÓN DE LECTURA ─────────────────────────── */
  #screen-comprension,#screen-lect-texto{display:none}
  .lect-header{padding:16px 20px;background:white;border-bottom:3px solid #F0F0F0;
    position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:12px}
  .nivel-card{background:white;border-radius:20px;padding:20px 22px;margin-bottom:14px;
    cursor:pointer;transition:all 0.2s;border:3px solid #E0E0E0;
    box-shadow:0 4px 16px rgba(0,0,0,.07);display:flex;align-items:center;gap:14px}
  .nivel-emoji{font-size:2.4rem;flex-shrink:0}
  .nivel-info{flex:1}
  .nivel-titulo{font-family:'Fredoka One',cursive;font-size:1.15rem}
  .nivel-sub{font-size:.83rem;color:#666;font-weight:600;margin-top:2px}
  .nivel-estrellas{font-size:.9rem;margin-top:6px;min-height:20px}
  .nivel-arrow{font-size:1.4rem;flex-shrink:0}
</style>""")

# ════════════════════════════════════════════════════════════════════════
# PATCH 2 — HTML: 2 nuevas pantallas
# ════════════════════════════════════════════════════════════════════════
HTML_SCREENS = """
<div id="screen-comprension">
  <div style="display:flex;align-items:center;gap:12px;padding:20px 20px 0">
    <button class="btn-volver" onclick="volverInicio()">← Volver</button>
    <h2 style="font-family:'Fredoka One',cursive;font-size:1.4rem">📖 Comprensión de Lectura</h2>
  </div>
  <p style="color:#666;font-size:.88rem;padding:8px 20px 16px;line-height:1.5">
    Lee cada texto con atención y responde las 10 preguntas. ¡Cada texto es único! Acumula ⭐ por nivel.
  </p>
  <div id="comprension-niveles" style="padding:0 20px;max-width:700px;margin:0 auto"></div>
</div>

<div id="screen-lect-texto">
  <div class="lect-header">
    <button class="btn-volver" onclick="mostrar('screen-comprension');renderComprensionMenu()">← Volver</button>
    <span style="font-family:'Fredoka One',cursive;font-size:1.05rem;color:#1A1A2E">📖 Lee con atención</span>
  </div>
  <div id="lect-contenido"></div>
</div>

<div id="screen-examen">"""

p(2, 'HTML screen-comprension + screen-lect-texto',
'\n<div id="screen-examen">',
HTML_SCREENS)

# ════════════════════════════════════════════════════════════════════════
# PATCH 3 — mostrar(): registrar las 2 pantallas nuevas
# ════════════════════════════════════════════════════════════════════════
p(3, "mostrar() — agregar pantallas nuevas",
"'screen-cuentos','screen-lector'",
"'screen-cuentos','screen-lector','screen-comprension','screen-lect-texto'")

# ════════════════════════════════════════════════════════════════════════
# PATCH 4 — Botón naranja en menú de Grado 6
# ════════════════════════════════════════════════════════════════════════
BTN_OLD = ('  <div style="text-align:center;margin-bottom:20px">\n'
           '    <button onclick="verMisResultados()" style="background:linear-gradient(135deg,#1A1A2E,#0F3460);'
           'color:white;border:none;border-radius:16px;padding:12px 28px;font-family:Nunito,sans-serif;'
           'font-weight:800;font-size:1rem;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,0.2)">'
           '📊 Mis Resultados</button>\n  </div>')
BTN_NEW = (
    '  <div style="text-align:center;margin-bottom:20px;display:flex;flex-direction:column;gap:10px;align-items:center">\n'
    '    <button onclick="abrirComprension()" style="background:linear-gradient(135deg,#E65100,#F57C00);'
    'color:white;border:none;border-radius:16px;padding:13px 28px;font-family:Nunito,sans-serif;'
    'font-weight:800;font-size:1rem;cursor:pointer;box-shadow:0 4px 16px rgba(230,81,0,.35);width:264px">'
    '📖 Comprensión de Lectura</button>\n'
    '    <button onclick="verMisResultados()" style="background:linear-gradient(135deg,#1A1A2E,#0F3460);'
    'color:white;border:none;border-radius:16px;padding:12px 28px;font-family:Nunito,sans-serif;'
    'font-weight:800;font-size:1rem;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.2);width:264px">'
    '📊 Mis Resultados</button>\n  </div>'
)
p(4, 'Botón Comprensión en screen-inicio', BTN_OLD, BTN_NEW)

# ════════════════════════════════════════════════════════════════════════
# PATCH 5 — Agregar CL a MATERIAS
# ════════════════════════════════════════════════════════════════════════
p(5, 'MATERIAS — agregar clave CL',
"  LEN: { nombre: 'Lenguaje',    emoji: '📖', clase: 'len-btn', color: '#339AF0', gradiente: 'linear-gradient(135deg,#339AF0,#1971C2)' },\n};",
"""  LEN: { nombre: 'Lenguaje',    emoji: '📖', clase: 'len-btn', color: '#339AF0', gradiente: 'linear-gradient(135deg,#339AF0,#1971C2)' },
  CL:  { nombre: 'Comprensión Lectora', emoji: '📖', clase: 'len-btn', color: '#E65100', gradiente: 'linear-gradient(135deg,#E65100,#F57C00)' },
};""")

# ════════════════════════════════════════════════════════════════════════
# PATCH 6 — JS: todas las funciones del módulo
# ════════════════════════════════════════════════════════════════════════
JS_CL = (
"""
// ── COMPRENSIÓN DE LECTURA ─────────────────────────────────────────────
let comprensionActual = null;

function abrirComprension() {
  mostrar('screen-comprension');
  renderComprensionMenu();
  window.scrollTo(0,0);
}

function renderComprensionMenu() {
  const NIVELES = [
    {n:1,emoji:'🌱',titulo:'Nivel 1 — Básico',
     sub:'Textos informativos y narrativos para 6to grado',
     color:'#37B24D',border:'#51CF66'},
    {n:2,emoji:'📚',titulo:'Nivel 2 — Intermedio',
     sub:'Historia, Ciencias, Biología y datos del mundo',
     color:'#1971C2',border:'#339AF0'},
    {n:3,emoji:'🔥',titulo:'Nivel 3 — Avanzado',
     sub:'Ciencia profunda, Filosofía y pensamiento crítico',
     color:'#6741D9',border:'#845EF7'},
  ];
  const cont = document.getElementById('comprension-niveles');
  cont.innerHTML = NIVELES.map(nv => {
    const hechos = parseInt(localStorage.getItem('cl_n'+nv.n+'_count')||'0');
    const estrellas = hechos > 0
      ? '\u2b50'.repeat(Math.min(hechos,10))+(hechos>10?' <span style="font-size:.8rem;color:#888">+' +(hechos-10)+' m\u00e1s</span>':'')
      : '<span style="color:#ccc;font-size:.85rem">\u2606 Sin intentos a\u00fan</span>';
    return '<div class="nivel-card" style="border-color:'+nv.border+'"'
      +' onclick="iniciarComprension('+nv.n+')"'
      +' onmouseover="this.style.borderColor=\\''+nv.color+'\\';this.style.transform=\\'translateY(-3px)\\';this.style.boxShadow=\\'0 10px 32px rgba(0,0,0,.14)\\'"'
      +' onmouseout="this.style.borderColor=\\''+nv.border+'\\';this.style.transform=\\'none\\';this.style.boxShadow=\\'0 4px 16px rgba(0,0,0,.07)\\'">'
      +'<span class="nivel-emoji">'+nv.emoji+'</span>'
      +'<div class="nivel-info">'
        +'<div class="nivel-titulo" style="color:'+nv.color+'">'+nv.titulo+'</div>'
        +'<div class="nivel-sub">'+nv.sub+'</div>'
        +'<div class="nivel-estrellas">'+estrellas+'</div>'
      +'</div>'
      +'<span class="nivel-arrow" style="color:'+nv.color+'">→</span>'
      +'</div>';
  }).join('');
}

async function iniciarComprension(nivel) {
  mostrar('screen-lect-texto');
  document.getElementById('lect-contenido').innerHTML =
    '<div style="padding:80px 20px;text-align:center"><div class="loading" style="justify-content:center">'
    +'<div class="spinner"></div><span>Buscando tu texto... \ud83d\udcd6</span></div></div>';
  try {
    let res  = await fetch('/api/comprension?nivel='+nivel+'&nombre='+encodeURIComponent(estado.nombre));
    let data = await res.json();
    if (!data.ok) throw new Error(data.error||'Error al buscar texto');
    if (data.generar) {
      document.getElementById('lect-contenido').innerHTML =
        '<div style="padding:80px 20px;text-align:center"><div class="loading" style="justify-content:center">'
        +'<div class="spinner"></div><span>\ud83e\udd16 Generando texto nuevo para ti...</span></div></div>';
      res  = await fetch('/api/comprension',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({nivel})});
      data = await res.json();
    }
    if (!data.ok) throw new Error(data.error||'Error al generar texto');
    comprensionActual = {nivel,id:data.id,titulo:data.titulo,texto:data.texto,preguntas:data.preguntas};
    renderTextoLectura();
  } catch(e) {
    document.getElementById('lect-contenido').innerHTML =
      '<div style="padding:60px 20px;text-align:center">'
      +'<div style="font-size:2.5rem;margin-bottom:12px">⚠️</div>'
      +'<p style="font-weight:700;color:#C92A2A;margin-bottom:20px">'+e.message+'</p>'
      +'<button onclick="iniciarComprension('+nivel+')" style="padding:12px 28px;background:#339AF0;color:white;'
      +'border:none;border-radius:14px;font-family:Nunito,sans-serif;font-weight:800;font-size:1rem;cursor:pointer">'
      +'\ud83d\udd04 Reintentar</button></div>';
  }
}

function renderTextoLectura() {
  const {nivel,titulo,texto} = comprensionActual;
  const COLS  = {1:'#37B24D',2:'#1971C2',3:'#6741D9'};
  const color = COLS[nivel]||'#339AF0';
  const parrafos = texto.split(/\\n\\n+/).filter(function(p){return p.trim();});
  const htmlP = parrafos.map(function(p){
    return '<p style="margin-bottom:18px;line-height:1.95;font-size:1.05rem;color:#1A1A2E;text-indent:1.5em">'+p.trim()+'</p>';
  }).join('');
  document.getElementById('lect-contenido').innerHTML =
    '<div style="max-width:680px;margin:0 auto;padding:24px 20px 60px">'
      +'<div style="text-align:center;margin-bottom:22px">'
        +'<div style="display:inline-block;background:'+color+'1A;border:2px solid '+color+';border-radius:50px;'
        +'padding:5px 18px;font-size:.78rem;font-weight:800;color:'+color+';margin-bottom:10px;'
        +'letter-spacing:.8px;text-transform:uppercase">\ud83d\udcd6 NIVEL '+nivel+'</div>'
        +'<h2 style="font-family:\\'Fredoka One\\',cursive;font-size:1.6rem;color:#1A1A2E;line-height:1.3">'+titulo+'</h2>'
      +'</div>'
      +'<div style="background:white;border-radius:20px;padding:28px 24px;box-shadow:0 4px 24px rgba(0,0,0,.08);'
      +'margin-bottom:20px;border-left:5px solid '+color+'">'
        +htmlP
      +'</div>'
      +'<div style="background:'+color+'0D;border:2px solid '+color+'33;border-radius:14px;padding:14px 18px;margin-bottom:20px;text-align:center">'
        +'<p style="font-size:.88rem;font-weight:700;color:#555;margin:0">'
        +'\ud83d\udca1 Lee con atenci\u00f3n \u2014 las preguntas pondr\u00e1n a prueba lo que recuerdas del texto</p>'
      +'</div>'
      +'<button onclick="comenzarQuizComprension()" onmouseover="this.style.transform=\\'translateY(-2px)\\'" onmouseout="this.style.transform=\\'none\\'"'
      +' style="width:100%;padding:18px;background:linear-gradient(135deg,'+color+','+color+'BB);color:white;border:none;'
      +'border-radius:16px;font-family:Nunito,sans-serif;font-weight:800;font-size:1.1rem;cursor:pointer;'
      +'box-shadow:0 4px 20px '+color+'44;transition:transform .15s">'
      +'\u2705 Ya le\u00ed \u2014 Comenzar las 10 preguntas \u2192</button>'
    +'</div>';
}

function comenzarQuizComprension() {
  const {nivel,id,preguntas} = comprensionActual;
  const GRADS = {
    1:'linear-gradient(135deg,#51CF66,#37B24D)',
    2:'linear-gradient(135deg,#339AF0,#1971C2)',
    3:'linear-gradient(135deg,#845EF7,#6741D9)'
  };
  examenActual = {
    dia:'Comprension_N'+nivel+'_'+id, materia:'CL', preguntas,
    idx:0, respuestas:[], puntaje:0, intentos:0,
    esComprension:true, nivelComprension:nivel,
  };
  document.getElementById('examen-badge').textContent = '\ud83d\udcd6 Nivel '+nivel;
  document.getElementById('examen-badge').style.background    = GRADS[nivel];
  document.getElementById('examen-badge').style.color         = 'white';
  document.getElementById('examen-badge').style.borderRadius  = '50px';
  document.getElementById('examen-badge').style.padding       = '6px 16px';
  document.getElementById('examen-dia-label').textContent     = '\ud83d\udcd6 Comprensión';
  document.getElementById('progress-fill').style.background   = GRADS[nivel];
  mostrar('screen-examen');
  renderPregunta();
}

async function terminarExamen_COMPRENSION_PATCH() {
  if (!examenActual.esComprension) return;
  const {nivelComprension,puntaje,preguntas,respuestas,dia} = examenActual;
  const key = 'cl_n'+nivelComprension+'_count';
  localStorage.setItem(key, String((parseInt(localStorage.getItem(key)||'0'))+1));
  try {
    const ctrl = new AbortController();
    const t = setTimeout(function(){ctrl.abort();}, 8000);
    await fetch('/api/guardar',{
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
        nombre:estado.nombre, dia, materia:'Comprensión Lectora',
        puntaje, total:preguntas.length, respuestas,
        fecha: new Date().toLocaleString('es-CO')
      }),
      signal: ctrl.signal
    });
    clearTimeout(t);
  } catch(e){ console.warn('No se guardó resultado comprensión:',e); }
  setTimeout(function(){
    var b = document.querySelector('#screen-resultado .btn-otra-materia:not(#btn-corrige)');
    if(b) b.textContent = '\ud83d\udcd6 Hacer otro texto';
  }, 80);
  if (puntaje/preguntas.length >= 0.8) sonidoEstrella(); else sonidoCorrecto();
}

""")

p(6, 'JS — funciones comprensión lectora',
'// ── VOLVER ──',
JS_CL + '// ── VOLVER ──')

# ════════════════════════════════════════════════════════════════════════
# PATCH 7 — volverInicio: regresar a pantalla correcta
# ════════════════════════════════════════════════════════════════════════
p(7, 'volverInicio() — soporte comprensión',
'function volverInicio() {\n  if (estado.grado === 2) {',
"""function volverInicio() {
  if (examenActual && examenActual.esComprension) {
    examenActual.esComprension = false;
    mostrar('screen-comprension');
    renderComprensionMenu();
    window.scrollTo(0,0);
    return;
  }
  if (estado.grado === 2) {""")

# ════════════════════════════════════════════════════════════════════════
# PATCH 8 — terminarExamen: llamar hook de comprensión primero
# ════════════════════════════════════════════════════════════════════════
p(8, 'terminarExamen() — hook comprensión',
'async function terminarExamen() {\n  await terminarExamen_JERO_PATCH();',
'async function terminarExamen() {\n  await terminarExamen_COMPRENSION_PATCH();\n  await terminarExamen_JERO_PATCH();')

# ════════════════════════════════════════════════════════════════════════
# PATCH 9 — Evitar doble guardado en Sheets para comprensión
# ════════════════════════════════════════════════════════════════════════
p(9, 'terminarExamen() — saltar guardado doble',
'  // Guardar en Sheets — solo para grado 6, Jero ya guardó arriba\n  if (!examenActual.esJero) try {',
'  // Guardar en Sheets — solo para grado 6 (Jero y Comprensión ya guardaron)\n  if (!examenActual.esJero && !examenActual.esComprension) try {')

# ════════════════════════════════════════════════════════════════════════
# Guardar index.html modificado
# ════════════════════════════════════════════════════════════════════════
with open(INDEX, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\n{"="*50}')
print(f'RESULTADO: {ok}/{T} patches aplicados {"✅" if ok==T else "⚠️"}')
print(f'Archivo guardado: {INDEX}')

# ════════════════════════════════════════════════════════════════════════
# Crear api/comprension.js
# ════════════════════════════════════════════════════════════════════════
API_FILE = os.path.join(HERE, 'api', 'comprension.js')
API_CONTENT = r"""const { google } = require('googleapis');
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
      "opciones": { "A": "...", "B": "...", "C": "...", "D": "..." },
      "respuesta": "B",
      "explicacion": "Explicación pedagógica de por qué esa respuesta es correcta..."
    }
  ]
}`;

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
  const nivelNum = parseInt(req.method === 'GET' ? req.query.nivel : (req.body||{}).nivel) || 1;
  const hoja = `Comprension_N${nivelNum}`;

  if (![1,2,3].includes(nivelNum))
    return res.status(400).json({ ok: false, error: 'Nivel inválido (1, 2 o 3)' });

  // ── GET: siguiente texto no hecho por el alumno ──────────────────────
  if (req.method === 'GET') {
    const nombre = req.query.nombre || '';
    try {
      const existe = await sheetExiste(sheets, hoja);
      if (!existe) return res.json({ ok: true, generar: true, total_banco: 0, hechos: 0 });

      // Banco de textos del nivel
      const bancoRes = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: `${hoja}!A2:E1000`,
      });
      const banco = (bancoRes.data.values || []).filter(r => r && r[0]);
      if (!banco.length) return res.json({ ok: true, generar: true, total_banco: 0, hechos: 0 });

      // Textos ya hechos por este alumno (buscar en Resultados)
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

      // Primer texto no hecho
      const siguiente = banco.find(row => !hechoSet.has(row[0]));
      if (siguiente) {
        let preguntas = [];
        try { preguntas = JSON.parse(siguiente[3]); } catch(e) {}
        return res.json({
          ok: true,
          id:       siguiente[0],
          titulo:   siguiente[1],
          texto:    siguiente[2],
          preguntas,
          es_nuevo: false,
          total_banco: banco.length,
          hechos:   hechoSet.size,
        });
      }

      // El alumno ya hizo todos los textos disponibles → generar uno nuevo
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
        return res.status(500).json({ ok: false, error: `Respuesta incompleta: ${data.preguntas?.length||0} preguntas generadas` });
      }

      // Crear hoja si no existe
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
        titulo:   data.titulo,
        texto:    data.texto,
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
"""

with open(API_FILE, 'w', encoding='utf-8') as f:
    f.write(API_CONTENT)
print(f'\n✅ api/comprension.js creado')

# ════════════════════════════════════════════════════════════════════════
# Crear api/setup-comprension.js
# ════════════════════════════════════════════════════════════════════════
SETUP_FILE = os.path.join(HERE, 'api', 'setup-comprension.js')
SETUP_CONTENT = r"""const { google } = require('googleapis');
const SHEET_ID = process.env.SHEET_ID;

module.exports = async (req, res) => {
  try {
    const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
    const auth = new google.auth.GoogleAuth({
      credentials,
      scopes: ['https://www.googleapis.com/auth/spreadsheets'],
    });
    const sheets = google.sheets({ version: 'v4', auth });

    const meta = await sheets.spreadsheets.get({ spreadsheetId: SHEET_ID });
    const existentes = meta.data.sheets.map(s => s.properties.title);

    const hojas = ['Comprension_N1','Comprension_N2','Comprension_N3'];
    const creadas = [];

    for (const nombre of hojas) {
      if (!existentes.includes(nombre)) {
        await sheets.spreadsheets.batchUpdate({
          spreadsheetId: SHEET_ID,
          requestBody: { requests: [{ addSheet: { properties: { title: nombre } } }] },
        });
        await sheets.spreadsheets.values.update({
          spreadsheetId: SHEET_ID,
          range: `${nombre}!A1:E1`,
          valueInputOption: 'RAW',
          requestBody: { values: [['ID','Titulo','Texto','Preguntas_JSON','Fecha']] },
        });
        creadas.push(nombre);
      }
    }

    return res.json({
      ok: true,
      mensaje: creadas.length > 0
        ? `Hojas creadas: ${creadas.join(', ')}`
        : 'Todas las hojas ya existían ✅',
      creadas,
    });
  } catch (e) {
    return res.status(500).json({ ok: false, error: e.message });
  }
};
"""

with open(SETUP_FILE, 'w', encoding='utf-8') as f:
    f.write(SETUP_CONTENT)
print(f'✅ api/setup-comprension.js creado')
print(f'\n{"="*50}')
print(f'TOTAL: {ok}/{T} patches en index.html + 2 archivos nuevos')
