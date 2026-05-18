import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
raw = open(path, 'rb').read()
has_crlf = b'\r\n' in raw
content = raw.decode('utf-8').replace('\r\n', '\n')

NUEVAS_FUNCIONES = r"""
function jeroHitoCompleto(n) {
  return Object.keys(MATERIAS_JERO).every(m =>
    (estado.jeroProgreso?.[m]?.completadas || []).includes(n)
  );
}

function jeroHitoActual() {
  for (let n = 1; n <= TOTAL_LECCIONES_JERO; n++) {
    if (!jeroHitoCompleto(n)) return n;
  }
  return TOTAL_LECCIONES_JERO;
}

function abrirPanelHito(n) {
  document.getElementById('jero-hito-panel')?.remove();
  document.getElementById('jero-panel-overlay')?.remove();
  const esReto = [28,56,84,112].includes(n);
  const etapa  = Math.ceil(n / 28);

  const overlay = document.createElement('div');
  overlay.id = 'jero-panel-overlay';
  overlay.className = 'jero-panel-overlay';
  const cerrar = () => {
    document.getElementById('jero-hito-panel')?.remove();
    document.getElementById('jero-panel-overlay')?.remove();
  };
  overlay.onclick = cerrar;

  const panel = document.createElement('div');
  panel.id = 'jero-hito-panel';
  panel.className = 'jero-hito-panel';

  const header = document.createElement('div');
  header.className = 'hito-panel-header';
  const titulo = document.createElement('span');
  titulo.className = 'hito-panel-titulo';
""" + r"  titulo.textContent = esReto ? `\u2b50 Reto \u2014 Etapa ${etapa}` : `Hito ${n} de ${TOTAL_LECCIONES_JERO}`;" + r"""
  const btnClose = document.createElement('button');
  btnClose.className = 'hito-panel-close';
  btnClose.textContent = '\u2715';
  btnClose.onclick = cerrar;
  header.appendChild(titulo);
  header.appendChild(btnClose);
  panel.appendChild(header);

  Object.entries(MATERIAS_JERO).forEach(([key, mat]) => {
    const comp    = (estado.jeroProgreso?.[key]?.completadas || []).includes(n);
    const numErr  = comp ? tieneErroresGuardadosJero(n, key) : 0;

    const btn = document.createElement('button');
    btn.className = 'hito-panel-mat' + (comp ? ' done' : '');
""" + r"    btn.innerHTML = `<span>${mat.emoji} ${mat.nombre}</span><span>${comp ? '\u2713' : '\u2192'}</span>`;" + r"""
    if (!comp) {
      btn.onclick = () => { cerrar(); iniciarLeccionJero(key, n); };
    }
    panel.appendChild(btn);

    if (comp && numErr > 0) {
      const ref = document.createElement('button');
      ref.className = 'hito-panel-ref';
""" + r"      ref.textContent = `\uD83D\uDD01`.replace(/./u, '\ud83d\udd01') " + r"""
        || ('\uD83D\uDD01'); // 🔁
      ref.textContent = '\uD83D\uDD01 Refuerzo \u00b7 ' + numErr + ' error' + (numErr > 1 ? 'es' : '');
      ref.onclick = () => { cerrar(); iniciarRefuerzoJero(n, key); };
      panel.appendChild(ref);
    }
  });

  document.body.appendChild(overlay);
  document.body.appendChild(panel);
}
"""

# Escribir los helpers como texto directo con emojis incluídos
HELPERS = """
function jeroHitoCompleto(n) {
  return Object.keys(MATERIAS_JERO).every(m =>
    (estado.jeroProgreso?.[m]?.completadas || []).includes(n)
  );
}

function jeroHitoActual() {
  for (let n = 1; n <= TOTAL_LECCIONES_JERO; n++) {
    if (!jeroHitoCompleto(n)) return n;
  }
  return TOTAL_LECCIONES_JERO;
}

function abrirPanelHito(n) {
  document.getElementById('jero-hito-panel')?.remove();
  document.getElementById('jero-panel-overlay')?.remove();
  const esReto = [28,56,84,112].includes(n);
  const etapa  = Math.ceil(n / 28);

  const overlay = document.createElement('div');
  overlay.id = 'jero-panel-overlay';
  overlay.className = 'jero-panel-overlay';
  const cerrar = () => {
    document.getElementById('jero-hito-panel')?.remove();
    document.getElementById('jero-panel-overlay')?.remove();
  };
  overlay.onclick = cerrar;

  const panel = document.createElement('div');
  panel.id = 'jero-hito-panel';
  panel.className = 'jero-hito-panel';

  const header = document.createElement('div');
  header.className = 'hito-panel-header';
  const titulo = document.createElement('span');
  titulo.className = 'hito-panel-titulo';
  titulo.textContent = esReto ? `\u2b50 Reto \u2014 Etapa ${etapa}` : `Hito ${n} de ${TOTAL_LECCIONES_JERO}`;
  const btnClose = document.createElement('button');
  btnClose.className = 'hito-panel-close';
  btnClose.textContent = '\u2715';
  btnClose.onclick = cerrar;
  header.appendChild(titulo);
  header.appendChild(btnClose);
  panel.appendChild(header);

  Object.entries(MATERIAS_JERO).forEach(([key, mat]) => {
    const comp   = (estado.jeroProgreso?.[key]?.completadas || []).includes(n);
    const numErr = comp ? tieneErroresGuardadosJero(n, key) : 0;

    const btn = document.createElement('button');
    btn.className = 'hito-panel-mat' + (comp ? ' done' : '');
    btn.innerHTML = `<span>${mat.emoji} ${mat.nombre}</span><span>${comp ? '\u2713' : '\u2192'}</span>`;
    if (!comp) {
      btn.onclick = () => { cerrar(); iniciarLeccionJero(key, n); };
    }
    panel.appendChild(btn);

    if (comp && numErr > 0) {
      const ref = document.createElement('button');
      ref.className = 'hito-panel-ref';
      ref.textContent = '\U0001F501 Refuerzo \u00b7 ' + numErr + ' error' + (numErr > 1 ? 'es' : '');
      ref.onclick = () => { cerrar(); iniciarRefuerzoJero(n, key); };
      panel.appendChild(ref);
    }
  });

  document.body.appendChild(overlay);
  document.body.appendChild(panel);
}
"""

OLD = ("function getEstrellasJero(mat) {\n"
       "  const completadas = estado.jeroProgreso?.[mat]?.completadas?.length || 0;\n"
       "  if (completadas === 0) return '\u2606\u2606\u2606';\n"
       "  if (completadas < 5)  return '\u2b50\u2606\u2606';\n"
       "  if (completadas < 15) return '\u2b50\u2b50\u2606';\n"
       "  return '\u2b50\u2b50\u2b50';\n"
       "}\n"
       "\nasync function sincronizarProgresoJeroDesdeSheets() {")

NEW = ("function getEstrellasJero(mat) {\n"
       "  const completadas = estado.jeroProgreso?.[mat]?.completadas?.length || 0;\n"
       "  if (completadas === 0) return '\u2606\u2606\u2606';\n"
       "  if (completadas < 5)  return '\u2b50\u2606\u2606';\n"
       "  if (completadas < 15) return '\u2b50\u2b50\u2606';\n"
       "  return '\u2b50\u2b50\u2b50';\n"
       "}\n"
       + HELPERS +
       "\nasync function sincronizarProgresoJeroDesdeSheets() {")

applied = 0
if OLD in content:
    content = content.replace(OLD, NEW, 1)
    applied += 1
    print('  \u2705 Patch 1: jeroHitoCompleto + jeroHitoActual + abrirPanelHito insertados')
else:
    print('  \u274c Patch 1: anchor getEstrellasJero no encontrado')
    # Debug
    idx = content.find('function getEstrellasJero')
    if idx >= 0:
        print(f'    (encontrada en pos {idx}, mostrando 20 chars): {content[idx:idx+80]!r}')

if has_crlf:
    content = content.replace('\n', '\r\n')
open(path, 'wb').write(content.encode('utf-8'))
total = 1
print(f'\n{applied}/{total} patches aplicados {"✅" if applied == total else "⚠️  revisa errores"}')
