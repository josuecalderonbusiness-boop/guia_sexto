"""
fix_boton_cargando.py
Soluciona el botón "Cargando..." que queda congelado cuando la hoja Errores
no existe o el fetch falla. También mejora la UX del refuerzo desde menú.

Ejecutar: python fix_boton_cargando.py
Resultado esperado: 3/3 patches aplicados ✅
"""

import os

BASE  = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, 'index.html')

patches_ok = 0
patches_total = 3

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 1 — renderInicio: los botones de refuerzo NO muestran "Cargando..."
# en el renderizado inicial. El texto correcto se pone desde Sheets
# después de cargar. Ahora el botón muestra el conteo desde localStorage
# y al hacer clic busca en Sheets si localStorage falla.
# 
# Problema: el id="btn-refuerzo-${dia}-${key}" funciona pero cuando
# iniciarRefuerzoDesdeMenu falla, el btnEl.disabled = false no se ejecuta
# porque el catch no lo restaura bien.
# Solución: envolver toda la lógica en try/finally para garantizar restauración.
# ══════════════════════════════════════════════════════════════════════════════

OLD1 = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
  const key = `errores_${dia}_${materia}`;

  // 1. Intentar desde localStorage primero (más rápido)
  const erroresRaw = JSON.parse(localStorage.getItem(key) || '[]');
  const erroresLocal = erroresRaw.filter(e => e?.pregunta?.opciones?.A !== undefined);

  if (erroresLocal.length > 0) {
    arrancarRefuerzo(dia, materia, erroresLocal, null);
    return;
  }

  // 2. Si no hay local, buscar en Sheets (otro dispositivo guardó los errores)
  if (!estado.codigo) {
    alert('Inicia sesión para cargar el refuerzo desde cualquier dispositivo.');
    return;
  }

  // Mostrar indicador de carga en el botón
  const btnId = `btn-refuerzo-${dia}-${materia}`;
  const btnEl = document.getElementById(btnId);
  const textoOriginal = btnEl ? btnEl.textContent : '';
  if (btnEl) { btnEl.textContent = '⏳ Cargando...'; btnEl.disabled = true; }

  try {
    const res = await fetch(
      `/api/errores?codigo=${encodeURIComponent(estado.codigo)}&dia=${dia}&materia=${materia}`
    );
    const data = await res.json();

    if (data.ok && data.errores && data.errores.length > 0) {
      const erroresSheets = data.errores.filter(e => e?.pregunta?.opciones?.A !== undefined);
      if (erroresSheets.length > 0) {
        // Guardar en localStorage para próxima vez (caché)
        localStorage.setItem(key, JSON.stringify(erroresSheets));
        arrancarRefuerzo(dia, materia, erroresSheets, null);
        return;
      }
    }

    // 3. No hay errores en ningún lado
    if (btnEl) { btnEl.textContent = textoOriginal; btnEl.disabled = false; }
    alert('No hay errores guardados para este refuerzo. Haz el examen primero en este u otro dispositivo.');
  } catch(e) {
    if (btnEl) { btnEl.textContent = textoOriginal; btnEl.disabled = false; }
    alert('Error de conexión al cargar el refuerzo. Revisa el internet e intenta de nuevo.');
  }
}"""

NEW1 = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
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
    alert('Aún no hay errores guardados en la nube para este refuerzo.\n¿Ya hiciste este examen en el otro dispositivo? Asegúrate de que tenga internet al terminar.');

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

if OLD1 in html:
    html = html.replace(OLD1, NEW1)
    patches_ok += 1
    print("  ✅ Patch 1/3 — iniciarRefuerzoDesdeMenu: try/finally garantiza restauración del botón")
else:
    print("  ❌ Patch 1/3 — NO encontrado. ¿Ya aplicaste fix_errores_multidispositivo.py?")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 2 — sincronizarBotonesRefuerzoDesdeSheets: no bloquear render inicial
# El problema es que se llama en sincronizarCompletadosDesdeSheets() pero si
# la hoja Errores no existe lanza excepción y deja cosas en mal estado.
# Ahora es completamente silenciosa y tolerante a fallos.
# ══════════════════════════════════════════════════════════════════════════════

OLD2 = """// Detectar qué materias/días tienen errores en Sheets y actualizar localStorage
async function sincronizarBotonesRefuerzoDesdeSheets() {
  if (!estado.codigo) return;
  try {
    const res = await fetch(`/api/errores?codigo=${encodeURIComponent(estado.codigo)}&todos=1`);
    if (!res.ok) return;
    const data = await res.json();
    if (!data.ok || !data.entradas) return;
    // Guardar en localStorage para que renderInicio los muestre
    data.entradas.forEach(e => {
      if (e.errores && e.errores.length > 0) {
        const key = `errores_${e.dia}_${e.materia}`;
        const existentes = JSON.parse(localStorage.getItem(key) || '[]');
        // Solo actualizar si localStorage está vacío (para no pisar datos frescos)
        if (existentes.length === 0) {
          localStorage.setItem(key, JSON.stringify(e.errores));
        }
      }
    });
  } catch(e) {}
}"""

NEW2 = """// Sincronizar errores desde Sheets a localStorage (silencioso, segundo plano)
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

if OLD2 in html:
    html = html.replace(OLD2, NEW2)
    patches_ok += 1
    print("  ✅ Patch 2/3 — sincronizarBotonesRefuerzoDesdeSheets: tolerante a hoja inexistente + re-render si hay datos nuevos")
else:
    print("  ❌ Patch 2/3 — NO encontrado")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 3 — meta versión
# ══════════════════════════════════════════════════════════════════════════════
OLD3 = '<meta name="version" content="errores-multidispositivo-v2"/>'
NEW3 = '<meta name="version" content="errores-multidispositivo-v3"/>'

if OLD3 in html:
    html = html.replace(OLD3, NEW3)
    patches_ok += 1
    print("  ✅ Patch 3/3 — versión actualizada a v3")
else:
    print("  ❌ Patch 3/3 — NO encontrado")

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
        print(f"  ⚠️  {patches_total - patches_ok} patch(es) fallaron.")
        print(f"  Asegúrate de haber corrido fix_errores_multidispositivo.py primero.")
    print(f"{'='*55}")
else:
    print("\n⚠️  Sin cambios. Verifica que el index.html sea el correcto.")
