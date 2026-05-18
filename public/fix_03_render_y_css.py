import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
raw = open(path, 'rb').read()
has_crlf = b'\r\n' in raw
content = raw.decode('utf-8').replace('\r\n', '\n')
applied = 0

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 1 — CSS: insertar estilos del camino de hitos antes de /* MIS RESULTADOS */
# ══════════════════════════════════════════════════════════════════════════════
CSS_OLD = '  /* MIS RESULTADOS */'

CSS_NEW = """\
  /* \u2500\u2500 JERO HITOS PATH \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */
  .jero-hitos-wrap { display:flex; flex-direction:column; gap:14px; padding:14px 0 80px; }
  .jero-hito-row   { display:flex; gap:18px; align-items:center; padding:0 12px; }

  .jero-hito-nodo {
    width:68px; height:68px; border-radius:50%;
    display:flex; flex-direction:column; align-items:center;
    justify-content:center; position:relative; flex-shrink:0;
    font-family:'Fredoka One',cursive; user-select:none;
  }
  .jero-hito-nodo.completado {
    background:linear-gradient(135deg,#51CF66,#37B24D);
    box-shadow:0 4px 14px rgba(81,207,102,0.45);
  }
  .jero-hito-nodo.activo {
    background:linear-gradient(135deg,#FF6B6B,#FA5252);
    box-shadow:0 4px 18px rgba(255,107,107,0.55);
    cursor:pointer;
    animation:hito-pulse 1.6s ease-in-out infinite;
  }
  .jero-hito-nodo.activo:active { transform:scale(0.92); animation:none; }
  .jero-hito-nodo.bloqueado     { background:#D8D8D8; box-shadow:none; cursor:default; }
  .jero-hito-nodo.reto          { border:3px solid rgba(255,255,255,0.5); }
  .jero-hito-nodo.reto.completado {
    background:linear-gradient(135deg,#FFD700,#FFA500);
    box-shadow:0 4px 20px rgba(255,215,0,0.5);
  }
  .hito-icon { font-size:1.7rem; line-height:1; color:white; font-weight:900; }
  .jero-hito-nodo.bloqueado .hito-icon { opacity:0.55; font-size:1.25rem; }

  .hito-burbuja {
    position:absolute; bottom:calc(100% + 10px); left:50%;
    transform:translateX(-50%); white-space:nowrap;
    background:#1A1A2E; color:white;
    padding:5px 13px; border-radius:20px;
    font-family:Nunito,sans-serif; font-size:0.7rem; font-weight:800;
    pointer-events:none; z-index:10;
    box-shadow:0 2px 10px rgba(0,0,0,0.25);
  }
  .hito-burbuja::after {
    content:''; position:absolute; top:100%; left:50%;
    transform:translateX(-50%);
    border:6px solid transparent; border-top-color:#1A1A2E;
  }
  @keyframes hito-pulse {
    0%,100% { transform:scale(1);    box-shadow:0 4px 18px rgba(255,107,107,0.55); }
    50%     { transform:scale(1.13); box-shadow:0 6px 26px rgba(255,107,107,0.75); }
  }

  .jero-panel-overlay {
    position:fixed; inset:0; background:rgba(0,0,0,0.45);
    z-index:499; animation:fadeIn 0.2s ease;
  }
  .jero-hito-panel {
    position:fixed; bottom:0; left:0; right:0; z-index:500;
    background:white; border-radius:24px 24px 0 0;
    padding:20px 16px 40px; box-shadow:0 -8px 32px rgba(0,0,0,0.18);
    animation:slideUp 0.25s ease both;
    max-height:72vh; overflow-y:auto;
  }
  @keyframes slideUp {
    from { transform:translateY(100%); opacity:0; }
    to   { transform:translateY(0);    opacity:1; }
  }
  .hito-panel-header {
    display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;
  }
  .hito-panel-titulo {
    font-family:'Fredoka One',cursive; font-size:1.15rem; color:#1A1A2E;
  }
  .hito-panel-close {
    background:none; border:none; font-size:1.2rem; cursor:pointer;
    color:#888; padding:4px 8px; border-radius:8px; line-height:1;
  }
  .hito-panel-mat {
    width:100%; padding:14px 16px; border-radius:14px;
    border:2px solid #E8E8E8; background:white;
    font-family:Nunito,sans-serif; font-weight:800; font-size:0.95rem;
    cursor:pointer; display:flex; justify-content:space-between;
    align-items:center; margin-bottom:8px; transition:all 0.15s;
    color:#1A1A2E; text-align:left;
  }
  .hito-panel-mat:hover:not(.done) { border-color:#339AF0; background:#F0F8FF; transform:translateX(4px); }
  .hito-panel-mat.done { background:#F0FFF4; border-color:#51CF66; color:#2F9E44; cursor:default; }
  .hito-panel-ref {
    width:100%; padding:10px 16px; border-radius:12px; margin-bottom:8px;
    border:2px solid #845EF7; background:linear-gradient(135deg,#F0EBFF,#E8F4FF);
    font-family:Nunito,sans-serif; font-weight:800; font-size:0.82rem;
    cursor:pointer; color:#6741D9; text-align:left;
  }

  /* MIS RESULTADOS */"""

if CSS_OLD in content:
    content = content.replace(CSS_OLD, CSS_NEW, 1)
    applied += 1
    print('  \u2705 Patch 1: CSS de hitos insertado')
else:
    print('  \u274c Patch 1: anchor "/* MIS RESULTADOS */" no encontrado')

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 2 — JS: reemplazar renderJero() con camino de hitos en zigzag
# ══════════════════════════════════════════════════════════════════════════════
NUEVA_RENDER = """\
async function renderJero() {
  if (!estado.jeroProgreso) estado.jeroProgreso = {};
  document.getElementById('jero-titulo').textContent = `\u00a1Hola, ${estado.nombre}! \U0001F44B`;
  await sincronizarProgresoJeroDesdeSheets();
  const cont = document.getElementById('jero-materias-container');
  cont.innerHTML = '';

  const hitoAct  = jeroHitoActual();
  const RETOS    = [28, 56, 84, 112];
  const POR_FILA = 4;
  const frases   = ['\u00a1T\u00fa puedes! \U0001F4AA', '\u00a1Sigue! \U0001F680', '\u00a1Lo est\u00e1s logrando! \u2b50', '\u00a1Campe\u00f3n! \U0001F3C6', '\u00a1Crack! \U0001F525'];
  const frase    = frases[(hitoAct - 1) % frases.length];

  const wrap = document.createElement('div');
  wrap.className = 'jero-hitos-wrap';

  const totalFilas = Math.ceil(TOTAL_LECCIONES_JERO / POR_FILA);
  let nodoActivo = null;

  for (let row = 0; row < totalFilas; row++) {
    const fila = document.createElement('div');
    fila.className = 'jero-hito-row';
    // Zigzag: filas impares invierten direcci\u00f3n para formar la serpiente
    if (row % 2 === 1) fila.style.flexDirection = 'row-reverse';

    for (let col = 0; col < POR_FILA; col++) {
      const n = row * POR_FILA + col + 1;
      if (n > TOTAL_LECCIONES_JERO) break;

      const esReto = RETOS.includes(n);
      const esCom  = jeroHitoCompleto(n);
      const esAct  = n === hitoAct;
      const esBloq = n > hitoAct;

      const nodo = document.createElement('div');
      let cls = 'jero-hito-nodo';
      if (esReto)  cls += ' reto';
      if (esCom)        cls += ' completado';
      else if (esAct)   cls += ' activo';
      else if (esBloq)  cls += ' bloqueado';
      nodo.className = cls;

      if (esCom) {
        nodo.innerHTML = '<span class="hito-icon">\u2713</span>';
      } else if (esAct) {
        nodo.innerHTML = `<span class="hito-icon">${esReto ? '\u2b50' : '\u25b6'}</span><div class="hito-burbuja">${frase}</div>`;
        nodo.onclick = () => { sonidoClick(); abrirPanelHito(n); };
        nodoActivo = nodo;
      } else {
        nodo.innerHTML = `<span class="hito-icon">${esReto ? '\u2b50' : '\U0001F512'}</span>`;
      }

      fila.appendChild(nodo);
    }
    wrap.appendChild(fila);
  }

  cont.appendChild(wrap);
  if (nodoActivo) setTimeout(() => nodoActivo.scrollIntoView({ behavior:'smooth', block:'center' }), 350);
}"""

# Localizar renderJero usando su inicio único y el marcador que sigue
SPLIT_AFTER = '\nasync function iniciarLeccionJero(materia, leccion) {'
FUNC_START  = 'async function renderJero() {'

partes = content.split(SPLIT_AFTER)
if len(partes) == 2:
    antes, despues = partes[0], SPLIT_AFTER + partes[1]
    idx = antes.rfind(FUNC_START)
    if idx != -1:
        content = antes[:idx] + NUEVA_RENDER + '\n\n' + despues
        applied += 1
        print('  \u2705 Patch 2: renderJero() reemplazada con camino de hitos en zigzag')
    else:
        print('  \u274c Patch 2: "async function renderJero()" no encontrada')
else:
    print(f'  \u274c Patch 2: marcador iniciarLeccionJero no encontrado (partes: {len(partes)})')

if has_crlf:
    content = content.replace('\n', '\r\n')
open(path, 'wb').write(content.encode('utf-8'))
total = 2
print(f'\n{applied}/{total} patches aplicados {"✅" if applied == total else "⚠️  revisa errores"}')
