"""
fix_refuerzo_desde_resultados.py
Reconstruye los errores de refuerzo cruzando datos de Resultados con las
preguntas del Sheet. Funciona en cualquier dispositivo sin depender de localStorage.

Ejecutar: python fix_refuerzo_desde_resultados.py
Resultado esperado: 4/4 patches aplicados
"""

import os

BASE  = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, 'index.html')

patches_ok = 0
patches_total = 4

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 1 — Nueva función: cargarErroresDesdeResultados
# Cruza Resultados (tiene preguntas con ok:false) + /api/preguntas (tiene opciones)
# ══════════════════════════════════════════════════════════════════════════════

OLD1 = "// ── REFUERZO ─────────────────────────────────────────────────────────"

NEW1 = """// ── REFUERZO ─────────────────────────────────────────────────────────

// Reconstruye errores cruzando Resultados con las preguntas del Sheet
async function cargarErroresDesdeResultados(dia, materia) {
  const mat = MATERIAS[materia];
  const diaLabel = `Día ${dia}`;

  // 1. Obtener resultados del alumno
  const resR = await fetch('/api/resultados?nombre=' + encodeURIComponent(estado.nombre));
  const dataR = await resR.json();
  if (!dataR.ok || !dataR.resultados) return [];

  // Buscar el resultado de este dia+materia (el más reciente si hay varios)
  const resultadosFiltrados = dataR.resultados.filter(r =>
    r.materia === mat.nombre &&
    (r.dia === diaLabel || r.dia === `Dia ${dia}` || r.dia === String(dia))
  );
  if (!resultadosFiltrados.length) return [];

  // Tomar el más reciente
  const resultado = resultadosFiltrados[resultadosFiltrados.length - 1];
  let respuestas = [];
  try {
    respuestas = typeof resultado.respuestas === 'string'
      ? JSON.parse(resultado.respuestas)
      : resultado.respuestas;
  } catch(e) { return []; }

  const erroresBasicos = respuestas.filter(r => !r.ok);
  if (!erroresBasicos.length) return [];

  // 2. Obtener preguntas del Sheet para cruzar opciones
  const resP = await fetch(`/api/preguntas?dia=${dia}&materia=${materia}`);
  const dataP = await resP.json();
  if (!dataP.ok || !dataP.preguntas) return [];

  // 3. Cruzar: para cada error, buscar la pregunta completa con opciones
  const erroresCompletos = [];
  for (const err of erroresBasicos) {
    const pregObj = dataP.preguntas.find(p =>
      p.pregunta && err.pregunta &&
      p.pregunta.trim().substring(0, 40) === err.pregunta.trim().substring(0, 40)
    );
    if (pregObj && pregObj.opciones && pregObj.opciones.A) {
      erroresCompletos.push({
        pregunta: pregObj,
        elegida: err.elegida,
        correcta: err.correcta
      });
    }
  }
  return erroresCompletos;
}"""

if OLD1 in html:
    html = html.replace(OLD1, NEW1)
    patches_ok += 1
    print("  ✅ Patch 1/4 — cargarErroresDesdeResultados: nueva función")
else:
    print("  ❌ Patch 1/4 — NO encontrado")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 2 — iniciarRefuerzoDesdeMenu: usar cargarErroresDesdeResultados como fallback
# ══════════════════════════════════════════════════════════════════════════════

OLD2 = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
  const key = `errores_${dia}_${materia}`;

  // 1. Intentar desde localStorage primero (más rápido, sin red)
  const erroresRaw = JSON.parse(localStorage.getItem(key) || '[]');
  const erroresLocal = erroresRaw.filter(e => e?.pregunta?.opciones?.A !== undefined);
  if (erroresLocal.length > 0) {
    arrancarRefuerzo(dia, materia, erroresLocal, null);
    return;
  }

  // 2. Sin localStorage → buscar en Sheets
  if (!estado.codigo) {
    alert('Inicia sesión para acceder al refuerzo desde cualquier dispositivo.');
    return;
  }

  // Guardar referencia al botón ANTES del try/finally
  const btnId = `btn-refuerzo-${dia}-${materia}`;
  const btnEl = document.getElementById(btnId);
  const textoOriginal = btnEl ? btnEl.innerHTML : '';

  try {
    if (btnEl) {
      btnEl.innerHTML = '⏳ Buscando en la nube...';
      btnEl.disabled = true;
      btnEl.style.opacity = '0.7';
    }

    const res = await fetch(
      `/api/errores?codigo=${encodeURIComponent(estado.codigo)}&dia=${dia}&materia=${encodeURIComponent(materia)}`,
      { signal: AbortSignal.timeout(8000) }   // timeout 8s
    );

    if (!res.ok) throw new Error('HTTP ' + res.status);

    const data = await res.json();

    if (data.ok && Array.isArray(data.errores) && data.errores.length > 0) {
      const validos = data.errores.filter(e => e?.pregunta?.opciones?.A !== undefined);
      if (validos.length > 0) {
        // Cachear en localStorage para la próxima vez
        localStorage.setItem(key, JSON.stringify(validos));
        arrancarRefuerzo(dia, materia, validos, null);
        return;   // sale del try → finally restaura si algo falla, pero aquí ya cambia pantalla
      }
    }

    // No hay errores guardados en Sheets tampoco
    alert('Aún no hay errores guardados en la nube.\\n¿Ya hiciste este examen en el otro dispositivo? Asegúrate de tener internet al terminar.');

  } catch(err) {
    if (err.name === 'TimeoutError') {
      alert('Se tardó demasiado. Revisa tu conexión e intenta de nuevo.');
    } else {
      alert('No se pudo conectar al servidor. Revisa el internet e intenta de nuevo.');
    }
  } finally {
    // SIEMPRE restaurar el botón, sin importar qué pasó
    if (btnEl) {
      btnEl.innerHTML = textoOriginal;
      btnEl.disabled = false;
      btnEl.style.opacity = '1';
    }
  }
}"""

NEW2 = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
  const key = `errores_${dia}_${materia}`;

  // 1. localStorage (más rápido, sin red)
  const erroresRaw = JSON.parse(localStorage.getItem(key) || '[]');
  const erroresLocal = erroresRaw.filter(e => e?.pregunta?.opciones?.A !== undefined);
  if (erroresLocal.length > 0) {
    arrancarRefuerzo(dia, materia, erroresLocal, null);
    return;
  }

  // 2. Reconstruir desde Resultados + preguntas del Sheet
  const btnId = `btn-refuerzo-${dia}-${materia}`;
  const btnEl = document.getElementById(btnId);
  const textoOriginal = btnEl ? btnEl.innerHTML : '';

  try {
    if (btnEl) {
      btnEl.innerHTML = '⏳ Cargando refuerzo...';
      btnEl.disabled = true;
      btnEl.style.opacity = '0.7';
    }

    const errores = await cargarErroresDesdeResultados(dia, materia);

    if (errores.length > 0) {
      // Cachear para la próxima vez
      localStorage.setItem(key, JSON.stringify(errores));
      arrancarRefuerzo(dia, materia, errores, null);
      return;
    }

    alert('No se encontraron errores para este refuerzo. ¡Puede que hayas aprobado todo!');

  } catch(err) {
    alert('Error de conexión. Revisa el internet e intenta de nuevo.');
  } finally {
    if (btnEl) {
      btnEl.innerHTML = textoOriginal;
      btnEl.disabled = false;
      btnEl.style.opacity = '1';
    }
  }
}"""

if OLD2 in html:
    html = html.replace(OLD2, NEW2)
    patches_ok += 1
    print("  ✅ Patch 2/4 — iniciarRefuerzoDesdeMenu: usa cargarErroresDesdeResultados")
else:
    print("  ❌ Patch 2/4 — NO encontrado")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 3 — renderInicio: mostrar botones de refuerzo también desde Resultados
# El problema: los botones solo aparecen si hay datos en localStorage.
# Fix: también mostrarlos si el alumno tuvo errores en Resultados (via completados).
# Añadir función que detecta materias con errores desde el resumen de resultados.
# ══════════════════════════════════════════════════════════════════════════════

OLD3 = "async function renderInicio() {"

NEW3 = """// Detecta qué dia/materia tienen errores guardados en localStorage O en caché de resultados
function tieneErroresGuardados(dia, mat) {
  const key = `errores_${dia}_${mat}`;
  const local = JSON.parse(localStorage.getItem(key) || '[]');
  if (local.filter(e => e?.pregunta?.opciones?.A !== undefined).length > 0) return local.length;
  // Buscar en caché de resultados (guardado por sincronizarBotonesRefuerzoDesdeSheets)
  const cacheKey = `errores_cache_${dia}_${mat}`;
  return parseInt(localStorage.getItem(cacheKey) || '0');
}

async function renderInicio() {"""

if OLD3 in html:
    html = html.replace(OLD3, NEW3, 1)
    patches_ok += 1
    print("  ✅ Patch 3/4 — tieneErroresGuardados: nueva función helper")
else:
    print("  ❌ Patch 3/4 — NO encontrado")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 4 — sincronizarBotonesRefuerzoDesdeSheets: cachear conteo de errores
# desde Resultados para que renderInicio muestre los botones correctamente
# ══════════════════════════════════════════════════════════════════════════════

OLD4 = """// Sincronizar errores desde Sheets a localStorage (silencioso, segundo plano)
async function sincronizarBotonesRefuerzoDesdeSheets() {
  if (!estado.codigo) return;
  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 6000);
    const res = await fetch(
      `/api/errores?codigo=${encodeURIComponent(estado.codigo)}&todos=1`,
      { signal: controller.signal }
    );
    clearTimeout(timer);
    if (!res.ok) return;           // 404/500 → silencioso (hoja puede no existir aún)
    const data = await res.json();
    if (!data.ok || !Array.isArray(data.entradas)) return;
    let sincronizados = 0;
    data.entradas.forEach(e => {
      if (!e.errores || !e.errores.length) return;
      const key = `errores_${e.dia}_${e.materia}`;
      const existentes = JSON.parse(localStorage.getItem(key) || '[]');
      // Solo escribir si localStorage no tiene datos frescos
      if (existentes.length === 0) {
        localStorage.setItem(key, JSON.stringify(e.errores));
        sincronizados++;
      }
    });
    // Refrescar el render solo si encontramos algo nuevo
    if (sincronizados > 0) renderInicio();
  } catch(e) {
    // Silencioso — red cortada, hoja inexistente, timeout → no importa
  }
}"""

NEW4 = """// Sincroniza qué materias tienen errores, usando Resultados como fuente de verdad
async function sincronizarBotonesRefuerzoDesdeSheets() {
  if (!estado.nombre) return;
  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 8000);
    const res = await fetch(
      '/api/resultados?nombre=' + encodeURIComponent(estado.nombre),
      { signal: controller.signal }
    );
    clearTimeout(timer);
    if (!res.ok) return;
    const data = await res.json();
    if (!data.ok || !data.resultados) return;

    const NOMBRES = { MAT:'Matemáticas', BIO:'Biología', QUI:'Química', SOC:'Cs. Sociales', LEN:'Lenguaje' };
    let cambios = 0;

    data.resultados.forEach(r => {
      const matKey = Object.keys(NOMBRES).find(k => NOMBRES[k] === r.materia);
      const diaNum = r.dia ? r.dia.replace('Día ','').replace('Dia ','').trim() : null;
      if (!matKey || !diaNum || isNaN(parseInt(diaNum))) return;
      if (r.dia.includes('Refuerzo')) return; // ignorar sesiones de refuerzo

      let respuestas = [];
      try { respuestas = typeof r.respuestas === 'string' ? JSON.parse(r.respuestas) : r.respuestas; } catch(e) {}
      const numErrores = respuestas.filter(rr => !rr.ok).length;

      // Guardar conteo en caché para que renderInicio muestre el botón
      const cacheKey = `errores_cache_${diaNum}_${matKey}`;
      const anterior = localStorage.getItem(cacheKey);
      if (numErrores > 0 && anterior !== String(numErrores)) {
        localStorage.setItem(cacheKey, String(numErrores));
        cambios++;
      } else if (numErrores === 0) {
        localStorage.removeItem(cacheKey);
      }
    });

    if (cambios > 0) renderInicio();
  } catch(e) {
    // Silencioso
  }
}"""

if OLD4 in html:
    html = html.replace(OLD4, NEW4)
    patches_ok += 1
    print("  ✅ Patch 4/4 — sincronizarBotonesRefuerzoDesdeSheets: usa Resultados como fuente")
else:
    print("  ❌ Patch 4/4 — NO encontrado")

# ══════════════════════════════════════════════════════════════════════════════
# Necesitamos también actualizar renderInicio para usar tieneErroresGuardados()
# El bloque de refuerzoHtml usa erroresGuardados.length — reemplazarlo
# ══════════════════════════════════════════════════════════════════════════════
OLD5 = """    for (const [key, mat] of Object.entries(MATERIAS)) {
      const erroresKey = `errores_${dia}_${key}`;
      const erroresGuardados = JSON.parse(localStorage.getItem(erroresKey) || 'null');
      if (erroresGuardados && erroresGuardados.length > 0 && materiaCompletada(dia, key)) {
        refuerzoHtml += `<button id="btn-refuerzo-${dia}-${key}" onclick="iniciarRefuerzoDesdeMenu(${dia},'${key}')"
          style="margin-top:8px;width:100%;padding:8px 14px;background:linear-gradient(135deg,#F0EBFF,#E8F4FF);border:2px solid #845EF7;border-radius:12px;font-family:Nunito,sans-serif;font-weight:800;font-size:0.82rem;cursor:pointer;color:#6741D9;text-align:left">
          🔁 Refuerzo ${mat.emoji} ${mat.nombre.split(' ')[0]} · ${erroresGuardados.length} error${erroresGuardados.length>1?'es':''}
        </button>`;
      }
    }"""

NEW5 = """    for (const [key, mat] of Object.entries(MATERIAS)) {
      const numErr = tieneErroresGuardados(dia, key);
      if (numErr > 0 && materiaCompletada(dia, key)) {
        refuerzoHtml += `<button id="btn-refuerzo-${dia}-${key}" onclick="iniciarRefuerzoDesdeMenu(${dia},'${key}')"
          style="margin-top:8px;width:100%;padding:8px 14px;background:linear-gradient(135deg,#F0EBFF,#E8F4FF);border:2px solid #845EF7;border-radius:12px;font-family:Nunito,sans-serif;font-weight:800;font-size:0.82rem;cursor:pointer;color:#6741D9;text-align:left">
          🔁 Refuerzo ${mat.emoji} ${mat.nombre.split(' ')[0]} · ${numErr} error${numErr>1?'es':''}
        </button>`;
      }
    }"""

if OLD5 in html:
    html = html.replace(OLD5, NEW5)
    patches_ok += 1
    print("  ✅ Bonus — renderInicio: usa tieneErroresGuardados()")
    patches_total += 1
else:
    print("  ❌ Bonus — renderInicio bloque refuerzo NO encontrado")

# ══════════════════════════════════════════════════════════════════════════════
# GUARDAR
# ══════════════════════════════════════════════════════════════════════════════
if html != original:
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\n{'='*55}")
    print(f"  {patches_ok}/{patches_total} patches aplicados ✅")
    print(f"  index.html guardado.")
    if patches_ok < patches_total:
        print(f"  ⚠️  {patches_total - patches_ok} patch(es) fallaron — revisa los OLD strings.")
    print(f"{'='*55}")
else:
    print("\n⚠️  Sin cambios. Verifica que el index.html sea el correcto.")
