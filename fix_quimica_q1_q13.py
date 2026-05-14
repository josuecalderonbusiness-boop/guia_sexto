# -*- coding: utf-8 -*-
import os

base = os.path.dirname(os.path.abspath(__file__))
paths = {
    'html': os.path.join(base, 'index.html'),
    'js':   os.path.join(base, 'script.js'),
}
data = {}
for k, p in paths.items():
    with open(p, 'r', encoding='utf-8') as f:
        data[k] = f.read()

patches = []
applied = 0

def px(old, new, fk, desc):
    patches.append((old, new, fk, desc))

# ══════════════════════════════════════════════════════════════════════════
# Q1 → Verdadero / Falso
# Lavoisier padre de la química → VERDADERO
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 1</div>
        <div class="q-text">¿Quién es conocido como el "Padre de la Química"?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q1" value="a"> Isaac Newton</label>
          <label><input type="radio" name="q1" value="b"> Antoine Lavoisier</label>
          <label><input type="radio" name="q1" value="c"> John Dalton</label>
          <label><input type="radio" name="q1" value="d"> Robert Boyle</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 1</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">Antoine Lavoisier es conocido como el "Padre de la Química" porque fue el primero en demostrar experimentalmente que la <strong>materia se conserva</strong> en las reacciones químicas.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q1" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q1" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'Q1 → T/F Lavoisier padre química'
)

# ══════════════════════════════════════════════════════════════════════════
# Q2 → Texto corto + MCQ
# Contexto: laboratorio con balanza en kg, necesita gramos → 2.5 kg
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 2</div>
        <div class="q-text">Si una mochila pesa 3.5 kg, ¿cuántos gramos pesa?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q2" value="a"> 35 g</label>
          <label><input type="radio" name="q2" value="b"> 350 g</label>
          <label><input type="radio" name="q2" value="c"> 3 500 g</label>
          <label><input type="radio" name="q2" value="d"> 35 000 g</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 2</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          En el laboratorio de la escuela, la profesora necesita pesar exactamente <strong>2 500 gramos</strong> de bicarbonato de sodio para un experimento. La única balanza disponible mide en kilogramos.
        </div>
        <div class="q-text">¿Cuántos kilogramos debe marcar la balanza para obtener los 2 500 g que necesita?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q2" value="a"> 25 kg</label>
          <label><input type="radio" name="q2" value="b"> 0.025 kg</label>
          <label><input type="radio" name="q2" value="c"> 2.5 kg</label>
          <label><input type="radio" name="q2" value="d"> 250 kg</label>
        </div>
      </div>''',
  'html', 'Q2 → Texto laboratorio kg/g'
)

# ══════════════════════════════════════════════════════════════════════════
# Q3 → Verdadero / Falso
# Líquido tiene forma fija → FALSO (forma variable, volumen fijo)
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 3</div>
        <div class="q-text">¿Qué estado de la materia tiene forma y volumen FIJOS?</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="q3" value="a"> Sólido</label>
          <label><input type="radio" name="q3" value="b"> Líquido</label>
          <label><input type="radio" name="q3" value="c"> Gaseoso</label>
          <label><input type="radio" name="q3" value="d"> Plasma</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 3</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">El estado <strong>líquido</strong> de la materia tiene <strong>forma fija</strong>, es decir, mantiene su forma independientemente del recipiente que lo contenga.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q3" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q3" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'Q3 → T/F líquido forma fija'
)

# ══════════════════════════════════════════════════════════════════════════
# Q4 → El intruso (2×2 grid)
# Tres sustancias puras, una mezcla → Café con leche
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 4</div>
        <div class="q-text">En la fórmula H₂O, ¿cuántos átomos de hidrógeno hay?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q4" value="a"> 1</label>
          <label><input type="radio" name="q4" value="b"> 2</label>
          <label><input type="radio" name="q4" value="c"> 3</label>
          <label><input type="radio" name="q4" value="d"> 4</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 4</div>
        <span class="q-type-badge badge-trap">🔍 Encuentra al intruso</span>
        <div class="q-text">Tres de las siguientes son <strong>sustancias puras</strong>. ¿Cuál es la única <strong>mezcla</strong>?</div>
        <div class="options intruso-opts" data-correct="c">
          <label><input type="radio" name="q4" value="a"> 💧 Agua destilada (H₂O)</label>
          <label><input type="radio" name="q4" value="b"> 🥇 Oro puro (Au)</label>
          <label><input type="radio" name="q4" value="c"> ☕ Café con leche</label>
          <label><input type="radio" name="q4" value="d"> 🧂 Sal de mesa (NaCl)</label>
        </div>
      </div>''',
  'html', 'Q4 → Intruso sustancia pura vs mezcla'
)

# ══════════════════════════════════════════════════════════════════════════
# Q5 → Gráfico SVG (3 modelos atómicos)
# ¿Cuál tiene núcleo denso positivo central? → C (Rutherford)
# ══════════════════════════════════════════════════════════════════════════
SVG_MODELOS = '''<svg viewBox="0 0 300 115" style="max-width:100%;font-family:sans-serif;">
  <text x="150" y="12" text-anchor="middle" font-size="10" font-weight="bold" fill="#374151">Evolución de los modelos atómicos</text>
  <circle cx="50" cy="60" r="36" fill="#dbeafe" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="50" y="64" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">sólido</text>
  <text x="50" y="104" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#374151">A — Dalton</text>
  <circle cx="150" cy="60" r="36" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="138" cy="50" r="5" fill="#1d4ed8"/><circle cx="162" cy="50" r="5" fill="#1d4ed8"/>
  <circle cx="138" cy="70" r="5" fill="#1d4ed8"/><circle cx="162" cy="70" r="5" fill="#1d4ed8"/>
  <circle cx="150" cy="60" r="5" fill="#1d4ed8"/>
  <text x="150" y="104" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#374151">B — Thomson</text>
  <ellipse cx="250" cy="60" rx="36" ry="22" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>
  <ellipse cx="250" cy="60" rx="18" ry="36" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>
  <circle cx="250" cy="60" r="11" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
  <text x="250" y="64" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">+</text>
  <circle cx="214" cy="60" r="5" fill="#1d4ed8"/>
  <circle cx="286" cy="60" r="5" fill="#1d4ed8"/>
  <circle cx="250" cy="24" r="5" fill="#1d4ed8"/>
  <text x="250" y="104" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#374151">C — Rutherford</text>
</svg>'''

px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 5</div>
        <div class="q-text">¿Cuáles de las siguientes son moléculas diatómicas? (Selecciona todas las correctas)</div>
        <div class="options" data-correct="ac" data-type="multi">
          <label><input type="checkbox" name="q5" value="a"> H₂ (hidrógeno)</label>
          <label><input type="checkbox" name="q5" value="b"> H₂O (agua)</label>
          <label><input type="checkbox" name="q5" value="c"> O₂ (oxígeno)</label>
          <label><input type="checkbox" name="q5" value="d"> CO₂ (dióxido de carbono)</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 5</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_MODELOS + '''
        </div>
        <div class="q-text">¿Cuál de los modelos representó por <strong>primera vez un núcleo denso y positivo</strong> en el centro del átomo?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q5" value="a"> Solo el Modelo A (Dalton)</label>
          <label><input type="radio" name="q5" value="b"> Solo el Modelo B (Thomson)</label>
          <label><input type="radio" name="q5" value="c"> Solo el Modelo C (Rutherford)</label>
          <label><input type="radio" name="q5" value="d"> Los tres modelos por igual</label>
        </div>
      </div>''',
  'html', 'Q5 → SVG modelos atómicos Rutherford'
)

# ══════════════════════════════════════════════════════════════════════════
# Q6 → Verdadero / Falso
# Gases nobles 8e los hace muy reactivos → FALSO (son inertes)
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 6</div>
        <div class="q-text">¿Cuántos electrones de valencia tienen los gases nobles (excepto el Helio)?</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="q6" value="a"> 2</label>
          <label><input type="radio" name="q6" value="b"> 4</label>
          <label><input type="radio" name="q6" value="c"> 6</label>
          <label><input type="radio" name="q6" value="d"> 8</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 6</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">Los gases nobles (excepto el Helio) tienen <strong>8 electrones de valencia</strong>, lo que los hace <strong>muy reactivos</strong> y capaces de formar compuestos fácilmente con otros elementos.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q6" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q6" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'Q6 → T/F gases nobles reactivos'
)

# ══════════════════════════════════════════════════════════════════════════
# Q7 → Texto corto + MCQ
# Dalton: átomos se reorganizan en reacciones → c
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 7</div>
        <div class="q-text">Según la Teoría de Dalton, ¿cómo son los átomos de un mismo elemento?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q7" value="a"> Diferentes entre sí</label>
          <label><input type="radio" name="q7" value="b"> Idénticos entre sí</label>
          <label><input type="radio" name="q7" value="c"> Divisibles en partes más pequeñas</label>
          <label><input type="radio" name="q7" value="d"> Cambian con el tiempo</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 7</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          En 1803, John Dalton propuso que toda la materia está formada por partículas muy pequeñas llamadas átomos, que <strong>no se pueden crear ni destruir</strong>. Los átomos de un mismo elemento son idénticos entre sí. En las reacciones químicas, los átomos no desaparecen: simplemente se <strong>reorganizan</strong> para formar nuevas sustancias.
        </div>
        <div class="q-text">Según el texto, ¿qué les ocurre a los átomos durante una reacción química?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q7" value="a"> Se crean nuevos átomos según se necesiten</label>
          <label><input type="radio" name="q7" value="b"> Algunos átomos desaparecen al reaccionar</label>
          <label><input type="radio" name="q7" value="c"> Se reorganizan sin crearse ni destruirse</label>
          <label><input type="radio" name="q7" value="d"> Cambian de un elemento a otro</label>
        </div>
      </div>''',
  'html', 'Q7 → Texto Dalton átomos reacción'
)

# ══════════════════════════════════════════════════════════════════════════
# Q8 → El intruso (2×2 grid)
# Tres son propiedades de mezclas; una es de compuesto → b (enlaces químicos)
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 8</div>
        <div class="q-text">En una solución de agua con azúcar: el azúcar es el ___ y el agua es el ___.</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="q8" value="a"> soluto / solvente</label>
          <label><input type="radio" name="q8" value="b"> solvente / soluto</label>
          <label><input type="radio" name="q8" value="c"> soluto / soluto</label>
          <label><input type="radio" name="q8" value="d"> solvente / solvente</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 8</div>
        <span class="q-type-badge badge-trap">🔍 Encuentra al intruso</span>
        <div class="q-text">Tres de las siguientes son características de las <strong>mezclas</strong>. ¿Cuál <strong>NO</strong> corresponde a una mezcla?</div>
        <div class="options intruso-opts" data-correct="b">
          <label><input type="radio" name="q8" value="a"> 🔀 Sus componentes conservan sus propiedades originales</label>
          <label><input type="radio" name="q8" value="b"> ⚗️ Sus componentes se unen mediante enlaces químicos fijos</label>
          <label><input type="radio" name="q8" value="c"> 🔍 Se puede separar por métodos físicos (filtración, evaporación)</label>
          <label><input type="radio" name="q8" value="d"> 📊 Su composición puede variar en proporciones</label>
        </div>
      </div>''',
  'html', 'Q8 → Intruso propiedades mezclas'
)

# ══════════════════════════════════════════════════════════════════════════
# Q9 → Verdadero / Falso
# Thomson descubrió electrón con rayos catódicos carga negativa → VERDADERO
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 9</div>
        <div class="q-text">¿Qué descubrió J.J. Thomson en su experimento con tubos de rayos catódicos?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q9" value="a"> El núcleo atómico</label>
          <label><input type="radio" name="q9" value="b"> El protón</label>
          <label><input type="radio" name="q9" value="c"> El electrón</label>
          <label><input type="radio" name="q9" value="d"> El neutrón</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 9</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">J.J. Thomson descubrió el <strong>electrón</strong> al demostrar que los tubos de rayos catódicos emitían partículas de <strong>carga negativa</strong>, independientemente del material usado en el tubo.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q9" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q9" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'Q9 → T/F Thomson electrón'
)

# ══════════════════════════════════════════════════════════════════════════
# Q10 → Completa la frase (MCQ con blancos)
# Ley Lavoisier: no se ___ ni se ___ → b (crea / destruye)
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 10</div>
        <div class="q-text">¿Qué ley formuló Lavoisier? "La materia no se crea ni se destruye, solo se ___".</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q10" value="a"> elimina</label>
          <label><input type="radio" name="q10" value="b"> transforma</label>
          <label><input type="radio" name="q10" value="c"> divide</label>
          <label><input type="radio" name="q10" value="d"> duplica</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 10</div>
        <span class="q-type-badge badge-text">✏️ Completa la idea</span>
        <div class="q-text">Elige las palabras que completan correctamente la Ley de Lavoisier:<br><br>
        <em>"La materia no se <strong>___</strong> ni se <strong>___</strong>, solo se transforma."</em></div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q10" value="a"> aumenta / reduce</label>
          <label><input type="radio" name="q10" value="b"> crea / destruye</label>
          <label><input type="radio" name="q10" value="c"> mezcla / separa</label>
          <label><input type="radio" name="q10" value="d"> calienta / enfría</label>
        </div>
      </div>''',
  'html', 'Q10 → Completa Ley de Lavoisier'
)

# ══════════════════════════════════════════════════════════════════════════
# Q11 → Gráfico SVG (H₂SO₄ diagrama de átomos)
# ¿Cuántos átomos en total? 2H+1S+4O=7 → c
# ══════════════════════════════════════════════════════════════════════════
SVG_HSO4 = '''<svg viewBox="0 0 290 105" style="max-width:100%;font-family:sans-serif;">
  <text x="145" y="13" text-anchor="middle" font-size="11" font-weight="bold" fill="#374151">Molécula de H₂SO₄ — ácido sulfúrico</text>
  <circle cx="45"  cy="62" r="20" fill="#fce7f3" stroke="#ec4899" stroke-width="2"/>
  <text x="45"  y="58" text-anchor="middle" font-size="15" font-weight="bold" fill="#be185d">H</text>
  <text x="45"  y="74" text-anchor="middle" font-size="10" fill="#be185d">× 2</text>
  <text x="45"  y="92" text-anchor="middle" font-size="8.5" fill="#6b7280">2 átomos</text>
  <line x1="65" y1="62" x2="90" y2="62" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="113" cy="62" r="24" fill="#fef9c3" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="113" y="58" text-anchor="middle" font-size="15" font-weight="bold" fill="#92400e">S</text>
  <text x="113" y="74" text-anchor="middle" font-size="10" fill="#92400e">× 1</text>
  <text x="113" y="96" text-anchor="middle" font-size="8.5" fill="#6b7280">1 átomo</text>
  <line x1="137" y1="62" x2="162" y2="62" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="185" cy="62" r="24" fill="#dbeafe" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="185" y="58" text-anchor="middle" font-size="15" font-weight="bold" fill="#1e3a8a">O</text>
  <text x="185" y="74" text-anchor="middle" font-size="10" fill="#1e3a8a">× 4</text>
  <text x="185" y="96" text-anchor="middle" font-size="8.5" fill="#6b7280">4 átomos</text>
  <rect x="228" y="42" width="54" height="42" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="2"/>
  <text x="255" y="60" text-anchor="middle" font-size="10" fill="#166534" font-weight="bold">Total:</text>
  <text x="255" y="76" text-anchor="middle" font-size="18" font-weight="bold" fill="#166534">?</text>
</svg>'''

px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 11</div>
        <div class="q-text">¿Cuántos átomos de oxígeno tiene la fórmula H₂SO₄?</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="q11" value="a"> 1</label>
          <label><input type="radio" name="q11" value="b"> 2</label>
          <label><input type="radio" name="q11" value="c"> 3</label>
          <label><input type="radio" name="q11" value="d"> 4</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 11</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_HSO4 + '''
          <figcaption>Cada grupo de círculos representa un tipo de átomo en la molécula</figcaption>
        </div>
        <div class="q-text">Según el diagrama, ¿cuántos átomos en <strong>total</strong> tiene la molécula H₂SO₄?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q11" value="a"> 5 átomos</label>
          <label><input type="radio" name="q11" value="b"> 6 átomos</label>
          <label><input type="radio" name="q11" value="c"> 7 átomos</label>
          <label><input type="radio" name="q11" value="d"> 8 átomos</label>
        </div>
      </div>''',
  'html', 'Q11 → SVG H₂SO₄ total átomos'
)

# ══════════════════════════════════════════════════════════════════════════
# Q12 → Verdadero / Falso
# Plasma en el Sol y rayos eléctricos → VERDADERO
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 12</div>
        <div class="q-text">¿Cuál de estos NO es un estado de la materia?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="q12" value="a"> Sólido</label>
          <label><input type="radio" name="q12" value="b"> Plasma</label>
          <label><input type="radio" name="q12" value="c"> Energía</label>
          <label><input type="radio" name="q12" value="d"> Gaseoso</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 12</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">El <strong>plasma</strong> es considerado el cuarto estado de la materia y se puede encontrar naturalmente en el interior del <strong>Sol</strong> y en los <strong>rayos eléctricos</strong> durante las tormentas.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="q12" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="q12" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'Q12 → T/F plasma Sol y rayos'
)

# ══════════════════════════════════════════════════════════════════════════
# Q13 → Texto corto + MCQ
# Thomson modelo pudín de pasas → b
# ══════════════════════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 13</div>
        <div class="q-text">El modelo atómico de Thomson es conocido como el modelo del "Pudín de ___".</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q13" value="a"> uvas</label>
          <label><input type="radio" name="q13" value="b"> pasas</label>
          <label><input type="radio" name="q13" value="c"> ciruelas</label>
          <label><input type="radio" name="q13" value="d"> manzanas</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 13</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          En 1904, J.J. Thomson propuso un modelo atómico en el que los electrones (partículas con carga negativa) estaban <strong>incrustados</strong> dentro de una esfera de carga positiva difusa, similar a las pasas distribuidas dentro de un pudín. Fue el primer modelo atómico que incorporó la existencia de <strong>partículas subatómicas</strong>.
        </div>
        <div class="q-text">¿Por qué el modelo de Thomson se compara con un "pudín de pasas"?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="q13" value="a"> Porque el átomo de Thomson era amarillo y dulce como un pudín</label>
          <label><input type="radio" name="q13" value="b"> Porque en ambos hay partículas pequeñas distribuidas dentro de una masa mayor</label>
          <label><input type="radio" name="q13" value="c"> Porque Thomson era un famoso cocinero además de científico</label>
          <label><input type="radio" name="q13" value="d"> Porque el modelo tenía exactamente la misma forma redonda que un pudín</label>
        </div>
      </div>''',
  'html', 'Q13 → Texto Thomson modelo pudín'
)

# ══════════════════════════════════════════════════════════════════════════
# JS — actualizar correctAnswers quimica q1-q10
# ══════════════════════════════════════════════════════════════════════════
px(
  "      q1:'b',q2:'c',q3:'a',q4:'b',q5:'ac',q6:'d',q7:'b',q8:'a',q9:'c',q10:'b',",
  "      q1:'v',q2:'c',q3:'f',q4:'c',q5:'c',q6:'f',q7:'c',q8:'b',q9:'v',q10:'b',",
  'js', 'JS correctAnswers quimica q1-q10'
)

# ══════════════════════════════════════════════════════════════════════════
# JS — actualizar correctAnswers quimica q11-q13
# ══════════════════════════════════════════════════════════════════════════
px(
  "      q11:'d',q12:'c',q13:'b',q14:'f',q15:'c',q16:'c',q17:'f',q18:'c',q19:'c',q20:'f'",
  "      q11:'c',q12:'v',q13:'b',q14:'f',q15:'c',q16:'c',q17:'f',q18:'c',q19:'c',q20:'f'",
  'js', 'JS correctAnswers quimica q11-q13'
)

# ══════════════════════════════════════════════════════════════════════════
# Aplicar
# ══════════════════════════════════════════════════════════════════════════
total = len(patches)
for i, (old, new, fk, desc) in enumerate(patches, 1):
    if old in data[fk]:
        data[fk] = data[fk].replace(old, new, 1)
        applied += 1
        print(f'  ✅ Patch {i:02d}/{total} — {desc}')
    else:
        print(f'  ⚠️  Patch {i:02d}/{total} NO encontrado — {desc}')

for k, p in paths.items():
    with open(p, 'w', encoding='utf-8') as f:
        f.write(data[k])

print(f'\n{"="*52}')
print(f'{applied}/{total} {"✅  Todo aplicado" if applied == total else "⚠️  Revisa los fallidos"}')
print()
print('Resumen Q1–Q13 Química:')
tipos = [
    ('Q1',  '✓✗ V/F',    'Lavoisier padre química → VERDADERO'),
    ('Q2',  '📄 Lectura', 'Laboratorio kg/g → 2.5 kg (c)'),
    ('Q3',  '✓✗ V/F',    'Líquido forma fija → FALSO'),
    ('Q4',  '🔍 Intruso', 'Sustancias puras vs mezcla → Café (c)'),
    ('Q5',  '📊 Gráfico', '3 modelos atómicos → Rutherford (c)'),
    ('Q6',  '✓✗ V/F',    'Gases nobles muy reactivos → FALSO'),
    ('Q7',  '📄 Lectura', 'Dalton: átomos se reorganizan (c)'),
    ('Q8',  '🔍 Intruso', 'Propiedades mezclas → enlaces ≠ mezcla (b)'),
    ('Q9',  '✓✗ V/F',    'Thomson electrón carga negativa → VERDADERO'),
    ('Q10', '✏️ Cloze',   'Completa Ley Lavoisier → crea/destruye (b)'),
    ('Q11', '📊 Gráfico', 'H₂SO₄ total átomos → 7 (c)'),
    ('Q12', '✓✗ V/F',    'Plasma en Sol y rayos → VERDADERO'),
    ('Q13', '📄 Lectura', 'Thomson pudín de pasas → por qué (b)'),
]
for q, tipo, desc in tipos:
    print(f'  {q:3s} → {tipo:12s}: {desc}')
print()
print('git add . → git commit -m "Química: 20/20 preguntas nuevas" → git push')
