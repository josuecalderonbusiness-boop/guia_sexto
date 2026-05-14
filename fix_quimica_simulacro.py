import os

base = os.path.dirname(os.path.abspath(__file__))

paths = {
    'html': os.path.join(base, 'index.html'),
    'css':  os.path.join(base, 'style.css'),
    'js':   os.path.join(base, 'script.js'),
}

data = {}
for k, p in paths.items():
    with open(p, 'r', encoding='utf-8') as f:
        data[k] = f.read()

patches = []   # (old, new, file_key, descripcion)
applied = 0

def px(old, new, fk, desc):
    patches.append((old, new, fk, desc))

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 1 — CSS: nuevos tipos de pregunta (style.css)
# ══════════════════════════════════════════════════════════════════════════════
px(
  '  /* grid for visual items */',
  '''  /* ===== NUEVOS TIPOS DE PREGUNTA (simulacros) ===== */

  /* Badges de tipo */
  .q-type-badge {
    display:inline-block; font-size:0.68rem; font-weight:800;
    padding:0.13rem 0.55rem; border-radius:20px; margin-bottom:0.45rem;
    letter-spacing:0.5px; text-transform:uppercase;
  }
  .badge-tf    { background:#f0fdf4; color:#166534; border:1.5px solid #86efac; }
  .badge-text  { background:#fdf4ff; color:#6b21a8; border:1.5px solid #d8b4fe; }
  .badge-graph { background:#eff6ff; color:#1e40af; border:1.5px solid #93c5fd; }
  .badge-trap  { background:#fff7ed; color:#9a3412; border:1.5px solid #fdba74; }

  /* Verdadero / Falso */
  .options.tf-opts { display:flex; gap:0.8rem; flex-wrap:wrap; }
  .options.tf-opts label {
    flex:1; min-width:120px; margin-bottom:0 !important;
    border:none !important; padding:0 !important; background:none !important;
  }
  .options.tf-opts input[type="radio"] { display:none; }
  .tf-btn {
    display:block; text-align:center; padding:0.85rem 0.5rem;
    border-radius:12px; cursor:pointer; font-weight:900; font-size:1rem;
    border:3px solid; transition:all 0.2s; user-select:none;
  }
  .tf-btn-v { border-color:#27ae60; color:#27ae60; background:#f0fdf4; }
  .tf-btn-f { border-color:#e74c3c; color:#e74c3c; background:#fff5f5; }
  .options.tf-opts input[type="radio"]:checked + .tf-btn-v { background:#27ae60; color:white; }
  .options.tf-opts input[type="radio"]:checked + .tf-btn-f { background:#e74c3c; color:white; }

  /* Texto pasaje */
  .text-passage {
    background:#fafaf9; border-left:4px solid var(--accent);
    padding:0.85rem 1.1rem; border-radius:0 10px 10px 0;
    margin-bottom:0.9rem; font-size:0.88rem; line-height:1.85;
    color:#374151; font-style:italic;
  }
  .text-passage strong { font-style:normal; color:#1a202c; }

  /* Gráfico SVG */
  .q-graphic {
    background:white; border:2px solid var(--border);
    border-radius:12px; padding:0.9rem 0.4rem; margin-bottom:0.9rem;
    text-align:center; overflow-x:auto;
  }
  .q-graphic svg { max-width:100%; height:auto; display:inline-block; }
  .q-graphic figcaption {
    font-size:0.75rem; color:#6b7280; margin-top:0.35rem; font-style:italic;
  }

  /* El intruso — cuadrícula 2×2 */
  .options.intruso-opts {
    display:grid; grid-template-columns:1fr 1fr; gap:0.7rem;
  }
  .options.intruso-opts label {
    border-radius:12px !important; text-align:center !important;
    padding:1rem 0.6rem !important; font-weight:700 !important;
    justify-content:center !important; cursor:pointer;
  }

  /* grid for visual items */''',
  'css',
  'CSS nuevos tipos de pregunta'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 2 — Q14: Verdadero / Falso
# El H₂O como mezcla → FALSO (es un compuesto)
# ══════════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 14</div>
        <div class="q-text">600 g son equivalentes a:</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="q14" value="a"> 0.6 kg</label>
          <label><input type="radio" name="q14" value="b"> 6 kg</label>
          <label><input type="radio" name="q14" value="c"> 60 kg</label>
          <label><input type="radio" name="q14" value="d"> 0.06 kg</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 14</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">El agua pura (H₂O) es una <strong>mezcla homogénea</strong>, porque está formada por diferentes sustancias mezcladas de forma uniforme.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q14" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q14" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html',
  'Q14 → T/F: H₂O es mezcla homogénea'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 3 — Q15: Lectura + MCQ
# Cambios de estado — respuesta: c) Condensación
# ══════════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 15</div>
        <div class="q-text">¿Cuál de estos elementos SÍ forma molécula diatómica?</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="q15" value="a"> Sodio (Na)</label>
          <label><input type="radio" name="q15" value="b"> Calcio (Ca)</label>
          <label><input type="radio" name="q15" value="c"> Hierro (Fe)</label>
          <label><input type="radio" name="q15" value="d"> Cloro (Cl)</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 15</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          En el laboratorio, una estudiante calienta agua en un vaso de precipitados. Observa que al aumentar la temperatura el agua burbujea y se convierte en vapor. Luego apaga el mechero y acerca un vidrio frío a la boca del recipiente: el vapor que toca el vidrio vuelve inmediatamente a su estado <strong>líquido</strong>, formando pequeñas gotas.
        </div>
        <div class="q-text">Según el texto, ¿qué cambio de estado ocurre cuando el vapor toca el vidrio frío?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q15" value="a"> Evaporación</label>
          <label><input type="radio" name="q15" value="b"> Fusión</label>
          <label><input type="radio" name="q15" value="c"> Condensación</label>
          <label><input type="radio" name="q15" value="d"> Sublimación</label>
        </div>
      </div>''',
  'html',
  'Q15 → Texto corto + MCQ cambios de estado'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 4 — Q16: Gráfico SVG — Modelo de Bohr (Sodio, 11e)
# Respuesta: c) 11
# ══════════════════════════════════════════════════════════════════════════════
SVG_BOHR = '''<svg viewBox="0 0 220 220" style="max-width:210px;font-family:sans-serif;">
  <circle cx="110" cy="110" r="22" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
  <text x="110" y="116" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">Na</text>
  <circle cx="110" cy="110" r="38" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5,3"/>
  <circle cx="110" cy="72" r="6" fill="#2563eb"/>
  <circle cx="110" cy="148" r="6" fill="#2563eb"/>
  <text x="152" y="90" font-size="9" fill="#2563eb">2 e⁻</text>
  <circle cx="110" cy="110" r="68" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5,3"/>
  <circle cx="178" cy="110" r="6" fill="#2563eb"/>
  <circle cx="158" cy="158" r="6" fill="#2563eb"/>
  <circle cx="110" cy="178" r="6" fill="#2563eb"/>
  <circle cx="62"  cy="158" r="6" fill="#2563eb"/>
  <circle cx="42"  cy="110" r="6" fill="#2563eb"/>
  <circle cx="62"  cy="62"  r="6" fill="#2563eb"/>
  <circle cx="110" cy="42"  r="6" fill="#2563eb"/>
  <circle cx="158" cy="62"  r="6" fill="#2563eb"/>
  <text x="15" y="104" font-size="9" fill="#2563eb">8 e⁻</text>
  <circle cx="110" cy="110" r="95" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5,3"/>
  <circle cx="110" cy="15"  r="7"  fill="#dc2626" stroke="#991b1b" stroke-width="1.5"/>
  <text x="122" y="20" font-size="9" fill="#dc2626" font-weight="bold">1 e⁻</text>
</svg>'''

px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 16</div>
        <div class="q-text">En la fórmula CO₂ hay ___carbono(s) y ___ oxígeno(s).</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q16" value="a"> 2 y 1</label>
          <label><input type="radio" name="q16" value="b"> 1 y 2</label>
          <label><input type="radio" name="q16" value="c"> 2 y 2</label>
          <label><input type="radio" name="q16" value="d"> 1 y 1</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 16</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_BOHR + '''
          <figcaption>Modelo de Bohr — cada punto azul es un electrón; el punto rojo es el electrón de la capa exterior</figcaption>
        </div>
        <div class="q-text">Según el modelo atómico representado, ¿cuántos electrones tiene este átomo en total?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q16" value="a"> 9</label>
          <label><input type="radio" name="q16" value="b"> 10</label>
          <label><input type="radio" name="q16" value="c"> 11</label>
          <label><input type="radio" name="q16" value="d"> 12</label>
        </div>
      </div>''',
  'html',
  'Q16 → SVG Modelo de Bohr (Sodio)'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 5 — Q17: Verdadero / Falso
# Ley de Lavoisier mal enunciada → FALSO
# ══════════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 17</div>
        <div class="q-text">¿Por qué los gases nobles casi no reaccionan con otros elementos?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q17" value="a"> Porque son muy pesados</label>
          <label><input type="radio" name="q17" value="b"> Porque no tienen átomos</label>
          <label><input type="radio" name="q17" value="c"> Porque tienen su última capa de electrones completa</label>
          <label><input type="radio" name="q17" value="d"> Porque están en estado sólido</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 17</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">Según la Ley de Lavoisier, en una reacción química la masa total de los <strong>productos</strong> es siempre <strong>mayor</strong> que la masa total de los reactivos.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q17" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q17" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html',
  'Q17 → T/F: Ley de Lavoisier mal enunciada'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 6 — Q18: El intruso (cuadrícula 2×2)
# ¿Cuál es la ÚNICA mezcla heterogénea? → c) Ensalada
# ══════════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 18</div>
        <div class="q-text">¿Cuál es el mayor aporte de Dalton a la ciencia?</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="q18" value="a"> Proponer que la materia está formada por átomos</label>
          <label><input type="radio" name="q18" value="b"> Descubrir el electrón</label>
          <label><input type="radio" name="q18" value="c"> Descubrir el oxígeno</label>
          <label><input type="radio" name="q18" value="d"> Crear la Tabla Periódica</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 18</div>
        <span class="q-type-badge badge-trap">🔍 Encuentra al intruso</span>
        <div class="q-text">Tres de las siguientes son <strong>mezclas homogéneas</strong>. ¿Cuál es la ÚNICA mezcla <strong>heterogénea</strong>?</div>
        <div class="options intruso-opts" data-correct="c">
          <label><input type="radio" name="q18" value="a"> 🧂 Agua con sal</label>
          <label><input type="radio" name="q18" value="b"> 🍹 Limonada</label>
          <label><input type="radio" name="q18" value="c"> 🥗 Ensalada</label>
          <label><input type="radio" name="q18" value="d"> 🍷 Agua con vinagre</label>
        </div>
      </div>''',
  'html',
  'Q18 → El intruso 2×2: mezcla heterogénea'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 7 — Q19: Gráfico SVG — fragmento Tabla Periódica
# Gases nobles = Grupo 18 → respuesta c)
# ══════════════════════════════════════════════════════════════════════════════
SVG_TABLA = '''<svg viewBox="0 0 280 145" style="max-width:100%;font-family:sans-serif;">
  <text x="47"  y="14" text-anchor="middle" font-size="9.5" fill="#6b7280">Grupo 1</text>
  <text x="142" y="14" text-anchor="middle" font-size="9.5" fill="#6b7280">Grupo 17</text>
  <text x="232" y="14" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#dc2626">Grupo 18 ★</text>
  <rect x="10"  y="18" width="74" height="32" rx="6" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.5"/>
  <text x="47"  y="31" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">H</text>
  <text x="47"  y="43" text-anchor="middle" font-size="8"  fill="#374151">Hidrógeno</text>
  <rect x="193" y="18" width="78" height="32" rx="6" fill="#fee2e2" stroke="#f87171" stroke-width="2"/>
  <text x="232" y="31" text-anchor="middle" font-size="13" font-weight="bold" fill="#dc2626">He</text>
  <text x="232" y="43" text-anchor="middle" font-size="8"  fill="#374151">Helio</text>
  <rect x="10"  y="55" width="74" height="32" rx="6" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.5"/>
  <text x="47"  y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Li</text>
  <text x="47"  y="80" text-anchor="middle" font-size="8"  fill="#374151">Litio</text>
  <rect x="104" y="55" width="74" height="32" rx="6" fill="#fef9c3" stroke="#fde047" stroke-width="1.5"/>
  <text x="141" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">F</text>
  <text x="141" y="80" text-anchor="middle" font-size="8"  fill="#374151">Flúor</text>
  <rect x="193" y="55" width="78" height="32" rx="6" fill="#fee2e2" stroke="#f87171" stroke-width="2"/>
  <text x="232" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#dc2626">Ne</text>
  <text x="232" y="80" text-anchor="middle" font-size="8"  fill="#374151">Neón</text>
  <rect x="10"  y="92" width="74" height="32" rx="6" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.5"/>
  <text x="47"  y="105" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Na</text>
  <text x="47"  y="117" text-anchor="middle" font-size="8"  fill="#374151">Sodio</text>
  <rect x="104" y="92" width="74" height="32" rx="6" fill="#fef9c3" stroke="#fde047" stroke-width="1.5"/>
  <text x="141" y="105" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">Cl</text>
  <text x="141" y="117" text-anchor="middle" font-size="8"  fill="#374151">Cloro</text>
  <rect x="193" y="92" width="78" height="32" rx="6" fill="#fee2e2" stroke="#f87171" stroke-width="2"/>
  <text x="232" y="105" text-anchor="middle" font-size="13" font-weight="bold" fill="#dc2626">Ar</text>
  <text x="232" y="117" text-anchor="middle" font-size="8"  fill="#374151">Argón</text>
  <text x="10" y="140" font-size="8.5" fill="#dc2626" font-weight="bold">★ Gases Nobles — capa exterior completa, casi no reaccionan</text>
</svg>'''

px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 19</div>
        <div class="q-text">¿Cuál es el solvente más universal en la naturaleza?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q19" value="a"> El alcohol</label>
          <label><input type="radio" name="q19" value="b"> El agua</label>
          <label><input type="radio" name="q19" value="c"> El vinagre</label>
          <label><input type="radio" name="q19" value="d"> La gasolina</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 19</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_TABLA + '''
          <figcaption>Fragmento simplificado de la Tabla Periódica (Períodos 1–3)</figcaption>
        </div>
        <div class="q-text">Según el fragmento, ¿en qué grupo se ubican los gases nobles?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q19" value="a"> Grupo 1</label>
          <label><input type="radio" name="q19" value="b"> Grupo 17</label>
          <label><input type="radio" name="q19" value="c"> Grupo 18</label>
          <label><input type="radio" name="q19" value="d"> Grupo 2</label>
        </div>
      </div>''',
  'html',
  'Q19 → SVG fragmento Tabla Periódica'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 8 — Q20: Verdadero / Falso
# Descripción del modelo de Thomson confundida con Rutherford → FALSO
# ══════════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 20</div>
        <div class="q-text">El plasma es un estado de la materia que se encuentra en:</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="q20" value="a"> El hielo</label>
          <label><input type="radio" name="q20" value="b"> El vapor de agua</label>
          <label><input type="radio" name="q20" value="c"> El aceite</label>
          <label><input type="radio" name="q20" value="d"> El Sol y los rayos eléctricos</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 20</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">El modelo atómico de <strong>Rutherford</strong> propuso que los electrones están distribuidos uniformemente dentro del átomo, como pasas en un pudín.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q20" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q20" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html',
  'Q20 → T/F: modelo de Rutherford vs Thomson'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 9 — JS: actualizar correctAnswers para química q14-q20
# ══════════════════════════════════════════════════════════════════════════════
px(
  "      q11:'d',q12:'c',q13:'b',q14:'a',q15:'d',q16:'b',q17:'c',q18:'a',q19:'b',q20:'d'",
  "      q11:'d',q12:'c',q13:'b',q14:'f',q15:'c',q16:'c',q17:'f',q18:'c',q19:'c',q20:'f'",
  'js',
  'JS correctAnswers quimica q14-q20'
)

# ══════════════════════════════════════════════════════════════════════════════
# PATCH 10 — JS: añadir labelAns() y mejorar feedback T/F
# ══════════════════════════════════════════════════════════════════════════════
px(
  '  function gradeQuiz(subject) {',
  '''  function labelAns(a) {
    if (a === 'v') return 'VERDADERO';
    if (a === 'f') return 'FALSO';
    return a.toUpperCase().split('').join(', ');
  }

  function gradeQuiz(subject) {''',
  'js',
  'JS añadir labelAns helper'
)

px(
  "        const correctLetters = correctAns.toUpperCase().split('').join(', ');\n        feedbackHTML += `<div class=\"result-item\"><span class=\"wrong-ans\">\u274c P${idx+1}:</span> Tu respuesta: ${userAns ? userAns.toUpperCase() : 'Sin respuesta'} \u2014 Correcta: <strong>${correctLetters}</strong></div>`;",
  "        feedbackHTML += `<div class=\"result-item\"><span class=\"wrong-ans\">\u274c P${idx+1}:</span> Tu respuesta: ${userAns ? labelAns(userAns) : 'Sin respuesta'} \u2014 Correcta: <strong>${labelAns(correctAns)}</strong></div>`;",
  'js',
  'JS mejorar feedback con labelAns'
)

# ══════════════════════════════════════════════════════════════════════════════
# Aplicar todos los patches
# ══════════════════════════════════════════════════════════════════════════════
total = len(patches)
for i, (old, new, fk, desc) in enumerate(patches, 1):
    if old in data[fk]:
        data[fk] = data[fk].replace(old, new, 1)
        applied += 1
        print(f'  ✅ Patch {i:02d}/{total} — {desc}')
    else:
        print(f'  ⚠️  Patch {i:02d}/{total} NO encontrado — {desc}')
        print(f'         Buscando en {fk}: "{old[:60].strip()}..."')

for k, p in paths.items():
    with open(p, 'w', encoding='utf-8') as f:
        f.write(data[k])

print(f'\n{"="*50}')
print(f'{applied}/{total} {"✅  Todo aplicado" if applied == total else "⚠️  Revisa los fallidos"}')
print(f'\nCambios en Química:')
print(f'  Q14 → ✓✗ V/F    : H₂O ¿es mezcla? → FALSO')
print(f'  Q15 → 📄 Lectura : cambios de estado → Condensación (c)')
print(f'  Q16 → 📊 Gráfico : Modelo Bohr Sodio → 11 e⁻ (c)')
print(f'  Q17 → ✓✗ V/F    : Lavoisier mal enunciada → FALSO')
print(f'  Q18 → 🔍 Intruso : mezcla heterogénea → Ensalada (c)')
print(f'  Q19 → 📊 Gráfico : Tabla Periódica → Grupo 18 (c)')
print(f'  Q20 → ✓✗ V/F    : Rutherford vs Thomson → FALSO')
print(f'\nHaz: git add . → git commit -m "Química: nuevos tipos de pregunta" → git push')
