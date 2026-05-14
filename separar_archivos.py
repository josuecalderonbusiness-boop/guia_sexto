import os, re

base = os.path.dirname(os.path.abspath(__file__))
html_path  = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'style.css')
js_path    = os.path.join(base, 'script.js')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

patches = []
applied = 0

# ─────────────────────────────────────────────
# PATCH 1 – Extraer CSS y crear style.css
# ─────────────────────────────────────────────
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if css_match:
    css_content = css_match.group(1).strip()
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write('/* ============================================================\n')
        f.write('   Guía de Estudio – Grado Sexto | Monterrosales Homeschool\n')
        f.write('   style.css – Todos los estilos del sitio\n')
        f.write('============================================================ */\n\n')
        f.write(css_content)
        f.write('\n')
    print(f'✅ Patch 1 – style.css creado ({len(css_content.splitlines())} líneas)')
    applied += 1

    # Reemplazar bloque <style>...</style> con <link>
    old_style = css_match.group(0)
    new_style  = '<link rel="stylesheet" href="style.css">'
    html = html.replace(old_style, new_style, 1)
else:
    print('⚠️  Patch 1 – No se encontró bloque <style>')

# ─────────────────────────────────────────────
# PATCH 2 – Extraer JS y crear script.js
# ─────────────────────────────────────────────
js_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if js_match:
    js_content = js_match.group(1).strip()
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write('// ============================================================\n')
        f.write('//  Guía de Estudio – Grado Sexto | Monterrosales Homeschool\n')
        f.write('//  script.js – Navegación + Motor de calificación de simulacros\n')
        f.write('// ============================================================\n\n')
        f.write(js_content)
        f.write('\n')
    print(f'✅ Patch 2 – script.js creado ({len(js_content.splitlines())} líneas)')
    applied += 1

    # Reemplazar bloque <script>...</script> con <script src="">
    old_script = js_match.group(0)
    new_script  = '<script src="script.js"></script>'
    html = html.replace(old_script, new_script, 1)
else:
    print('⚠️  Patch 2 – No se encontró bloque <script>')

# ─────────────────────────────────────────────
# PATCH 3 – Guardar index.html limpio
# ─────────────────────────────────────────────
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

lines_html = len(html.splitlines())
print(f'✅ Patch 3 – index.html actualizado ({lines_html} líneas)')
applied += 1

# ─────────────────────────────────────────────
# Resumen
# ─────────────────────────────────────────────
print(f'\n{applied}/3 ✅')
print(f'\nArchivos generados:')
print(f'  📄 index.html  → {os.path.getsize(html_path):,} bytes')
if os.path.exists(css_path):
    print(f'  🎨 style.css   → {os.path.getsize(css_path):,} bytes')
if os.path.exists(js_path):
    print(f'  ⚙️  script.js   → {os.path.getsize(js_path):,} bytes')
print('\n¡Listo! Haz git add . → git commit → git push')
