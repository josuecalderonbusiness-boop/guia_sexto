import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'public', 'index.html')

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

patches = []

# ══════════════════════════════════════════════════════════════════════
# PATCH 1 — CSS para el dashboard de Jero
# ══════════════════════════════════════════════════════════════════════
OLD1 = '  /* MIS RESULTADOS */'
NEW1 = '''  /* ── JERO GRADO 2 ──────────────────────────────────────────────── */
  #screen-jero { display:none; padding:20px 16px; max-width:600px; margin:0 auto; }
  .jero-saludo {
    text-align:center; margin-bottom:24px;
  }
  .jero-saludo .mascota { font-size:4rem; animation: bounce 1.5s ease-in-out infinite; display:block; margin-bottom:8px; }
  .jero-saludo h2 { font-family:'Fredoka One',cursive; font-size:1.8rem; color:#1A1A2E; }
  .jero-saludo p { color:#666; font-size:1rem; margin-top:4px; }
  @keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }

  .jero-materias { display:flex; flex-direction:column; gap:14px; }

  .jero-materia-card {
    border-radius:24px; padding:20px 22px;
    display:flex; align-items:center; gap:16px;
    cursor:pointer; transition:transform 0.2s, box-shadow 0.2s;
    position:relative; overflow:hidden; border:none;
    width:100%; text-align:left;
  }
  .jero-materia-card:hover:not(:disabled) { transform:translateY(-4px) scale(1.02); }
  .jero-materia-card:disabled { opacity:0.45; cursor:not-allowed; filter:grayscale(0.4); }
  .jero-materia-card::before {
    content:''; position:absolute; top:-40px; right:-40px;
    width:120px; height:120px; border-radius:50%;
    background:rgba(255,255,255,0.15);
  }

  .jero-mat-icon { font-size:2.8rem; flex-shrink:0; filter:drop-shadow(0 2px 4px rgba(0,0,0,0.2)); }
  .jero-mat-info { flex:1; }
  .jero-mat-nombre { font-family:'Fredoka One',cursive; font-size:1.3rem; color:white; display:block; }
  .jero-mat-estado { font-size:0.85rem; color:rgba(255,255,255,0.85); font-weight:700; margin-top:2px; display:block; }

  .jero-mat-progreso {
    display:flex; flex-direction:column; align-items:center; gap:4px; flex-shrink:0;
  }
  .jero-estrellas { font-size:1.2rem; letter-spacing:2px; }
  .jero-leccion-badge {
    background:rgba(255,255,255,0.25); color:white;
    padding:3px 10px; border-radius:50px; font-size:0.78rem; font-weight:800;
  }

  .jero-lock { font-size:2rem; flex-shrink:0; }

  /* Partículas de confetti al completar */
  @keyframes particle-fly {
    0%   { transform:translate(0,0) rotate(0deg); opacity:1; }
    100% { transform:translate(var(--tx),var(--ty)) rotate(720deg); opacity:0; }
  }
  .particle {
    position:fixed; width:10px; height:10px; border-radius:2px;
    pointer-events:none; z-index:9999;
    animation:particle-fly 0.9s ease-out forwards;
  }

  /* MIS RESULTADOS */'''

if OLD1 in src:
    src = src.replace(OLD1, NEW1)
    patches.append('PATCH 1 ✅ CSS dashboard Jero')
else:
    patches.append('PATCH 1 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 2 — Agregar screen-jero al HTML (después de screen-inicio)
# ══════════════════════════════════════════════════════════════════════
OLD2 = '<div id="screen-examen">'
NEW2 = '''<div id="screen-jero">
  <div class="jero-saludo">
    <span class="mascota">🧠</span>
    <h2 id="jero-titulo">¡Hola, Jero!</h2>
    <p>Elige qué quieres aprender hoy 🌟</p>
  </div>
  <div class="jero-materias" id="jero-materias-container"></div>
  <div style="text-align:center;margin-top:20px">
    <button onclick="verMisResultados()" style="background:linear-gradient(135deg,#1A1A2E,#0F3460);color:white;border:none;border-radius:16px;padding:12px 28px;font-family:Nunito,sans-serif;font-weight:800;font-size:0.95rem;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,0.2)">📊 Mis Resultados</button>
  </div>
</div>

<div id="screen-examen">'''

if OLD2 in src:
    src = src.replace(OLD2, NEW2, 1)
    patches.append('PATCH 2 ✅ screen-jero agregado al HTML')
else:
    patches.append('PATCH 2 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 3 — Agregar screen-jero a la función mostrar()
# ══════════════════════════════════════════════════════════════════════
OLD3 = "  ['screen-login','screen-grado','screen-inicio','screen-examen','screen-resultado','screen-misresultados','screen-admin','screen-refuerzo'].forEach(s => {"
NEW3 = "  ['screen-login','screen-grado','screen-inicio','screen-jero','screen-examen','screen-resultado','screen-misresultados','screen-admin','screen-refuerzo'].forEach(s => {"

if OLD3 in src:
    src = src.replace(OLD3, NEW3)
    patches.append('PATCH 3 ✅ screen-jero en función mostrar()')
else:
    patches.append('PATCH 3 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 4 — Login guarda grado y va directo si grado viene del Sheet
# ══════════════════════════════════════════════════════════════════════
OLD4 = '''    estado.nombre = data.nombre;
    estado.codigo = data.codigo;
    estado.esAdmin = data.esAdmin || false;
    guardarEstadoLocal();
    mostrarHeaderNombre();
    if (estado.esAdmin) {
      mostrar('screen-admin');
      adminInit();
    } else {
      mostrar('screen-grado');
    }'''

NEW4 = '''    estado.nombre = data.nombre;
    estado.codigo = data.codigo;
    estado.esAdmin = data.esAdmin || false;
    if (data.grado) estado.grado = data.grado;
    guardarEstadoLocal();
    mostrarHeaderNombre();
    if (estado.esAdmin) {
      mostrar('screen-admin');
      adminInit();
    } else if (estado.grado === 2) {
      mostrar('screen-jero');
      renderJero();
    } else if (estado.grado) {
      mostrar('screen-inicio');
      await sincronizarCompletadosDesdeSheets();
      renderInicio();
    } else {
      mostrar('screen-grado');
    }'''

if OLD4 in src:
    src = src.replace(OLD4, NEW4)
    patches.append('PATCH 4 ✅ login usa grado del Sheet, salta pantalla de selección')
else:
    patches.append('PATCH 4 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 5 — elegirGrado redirige a Jero si grado=2
# ══════════════════════════════════════════════════════════════════════
OLD5 = '''async function elegirGrado(grado) {
  estado.grado = grado;
  guardarEstadoLocal();
  mostrar('screen-inicio');
  await sincronizarCompletadosDesdeSheets();
  renderInicio();
}'''

NEW5 = '''async function elegirGrado(grado) {
  estado.grado = grado;
  guardarEstadoLocal();
  if (grado === 2) {
    mostrar('screen-jero');
    renderJero();
  } else {
    mostrar('screen-inicio');
    await sincronizarCompletadosDesdeSheets();
    renderInicio();
  }
}'''

if OLD5 in src:
    src = src.replace(OLD5, NEW5)
    patches.append('PATCH 5 ✅ elegirGrado redirige a Jero')
else:
    patches.append('PATCH 5 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 6 — volverInicio redirige según grado
# ══════════════════════════════════════════════════════════════════════
OLD6 = '''function volverInicio() {
  mostrar('screen-inicio');
  renderInicio();
  window.scrollTo(0,0);
}'''

NEW6 = '''function volverInicio() {
  if (estado.grado === 2) {
    mostrar('screen-jero');
    renderJero();
  } else {
    mostrar('screen-inicio');
    renderInicio();
  }
  window.scrollTo(0,0);
}'''

if OLD6 in src:
    src = src.replace(OLD6, NEW6)
    patches.append('PATCH 6 ✅ volverInicio según grado')
else:
    patches.append('PATCH 6 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 7 — Init al cargar: redirige a Jero si grado=2
# ══════════════════════════════════════════════════════════════════════
OLD7 = '''cargarEstado();
if (estado.nombre) {
  mostrarHeaderNombre();
  if (estado.esAdmin) {
    mostrar('screen-admin');
    adminInit();
  } else {
    mostrar('screen-inicio');
    sincronizarCompletadosDesdeSheets().then(() => renderInicio());
  }
} else {
  mostrar('screen-login');
}'''

NEW7 = '''cargarEstado();
if (estado.nombre) {
  mostrarHeaderNombre();
  if (estado.esAdmin) {
    mostrar('screen-admin');
    adminInit();
  } else if (estado.grado === 2) {
    mostrar('screen-jero');
    renderJero();
  } else {
    mostrar('screen-inicio');
    sincronizarCompletadosDesdeSheets().then(() => renderInicio());
  }
} else {
  mostrar('screen-login');
}'''

if OLD7 in src:
    src = src.replace(OLD7, NEW7)
    patches.append('PATCH 7 ✅ init redirige a Jero si grado=2')
else:
    patches.append('PATCH 7 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# PATCH 8 — Agregar toda la lógica de Jero antes del cierre </script>
# ══════════════════════════════════════════════════════════════════════
JERO_JS = '''
// ══════════════════════════════════════════════════════════════════
// ── JERO — GRADO 2 ───────────────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

const MATERIAS_JERO = {
  MAT: { nombre:'Matemáticas',      emoji:'🔢', bg:'linear-gradient(135deg,#FF6B6B,#FA5252)', shadow:'rgba(255,107,107,0.4)' },
  LCA: { nombre:'Lengua Castellana',emoji:'📖', bg:'linear-gradient(135deg,#339AF0,#1971C2)', shadow:'rgba(51,154,240,0.4)'  },
  ING: { nombre:'Inglés',           emoji:'🌎', bg:'linear-gradient(135deg,#51CF66,#37B24D)', shadow:'rgba(81,207,102,0.4)'  },
  NAT: { nombre:'Naturales',        emoji:'🌿', bg:'linear-gradient(135deg,#845EF7,#6741D9)', shadow:'rgba(132,94,247,0.4)'  },
  SOC: { nombre:'Sociales',         emoji:'🏘️', bg:'linear-gradient(135deg,#FF922B,#F76707)', shadow:'rgba(255,146,43,0.4)'  },
};

const TOTAL_LECCIONES_JERO = 20;

// Web Audio API — sonidos simples sin archivos externos
function playTono(freq, dur, type='sine') {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.connect(g); g.connect(ctx.destination);
    o.type = type; o.frequency.value = freq;
    g.gain.setValueAtTime(0.18, ctx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
    o.start(); o.stop(ctx.currentTime + dur);
  } catch(e) {}
}
function sonidoClick()     { playTono(520, 0.12); }
function sonidoCorrecto()  { playTono(660, 0.12); setTimeout(()=>playTono(880,0.18),120); }
function sonidoError()     { playTono(220, 0.3, 'sawtooth'); }
function sonidoEstrella()  { [523,659,784,1047].forEach((f,i)=>setTimeout(()=>playTono(f,0.18),i*100)); }

function lanzarParticulasJero(x, y) {
  const colors = ['#FF6B6B','#51CF66','#339AF0','#FF922B','#845EF7','#FFD700'];
  for (let i = 0; i < 18; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    const angle = (Math.PI * 2 * i) / 18;
    const dist = 80 + Math.random() * 80;
    p.style.cssText = `left:${x}px;top:${y}px;background:${colors[i%colors.length]};--tx:${Math.cos(angle)*dist}px;--ty:${Math.sin(angle)*dist}px`;
    document.body.appendChild(p);
    setTimeout(() => p.remove(), 950);
  }
}

function getLeccionActualJero(mat) {
  const estado_mat = estado.jeroProgreso?.[mat] || { leccionActual: 1, completadas: [] };
  return estado_mat;
}

function jeroLeccionCompletada(mat, leccion) {
  return estado.jeroProgreso?.[mat]?.completadas?.includes(leccion) || false;
}

function jeroLeccionDisponible(mat, leccion) {
  if (leccion === 1) return true;
  return jeroLeccionCompletada(mat, leccion - 1);
}

function getProximaLeccionJero(mat) {
  for (let l = 1; l <= TOTAL_LECCIONES_JERO; l++) {
    if (!jeroLeccionCompletada(mat, l)) return l;
  }
  return TOTAL_LECCIONES_JERO; // todas completas
}

function getEstrellasJero(mat) {
  const completadas = estado.jeroProgreso?.[mat]?.completadas?.length || 0;
  if (completadas === 0) return '☆☆☆';
  if (completadas < 5)  return '⭐☆☆';
  if (completadas < 15) return '⭐⭐☆';
  return '⭐⭐⭐';
}

async function renderJero() {
  if (!estado.jeroProgreso) estado.jeroProgreso = {};
  document.getElementById('jero-titulo').textContent = `¡Hola, ${estado.nombre}! 👋`;
  const cont = document.getElementById('jero-materias-container');
  cont.innerHTML = '';

  for (const [key, mat] of Object.entries(MATERIAS_JERO)) {
    const proxLec = getProximaLeccionJero(key);
    const completadas = estado.jeroProgreso?.[key]?.completadas?.length || 0;
    const todasCompletas = completadas >= TOTAL_LECCIONES_JERO;
    const estrellas = getEstrellasJero(key);

    const btn = document.createElement('button');
    btn.className = 'jero-materia-card fade-in';
    btn.style.cssText = `background:${mat.bg};box-shadow:0 8px 24px ${mat.shadow}`;
    btn.innerHTML = `
      <span class="jero-mat-icon">${mat.emoji}</span>
      <div class="jero-mat-info">
        <span class="jero-mat-nombre">${mat.nombre}</span>
        <span class="jero-mat-estado">${todasCompletas ? '¡Todo completado! 🏆' : completadas === 0 ? '¡Comienza aquí!' : `Lección ${proxLec} de ${TOTAL_LECCIONES_JERO}`}</span>
      </div>
      <div class="jero-mat-progreso">
        <span class="jero-estrellas">${estrellas}</span>
        <span class="jero-leccion-badge">${completadas}/${TOTAL_LECCIONES_JERO}</span>
      </div>
    `;
    btn.onclick = async (e) => {
      sonidoClick();
      const rect = btn.getBoundingClientRect();
      lanzarParticulasJero(rect.left + rect.width/2, rect.top + rect.height/2);
      await iniciarLeccionJero(key, proxLec);
    };
    cont.appendChild(btn);
  }
}

async function iniciarLeccionJero(materia, leccion) {
  const mat = MATERIAS_JERO[materia];
  // Mostrar pantalla de carga
  mostrar('screen-examen');
  document.getElementById('examen-badge').textContent = `${mat.emoji} ${mat.nombre}`;
  document.getElementById('examen-badge').style.background = mat.bg;
  document.getElementById('examen-badge').style.color = 'white';
  document.getElementById('examen-badge').style.borderRadius = '50px';
  document.getElementById('examen-badge').style.padding = '6px 16px';
  document.getElementById('examen-dia-label').textContent = `⭐ Lección ${leccion}`;
  document.getElementById('progress-fill').style.background = mat.bg;
  document.getElementById('pregunta-container').innerHTML =
    '<div class="loading"><div class="spinner"></div><span>Preparando tu lección... ✨</span></div>';

  try {
    // 1. Intentar cargar preguntas existentes del Sheet
    let res = await fetch(`/api/preguntas?grado=2&materia=${materia}&leccion=${leccion}`);
    let data = await res.json();

    // 2. Si no hay preguntas → generar con IA
    if (!data.ok || !data.preguntas || data.preguntas.length === 0) {
      document.getElementById('pregunta-container').innerHTML =
        '<div class="loading"><div class="spinner"></div><span>🤖 Preparando preguntas nuevas para ti...</span></div>';

      const genRes = await fetch('/api/generar-leccion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ grado: 2, materia, leccion })
      });
      const genData = await genRes.json();
      if (!genData.ok) {
        document.getElementById('pregunta-container').innerHTML =
          `<div class="error-msg">⚠️ No se pudo preparar la lección. Intenta de nuevo.<br><small>${genData.error||''}</small></div>`;
        return;
      }
      // Recargar preguntas ya generadas
      res = await fetch(`/api/preguntas?grado=2&materia=${materia}&leccion=${leccion}`);
      data = await res.json();
    }

    if (!data.ok || !data.preguntas?.length) {
      document.getElementById('pregunta-container').innerHTML =
        '<div class="error-msg">⚠️ No se pudieron cargar las preguntas. Intenta de nuevo.</div>';
      return;
    }

    examenActual = {
      dia: `G2_L${leccion}`,
      materia,
      preguntas: data.preguntas,
      idx: 0, respuestas: [], puntaje: 0, intentos: 0,
      esJero: true, leccionJero: leccion,
    };
    renderPregunta();

  } catch(e) {
    document.getElementById('pregunta-container').innerHTML =
      `<div class="error-msg">⚠️ Error de conexión. Revisa el internet e intenta de nuevo.</div>`;
  }
}

// Parchar terminarExamen para marcar lección de Jero como completada
const _terminarExamenOriginal = terminarExamen;
async function terminarExamen() {
  if (examenActual.esJero) {
    const { materia, leccionJero, puntaje, preguntas } = examenActual;
    if (!estado.jeroProgreso) estado.jeroProgreso = {};
    if (!estado.jeroProgreso[materia]) estado.jeroProgreso[materia] = { completadas: [] };
    const ya = estado.jeroProgreso[materia].completadas;
    if (!ya.includes(leccionJero)) ya.push(leccionJero);
    guardarEstadoLocal();

    // Generar la siguiente lección en segundo plano (sin bloquear)
    const siguiente = leccionJero + 1;
    if (siguiente <= TOTAL_LECCIONES_JERO) {
      fetch('/api/generar-leccion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ grado: 2, materia, leccion: siguiente })
      }).catch(() => {});
    }

    // Sonido de celebración
    const pct = Math.round((puntaje / preguntas.length) * 100);
    if (pct >= 80) sonidoEstrella();
    else sonidoCorrecto();
  }
  await _terminarExamenOriginal();
}
'''

OLD8 = '// ── VOLVER ───────────────────────────────────────────────────────'
NEW8 = JERO_JS + '\n' + OLD8

if OLD8 in src:
    src = src.replace(OLD8, NEW8, 1)
    patches.append('PATCH 8 ✅ lógica completa de Jero agregada')
else:
    patches.append('PATCH 8 ❌ no encontrado')

# ══════════════════════════════════════════════════════════════════════
# Guardar
# ══════════════════════════════════════════════════════════════════════
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

ok = sum(1 for p in patches if '✅' in p)
print(f'\nindex.html — {ok}/{len(patches)} patches aplicados')
for p in patches:
    print(' ', p)
