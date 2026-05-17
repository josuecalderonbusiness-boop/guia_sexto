"""
fix_errores_multidispositivo.py
Parchea index.html para que los errores de refuerzo se guarden en Google Sheets
y funcionen en cualquier dispositivo (no solo localStorage).

Ejecutar: python fix_errores_multidispositivo.py
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, 'index.html')

patches_ok = 0
patches_total = 6

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

original = html  # para comparar al final

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 1 — terminarExamen: guardar errores en Sheets + localStorage
# Reemplaza: localStorage.setItem(`errores_${dia}_${materia}`, ...)
# ══════════════════════════════════════════════════════════════════════════════
OLD1 = "  localStorage.setItem(`errores_${dia}_${materia}`, JSON.stringify(erroresParaRefuerzo));"

NEW1 = """  // Guardar errores localmente (fallback)
  localStorage.setItem(`errores_${dia}_${materia}`, JSON.stringify(erroresParaRefuerzo));
  // Guardar errores en Sheets para acceso multi-dispositivo
  if (estado.codigo && erroresParaRefuerzo.length > 0) {
    fetch('/api/errores', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        codigo: estado.codigo,
        dia,
        materia,
        errores: erroresParaRefuerzo
      })
    }).catch(() => {});
  } else if (estado.codigo && erroresParaRefuerzo.length === 0) {
    // Sin errores: borrar entrada previa en Sheets si existe
    fetch(`/api/errores?codigo=${encodeURIComponent(estado.codigo)}&dia=${dia}&materia=${materia}`, {
      method: 'DELETE'
    }).catch(() => {});
  }"""

if OLD1 in html:
    html = html.replace(OLD1, NEW1)
    patches_ok += 1
    print(f"  ✅ Patch 1/6 — terminarExamen: guardar errores en Sheets")
else:
    print(f"  ❌ Patch 1/6 — NO encontrado (revisar OLD1)")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 2 — terminarRefuerzo: limpiar errores en Sheets cuando completa 100%
# Reemplaza: if (puntaje === total) { localStorage.removeItem(...) }
# ══════════════════════════════════════════════════════════════════════════════
OLD2 = "  // Si mejoró todos, limpiar errores guardados\n  if (puntaje === total) {\n    localStorage.removeItem(`errores_${dia}_${materia}`);\n  }"

NEW2 = """  // Si mejoró todos, limpiar errores guardados
  if (puntaje === total) {
    localStorage.removeItem(`errores_${dia}_${materia}`);
    // Borrar en Sheets también
    if (estado.codigo) {
      fetch(`/api/errores?codigo=${encodeURIComponent(estado.codigo)}&dia=${dia}&materia=${encodeURIComponent(materia)}`, {
        method: 'DELETE'
      }).catch(() => {});
    }
  }"""

if OLD2 in html:
    html = html.replace(OLD2, NEW2)
    patches_ok += 1
    print(f"  ✅ Patch 2/6 — terminarRefuerzo: limpiar errores en Sheets")
else:
    print(f"  ❌ Patch 2/6 — NO encontrado (revisar OLD2)")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 3 — iniciarRefuerzoDesdeMenu: cargar errores desde Sheets si no hay local
# Reemplaza la función completa iniciarRefuerzoDesdeMenu
# ══════════════════════════════════════════════════════════════════════════════
OLD3 = """function iniciarRefuerzoDesdeMenu(dia, materia) {
  const key = `errores_${dia}_${materia}`;
  const erroresRaw = JSON.parse(localStorage.getItem(key) || '[]');
  const errores = erroresRaw.filter(e => e?.pregunta?.opciones?.A !== undefined);
if (!errores.length) { localStorage.removeItem(key); alert('Datos desactualizados. Haz el examen de nuevo.'); return; }
  arrancarRefuerzo(dia, materia, errores, null);
}"""

NEW3 = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
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

if OLD3 in html:
    html = html.replace(OLD3, NEW3)
    patches_ok += 1
    print(f"  ✅ Patch 3/6 — iniciarRefuerzoDesdeMenu: carga desde Sheets como fallback")
else:
    print(f"  ❌ Patch 3/6 — NO encontrado (revisar OLD3)")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 4 — renderInicio: agregar id a los botones de refuerzo para el loader
# Reemplaza la generación del botón de refuerzo en renderInicio
# ══════════════════════════════════════════════════════════════════════════════
OLD4 = """        refuerzoHtml += `<button onclick="iniciarRefuerzoDesdeMenu(${dia},'${key}')"
          style="margin-top:8px;width:100%;padding:8px 14px;background:linear-gradient(135deg,#F0EBFF,#E8F4FF);border:2px solid #845EF7;border-radius:12px;font-family:Nunito,sans-serif;font-weight:800;font-size:0.82rem;cursor:pointer;color:#6741D9;text-align:left">
          🔁 Refuerzo ${mat.emoji} ${mat.nombre.split(' ')[0]} · ${erroresGuardados.length} error${erroresGuardados.length>1?'es':''}
        </button>`;"""

NEW4 = """        refuerzoHtml += `<button id="btn-refuerzo-${dia}-${key}" onclick="iniciarRefuerzoDesdeMenu(${dia},'${key}')"
          style="margin-top:8px;width:100%;padding:8px 14px;background:linear-gradient(135deg,#F0EBFF,#E8F4FF);border:2px solid #845EF7;border-radius:12px;font-family:Nunito,sans-serif;font-weight:800;font-size:0.82rem;cursor:pointer;color:#6741D9;text-align:left">
          🔁 Refuerzo ${mat.emoji} ${mat.nombre.split(' ')[0]} · ${erroresGuardados.length} error${erroresGuardados.length>1?'es':''}
        </button>`;"""

if OLD4 in html:
    html = html.replace(OLD4, NEW4)
    patches_ok += 1
    print(f"  ✅ Patch 4/6 — renderInicio: id en botones de refuerzo")
else:
    print(f"  ❌ Patch 4/6 — NO encontrado (revisar OLD4)")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 5 — sincronizarCompletadosDesdeSheets: también sincronizar botones refuerzo
# Añade llamada a sincronizarBotonesRefuerzo() al final de sincronizarCompletadosDesdeSheets
# ══════════════════════════════════════════════════════════════════════════════
OLD5 = "    guardarEstadoLocal();\n  } catch(e) { console.warn('No se pudo sincronizar completados', e); }\n}"

NEW5 = """    guardarEstadoLocal();
    // Sincronizar botones de refuerzo desde Sheets en segundo plano
    sincronizarBotonesRefuerzoDesdeSheets().catch(() => {});
  } catch(e) { console.warn('No se pudo sincronizar completados', e); }
}

// Detectar qué materias/días tienen errores en Sheets y actualizar localStorage
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

if OLD5 in html:
    html = html.replace(OLD5, NEW5)
    patches_ok += 1
    print(f"  ✅ Patch 5/6 — sincronizarBotonesRefuerzoDesdeSheets: nueva función")
else:
    print(f"  ❌ Patch 5/6 — NO encontrado (revisar OLD5)")

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 6 — vercel.json route: añadir ruta para /api/errores
# Este patch es informativo; vercel.json detecta automáticamente archivos en /api/
# Solo añadimos un comentario en index.html como marcador de versión
# ══════════════════════════════════════════════════════════════════════════════
OLD6 = '<meta name="description" content="Hecho con amor por papá y mamá, para que aprender sea tu aventura favorita. 🧠✨"/>'

NEW6 = '<meta name="description" content="Hecho con amor por papá y mamá, para que aprender sea tu aventura favorita. 🧠✨"/>\n<meta name="version" content="errores-multidispositivo-v2"/>'

if OLD6 in html:
    html = html.replace(OLD6, NEW6)
    patches_ok += 1
    print(f"  ✅ Patch 6/6 — meta versión actualizada")
else:
    print(f"  ❌ Patch 6/6 — NO encontrado (revisar OLD6)")

# ══════════════════════════════════════════════════════════════════════════════
# ESCRIBIR RESULTADO
# ══════════════════════════════════════════════════════════════════════════════
if html != original:
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\n{'='*55}")
    print(f"  {patches_ok}/{patches_total} patches aplicados ✅")
    print(f"  index.html guardado correctamente.")
    if patches_ok < patches_total:
        print(f"  ⚠️  {patches_total - patches_ok} patches fallaron — revisa los OLD strings.")
    print(f"{'='*55}")
else:
    print(f"\n⚠️  No se realizaron cambios. Verifica que el index.html sea el correcto.")
