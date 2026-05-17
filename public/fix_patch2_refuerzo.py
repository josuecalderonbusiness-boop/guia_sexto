"""
fix_patch2_refuerzo.py
Reemplaza iniciarRefuerzoDesdeMenu con la version que usa cargarErroresDesdeResultados.
Ejecutar: python fix_patch2_refuerzo.py
Resultado esperado: 1/1 patches aplicados
"""

import os

BASE  = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, 'index.html')

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

original = html

OLD = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
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
      if (validos.length > 0) {"""

if OLD not in html:
    # Buscar con regex por si hay pequeñas diferencias de espaciado
    import re
    # Buscar desde la declaración hasta un punto identificable
    m = re.search(r'async function iniciarRefuerzoDesdeMenu\(dia, materia\) \{.*?if \(validos\.length > 0\) \{', html, re.DOTALL)
    if m:
        print(f"  ⚠️  Encontrado via regex en pos {m.start()}-{m.end()}")
        print(f"  Texto encontrado (primeros 200 chars):")
        print(f"  {repr(html[m.start():m.start()+200])}")
    else:
        print("  ❌ No se encontró la función. Mostrando contexto cerca de 'iniciarRefuerzoDesdeMenu':")
        idx = html.find('async function iniciarRefuerzoDesdeMenu')
        if idx >= 0:
            print(repr(html[idx:idx+800]))
        else:
            print("  ❌ Función no encontrada en absoluto.")
    exit(1)

# Encontrar el final de la función buscando el cierre correcto
start = html.find('async function iniciarRefuerzoDesdeMenu(dia, materia) {')
if start < 0:
    print("❌ No se encontró la función")
    exit(1)

# Encontrar el fin de la función contando llaves
depth = 0
end = start
i = start
while i < len(html):
    if html[i] == '{':
        depth += 1
    elif html[i] == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            break
    i += 1

funcion_actual = html[start:end]
print(f"  Función encontrada: {len(funcion_actual)} chars, líneas {html[:start].count(chr(10))+1} a {html[:end].count(chr(10))+1}")

NEW = """async function iniciarRefuerzoDesdeMenu(dia, materia) {
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

html = html[:start] + NEW + html[end:]

with open(INDEX, 'w', encoding='utf-8') as f:
    f.write(html)

print("  ✅ Patch 1/1 — iniciarRefuerzoDesdeMenu reemplazada correctamente")
print(f"\n{'='*50}")
print(f"  1/1 patches aplicados ✅")
print(f"  index.html guardado.")
print(f"{'='*50}")
