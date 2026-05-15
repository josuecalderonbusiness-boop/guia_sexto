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

# ══════════════════════════════════════════════════════════
# SVGs reutilizables
# ══════════════════════════════════════════════════════════
SVG_CADENA = '''<svg viewBox="0 0 350 78" style="max-width:100%;font-family:sans-serif;">
  <rect x="5" y="19" width="68" height="40" rx="7" fill="#d1fae5" stroke="#10b981" stroke-width="2"/>
  <text x="39" y="35" text-anchor="middle" font-size="10" font-weight="bold" fill="#065f46">🌿 Pasto</text>
  <text x="39" y="50" text-anchor="middle" font-size="8" fill="#065f46">Productor</text>
  <line x1="73" y1="39" x2="88" y2="39" stroke="#94a3b8" stroke-width="2"/>
  <polygon points="86,34 95,39 86,44" fill="#94a3b8"/>
  <rect x="95" y="19" width="74" height="40" rx="7" fill="#fef9c3" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="132" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#92400e">🦗 Saltamontes</text>
  <text x="132" y="50" text-anchor="middle" font-size="8" fill="#92400e">Cons. 1°</text>
  <line x1="169" y1="39" x2="184" y2="39" stroke="#94a3b8" stroke-width="2"/>
  <polygon points="182,34 191,39 182,44" fill="#94a3b8"/>
  <rect x="191" y="19" width="68" height="40" rx="7" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
  <text x="225" y="35" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e3a8a">🐸 Rana</text>
  <text x="225" y="50" text-anchor="middle" font-size="8" fill="#1e3a8a">Cons. 2°</text>
  <line x1="259" y1="39" x2="274" y2="39" stroke="#94a3b8" stroke-width="2"/>
  <polygon points="272,34 281,39 272,44" fill="#94a3b8"/>
  <rect x="281" y="19" width="64" height="40" rx="7" fill="#fce7f3" stroke="#ec4899" stroke-width="2"/>
  <text x="313" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#831843">🐍 Serpiente</text>
  <text x="313" y="50" text-anchor="middle" font-size="8" fill="#831843">Cons. 3°</text>
  <text x="175" y="73" text-anchor="middle" font-size="8.5" fill="#374151" font-weight="bold">Cadena Trófica</text>
</svg>'''

SVG_ECOSISTEMA = '''<svg viewBox="0 0 300 118" style="max-width:100%;font-family:sans-serif;">
  <text x="150" y="12" text-anchor="middle" font-size="10" font-weight="bold" fill="#374151">Factores de un Ecosistema</text>
  <rect x="5" y="18" width="130" height="92" rx="8" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="70" y="32" text-anchor="middle" font-size="9" fill="#64748b" font-weight="bold">ABIÓTICOS</text>
  <text x="38" y="62" text-anchor="middle" font-size="26">☀️</text>
  <text x="38" y="82" text-anchor="middle" font-size="8" fill="#64748b">Luz solar</text>
  <text x="100" y="62" text-anchor="middle" font-size="26">💧</text>
  <text x="100" y="82" text-anchor="middle" font-size="8" fill="#64748b">Agua</text>
  <text x="70" y="102" text-anchor="middle" font-size="7.5" fill="#94a3b8">Temperatura, suelo...</text>
  <rect x="160" y="18" width="135" height="92" rx="8" fill="#f0fdf4" stroke="#10b981" stroke-width="1.5"/>
  <text x="228" y="32" text-anchor="middle" font-size="9" fill="#065f46" font-weight="bold">BIÓTICOS</text>
  <text x="190" y="62" text-anchor="middle" font-size="24">🌳</text>
  <text x="190" y="80" text-anchor="middle" font-size="8" fill="#065f46">Árbol</text>
  <text x="228" y="62" text-anchor="middle" font-size="24">🐇</text>
  <text x="228" y="80" text-anchor="middle" font-size="8" fill="#065f46">Conejo</text>
  <text x="268" y="62" text-anchor="middle" font-size="24">🍄</text>
  <text x="268" y="80" text-anchor="middle" font-size="8" fill="#065f46">Hongo</text>
</svg>'''

SVG_BACTERIAS = '''<svg viewBox="0 0 300 95" style="max-width:100%;font-family:sans-serif;">
  <text x="150" y="12" text-anchor="middle" font-size="10" font-weight="bold" fill="#374151">Formas de Bacterias</text>
  <circle cx="37" cy="52" r="20" fill="#d1fae5" stroke="#10b981" stroke-width="2"/>
  <text x="37" y="56" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">A</text>
  <text x="37" y="80" text-anchor="middle" font-size="8.5" fill="#374151">Esférica</text>
  <rect x="72" y="40" width="46" height="22" rx="11" fill="#fef9c3" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="95" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">B</text>
  <text x="95" y="80" text-anchor="middle" font-size="8.5" fill="#374151">Bastón</text>
  <path d="M150,40 Q162,30 174,40 Q186,50 198,40 Q210,30 222,40" stroke="#818cf8" stroke-width="3" fill="none" stroke-linecap="round"/>
  <text x="186" y="58" text-anchor="middle" font-size="11" font-weight="bold" fill="#4338ca">C</text>
  <text x="186" y="80" text-anchor="middle" font-size="8.5" fill="#374151">Espiral</text>
  <path d="M248,38 Q260,28 264,46 Q266,58 260,65" stroke="#f472b6" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <text x="275" y="52" text-anchor="middle" font-size="11" font-weight="bold" fill="#be185d">D</text>
  <text x="268" y="80" text-anchor="middle" font-size="8.5" fill="#374151">Coma</text>
</svg>'''

SVG_RED = '''<svg viewBox="0 0 290 138" style="max-width:100%;font-family:sans-serif;">
  <text x="145" y="12" text-anchor="middle" font-size="10" font-weight="bold" fill="#374151">Red Trófica</text>
  <circle cx="40" cy="42" r="20" fill="#fef9c3" stroke="#f59e0b" stroke-width="2"/>
  <text x="40" y="46" text-anchor="middle" font-size="18">☀️</text>
  <rect x="100" y="26" width="60" height="32" rx="7" fill="#d1fae5" stroke="#10b981" stroke-width="2"/>
  <text x="130" y="38" text-anchor="middle" font-size="14">🌿</text>
  <text x="130" y="52" text-anchor="middle" font-size="8" fill="#065f46">Planta</text>
  <line x1="60" y1="42" x2="98" y2="42" stroke="#f59e0b" stroke-width="1.5"/>
  <polygon points="96,38 103,42 96,46" fill="#f59e0b"/>
  <rect x="200" y="26" width="60" height="32" rx="7" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <text x="230" y="38" text-anchor="middle" font-size="14">🐇</text>
  <text x="230" y="52" text-anchor="middle" font-size="8" fill="#92400e">Conejo</text>
  <line x1="160" y1="42" x2="198" y2="42" stroke="#94a3b8" stroke-width="1.5"/>
  <polygon points="196,38 203,42 196,46" fill="#94a3b8"/>
  <rect x="200" y="82" width="60" height="32" rx="7" fill="#fce7f3" stroke="#ec4899" stroke-width="2"/>
  <text x="230" y="94" text-anchor="middle" font-size="14">🦊</text>
  <text x="230" y="108" text-anchor="middle" font-size="8" fill="#831843">Zorro</text>
  <line x1="230" y1="58" x2="230" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
  <polygon points="225,78 230,85 235,78" fill="#94a3b8"/>
  <rect x="100" y="82" width="60" height="32" rx="7" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
  <text x="130" y="94" text-anchor="middle" font-size="14">🍄</text>
  <text x="130" y="108" text-anchor="middle" font-size="8" font-weight="bold" fill="#6d28d9">Hongo</text>
  <line x1="130" y1="58" x2="130" y2="80" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="4,3"/>
  <polygon points="125,78 130,85 135,78" fill="#7c3aed"/>
  <text x="20" y="100" font-size="7.5" fill="#6d28d9" font-style="italic">Descomponedor</text>
  <text x="130" y="128" text-anchor="middle" font-size="7.5" fill="#6d28d9">↑ recibe materia orgánica muerta</text>
</svg>'''

# ══════════════════════════════════════════════════════════
# B1 → T/F: factores abióticos NO son seres vivos → FALSO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 1</div>
        <div class="q-text">¿Cuál de estos es un factor ABIÓTICO de un ecosistema?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b1" value="a"> Un árbol</label>
          <label><input type="radio" name="b1" value="b"> Una bacteria</label>
          <label><input type="radio" name="b1" value="c"> La temperatura</label>
          <label><input type="radio" name="b1" value="d"> Un hongo</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 1</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">Los <strong>factores abióticos</strong> de un ecosistema son los seres vivos que lo habitan, como las plantas, los animales y los hongos.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b1" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b1" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B1 → T/F factores abióticos'
)

# ══════════════════════════════════════════════════════════
# B2 → T/F: mitosis produce 2 células idénticas → VERDADERO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 2</div>
        <div class="q-text">La mitosis produce:</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b2" value="a"> 4 células con la mitad de cromosomas</label>
          <label><input type="radio" name="b2" value="b"> 2 células idénticas a la célula madre</label>
          <label><input type="radio" name="b2" value="c"> 1 célula con el doble de cromosomas</label>
          <label><input type="radio" name="b2" value="d"> 3 células diferentes</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 2</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">La <strong>mitosis</strong> produce exactamente <strong>dos células hijas</strong> genéticamente idénticas a la célula madre, con el mismo número de cromosomas.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b2" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b2" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B2 → T/F mitosis 2 células idénticas'
)

# ══════════════════════════════════════════════════════════
# B3 → Texto + MCQ: plantas autótrofas → b
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 3</div>
        <div class="q-text">Las plantas son organismos:</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="b3" value="a"> Autótrofos</label>
          <label><input type="radio" name="b3" value="b"> Heterótrofos carnívoros</label>
          <label><input type="radio" name="b3" value="c"> Heterótrofos descomponedores</label>
          <label><input type="radio" name="b3" value="d"> Heterótrofos omnívoros</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 3</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          En la selva amazónica, las plantas captan la energía solar y, mediante la <strong>fotosíntesis</strong>, producen su propio alimento a partir de agua y CO₂. Los venados se alimentan de estas plantas, y los jaguares cazan a los venados para sobrevivir.
        </div>
        <div class="q-text">Según el texto, ¿qué tipo de nutrición tienen las plantas de la selva?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b3" value="a"> Heterótrofa carnívora</label>
          <label><input type="radio" name="b3" value="b"> Autótrofa</label>
          <label><input type="radio" name="b3" value="c"> Heterótrofa herbívora</label>
          <label><input type="radio" name="b3" value="d"> Descomponedora</label>
        </div>
      </div>''',
  'html', 'B3 → Texto selva amazónica autótrofos'
)

# ══════════════════════════════════════════════════════════
# B4 → T/F: aeróbica produce más ATP porque usa O₂ → VERDADERO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 4</div>
        <div class="q-text">La respiración aeróbica requiere:</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b4" value="a"> Nitrógeno</label>
          <label><input type="radio" name="b4" value="b"> Dióxido de carbono</label>
          <label><input type="radio" name="b4" value="c"> Oxígeno</label>
          <label><input type="radio" name="b4" value="d"> Metano</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 4</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">La respiración <strong>aeróbica</strong> produce mucha más energía (36–38 ATP) que la anaeróbica (2 ATP), porque utiliza <strong>oxígeno</strong> para descomponer completamente la glucosa.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b4" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b4" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B4 → T/F aeróbica más ATP'
)

# ══════════════════════════════════════════════════════════
# B5 → Gráfico SVG cadena trófica: saltamontes = Cons. 1° → b
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 5</div>
        <div class="q-text">El conjunto de seres vivos de diferentes especies que habitan en un área se llama:</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="b5" value="a"> Población</label>
          <label><input type="radio" name="b5" value="b"> Bioma</label>
          <label><input type="radio" name="b5" value="c"> Ecosistema</label>
          <label><input type="radio" name="b5" value="d"> Comunidad</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 5</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_CADENA + '''
          <figcaption>Cadena trófica de un ecosistema de pradera</figcaption>
        </div>
        <div class="q-text">Según la cadena trófica, ¿qué nivel ocupa el <strong>saltamontes</strong>?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b5" value="a"> Productor</label>
          <label><input type="radio" name="b5" value="b"> Consumidor primario</label>
          <label><input type="radio" name="b5" value="c"> Consumidor secundario</label>
          <label><input type="radio" name="b5" value="d"> Descomponedor</label>
        </div>
      </div>''',
  'html', 'B5 → Gráfico cadena trófica saltamontes'
)

# ══════════════════════════════════════════════════════════
# B6 → Intruso: tres son extractivas, fabricación NO → c
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 6</div>
        <div class="q-text">La minería es una actividad económica de tipo:</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b6" value="a"> Terciaria</label>
          <label><input type="radio" name="b6" value="b"> Extractiva</label>
          <label><input type="radio" name="b6" value="c"> Transformadora</label>
          <label><input type="radio" name="b6" value="d"> De servicios</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 6</div>
        <span class="q-type-badge badge-trap">🔍 Encuentra al intruso</span>
        <div class="q-text">Tres son actividades económicas <strong>extractivas</strong>. ¿Cuál <strong>NO</strong> lo es?</div>
        <div class="options intruso-opts" data-correct="c">
          <label><input type="radio" name="b6" value="a"> 🌾 Agricultura</label>
          <label><input type="radio" name="b6" value="b"> ⛏️ Minería</label>
          <label><input type="radio" name="b6" value="c"> 🏭 Fabricación de zapatos</label>
          <label><input type="radio" name="b6" value="d"> 🎣 Pesca</label>
        </div>
      </div>''',
  'html', 'B6 → Intruso actividades extractivas'
)

# ══════════════════════════════════════════════════════════
# B7 → T/F: CO₂ exceso causa efecto invernadero → VERDADERO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 7</div>
        <div class="q-text">El dióxido de carbono (CO₂) en exceso en la atmósfera es responsable del:</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="b7" value="a"> Efecto invernadero</label>
          <label><input type="radio" name="b7" value="b"> Agujero en la capa de ozono</label>
          <label><input type="radio" name="b7" value="c"> Lluvia ácida exclusivamente</label>
          <label><input type="radio" name="b7" value="d"> La respiración de las plantas</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 7</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">El exceso de <strong>CO₂</strong> en la atmósfera, producido por la quema de combustibles fósiles, es la principal causa del <strong>efecto invernadero</strong> y del calentamiento global.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b7" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b7" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B7 → T/F CO₂ efecto invernadero'
)

# ══════════════════════════════════════════════════════════
# B8 → Texto + MCQ: bacterias clasificación → d (Coco = esférica)
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 8</div>
        <div class="q-text">Las bacterias con forma de bastón se llaman:</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b8" value="a"> Cocos</label>
          <label><input type="radio" name="b8" value="b"> Bacilos</label>
          <label><input type="radio" name="b8" value="c"> Espirilos</label>
          <label><input type="radio" name="b8" value="d"> Vibrios</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 8</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          Las bacterias se clasifican según su forma: los <strong>bacilos</strong> tienen forma de bastón alargado (ej: E. coli). Los <strong>cocos</strong> son esféricos (ej: Streptococo). Los <strong>espirilos</strong> tienen forma de espiral (ej: Helicobacter). Los <strong>vibrios</strong> tienen forma de coma o media luna (ej: Cólera).
        </div>
        <div class="q-text">Según el texto, una bacteria con forma <strong>esférica</strong> se clasifica como:</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="b8" value="a"> Bacilo</label>
          <label><input type="radio" name="b8" value="b"> Espirilo</label>
          <label><input type="radio" name="b8" value="c"> Vibrio</label>
          <label><input type="radio" name="b8" value="d"> Coco</label>
        </div>
      </div>''',
  'html', 'B8 → Texto bacterias formas coco esférica'
)

# ══════════════════════════════════════════════════════════
# B9 → Gráfico SVG ecosistema: árbol+conejo+hongo = bióticos → c
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 9</div>
        <div class="q-text">¿Cuál es un factor BIÓTICO?</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="b9" value="a"> El suelo</label>
          <label><input type="radio" name="b9" value="b"> La luz solar</label>
          <label><input type="radio" name="b9" value="c"> La humedad</label>
          <label><input type="radio" name="b9" value="d"> Un hongo</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 9</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_ECOSISTEMA + '''
          <figcaption>Componentes de un ecosistema de bosque</figcaption>
        </div>
        <div class="q-text">Según el diagrama, ¿cuáles son los factores <strong>BIÓTICOS</strong>?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b9" value="a"> Solo la luz solar y el agua</label>
          <label><input type="radio" name="b9" value="b"> Solo el árbol</label>
          <label><input type="radio" name="b9" value="c"> El árbol, el conejo y el hongo</label>
          <label><input type="radio" name="b9" value="d"> La luz solar, el agua y el árbol</label>
        </div>
      </div>''',
  'html', 'B9 → Gráfico ecosistema factores bióticos'
)

# ══════════════════════════════════════════════════════════
# B10 → Texto + MCQ: fases mitosis, anafase = separación → c
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 10</div>
        <div class="q-text">¿En qué fase de la mitosis los cromosomas se alinean en el centro de la célula?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b10" value="a"> Profase</label>
          <label><input type="radio" name="b10" value="b"> Metafase</label>
          <label><input type="radio" name="b10" value="c"> Anafase</label>
          <label><input type="radio" name="b10" value="d"> Telofase</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 10</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          La mitosis tiene cuatro fases: <strong>Profase</strong> (los cromosomas se hacen visibles), <strong>Metafase</strong> (los cromosomas se alinean en el centro), <strong>Anafase</strong> (los cromosomas se separan y se mueven hacia los extremos opuestos de la célula) y <strong>Telofase</strong> (se forman dos núcleos nuevos).
        </div>
        <div class="q-text">Según el texto, ¿en qué fase los cromosomas se desplazan hacia los <strong>extremos opuestos</strong> de la célula?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b10" value="a"> Profase</label>
          <label><input type="radio" name="b10" value="b"> Metafase</label>
          <label><input type="radio" name="b10" value="c"> Anafase</label>
          <label><input type="radio" name="b10" value="d"> Telofase</label>
        </div>
      </div>''',
  'html', 'B10 → Texto fases mitosis anafase'
)

# ══════════════════════════════════════════════════════════
# B11 → T/F: fermentación pan = anaeróbica, NO aeróbica → FALSO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 11</div>
        <div class="q-text">La fermentación del pan es un ejemplo de respiración:</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b11" value="a"> Aeróbica</label>
          <label><input type="radio" name="b11" value="b"> Anaeróbica</label>
          <label><input type="radio" name="b11" value="c"> Fotosintética</label>
          <label><input type="radio" name="b11" value="d"> Celular aerobia</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 11</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">La fermentación del pan y la producción del yogur son ejemplos de respiración <strong>aeróbica</strong>, porque requieren la presencia de oxígeno para que ocurran.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b11" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b11" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B11 → T/F fermentación aeróbica falso'
)

# ══════════════════════════════════════════════════════════
# B12 → Intruso: tres heterótrofos, helecho = autótrofo → b
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 12</div>
        <div class="q-text">Un herbívoro es un organismo:</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b12" value="a"> Autótrofo</label>
          <label><input type="radio" name="b12" value="b"> Heterótrofo carnívoro</label>
          <label><input type="radio" name="b12" value="c"> Heterótrofo que se alimenta de plantas</label>
          <label><input type="radio" name="b12" value="d"> Descomponedor</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 12</div>
        <span class="q-type-badge badge-trap">🔍 Encuentra al intruso</span>
        <div class="q-text">Tres de los siguientes son organismos <strong>heterótrofos</strong>. ¿Cuál es el único <strong>autótrofo</strong>?</div>
        <div class="options intruso-opts" data-correct="b">
          <label><input type="radio" name="b12" value="a"> 🦁 León</label>
          <label><input type="radio" name="b12" value="b"> 🌿 Helecho</label>
          <label><input type="radio" name="b12" value="c"> 🐛 Oruga</label>
          <label><input type="radio" name="b12" value="d"> 🍄 Hongo</label>
        </div>
      </div>''',
  'html', 'B12 → Intruso autótrofo vs heterótrofos'
)

# ══════════════════════════════════════════════════════════
# B13 → Gráfico SVG bacterias: ¿cuál es bastón (bacilo)? → b
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 13</div>
        <div class="q-text">Las bacterias esféricas se denominan:</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="b13" value="a"> Cocos</label>
          <label><input type="radio" name="b13" value="b"> Bacilos</label>
          <label><input type="radio" name="b13" value="c"> Espirilos</label>
          <label><input type="radio" name="b13" value="d"> Vibrios</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 13</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_BACTERIAS + '''
          <figcaption>Cuatro formas distintas de bacterias (A, B, C, D)</figcaption>
        </div>
        <div class="q-text">¿Cuál de las formas representadas corresponde a un <strong>BACILO</strong>?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b13" value="a"> Forma A (esférica)</label>
          <label><input type="radio" name="b13" value="b"> Forma B (bastón)</label>
          <label><input type="radio" name="b13" value="c"> Forma C (espiral)</label>
          <label><input type="radio" name="b13" value="d"> Forma D (coma)</label>
        </div>
      </div>''',
  'html', 'B13 → Gráfico formas bacterias bacilo'
)

# ══════════════════════════════════════════════════════════
# B14 → T/F: ácido láctico en músculos por anaeróbica → VERDADERO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 14</div>
        <div class="q-text">¿Cuál es el producto principal de la respiración anaeróbica en los músculos?</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b14" value="a"> Oxígeno</label>
          <label><input type="radio" name="b14" value="b"> Ácido láctico</label>
          <label><input type="radio" name="b14" value="c"> Glucosa</label>
          <label><input type="radio" name="b14" value="d"> ATP en grandes cantidades</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 14</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">El <strong>ácido láctico</strong> es el producto principal de la respiración anaeróbica en los músculos, y es el responsable del dolor muscular que sentimos después de hacer ejercicio intenso.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b14" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b14" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B14 → T/F ácido láctico músculos'
)

# ══════════════════════════════════════════════════════════
# B15 → Texto + MCQ: actividades extractivas → c
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 15</div>
        <div class="q-text">La pesca y la agricultura son ejemplos de actividades:</div>
        <div class="options" data-correct="a">
          <label><input type="radio" name="b15" value="a"> Extractivas</label>
          <label><input type="radio" name="b15" value="b"> Industriales</label>
          <label><input type="radio" name="b15" value="c"> De servicios</label>
          <label><input type="radio" name="b15" value="d"> Tecnológicas</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 15</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          Las <strong>actividades extractivas</strong> toman recursos directamente de la naturaleza sin transformarlos significativamente. La pesca extrae peces del mar o los ríos. La minería extrae minerales del subsuelo. La agricultura cultiva y cosecha plantas. En todos los casos, el recurso viene <strong>directamente de la naturaleza</strong>.
        </div>
        <div class="q-text">Según el texto, ¿qué tienen en común la pesca, la minería y la agricultura?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b15" value="a"> Las tres usan maquinaria industrial avanzada</label>
          <label><input type="radio" name="b15" value="b"> Las tres transforman materias primas en productos elaborados</label>
          <label><input type="radio" name="b15" value="c"> Las tres extraen recursos directamente de la naturaleza</label>
          <label><input type="radio" name="b15" value="d"> Las tres producen exclusivamente alimentos</label>
        </div>
      </div>''',
  'html', 'B15 → Texto actividades extractivas naturaleza'
)

# ══════════════════════════════════════════════════════════
# B16 → T/F: en Interfase el ADN se duplica → VERDADERO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 16</div>
        <div class="q-text">¿Qué ocurre en la Interfase de la mitosis?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b16" value="a"> Los cromosomas se separan</label>
          <label><input type="radio" name="b16" value="b"> La célula se divide</label>
          <label><input type="radio" name="b16" value="c"> El ADN se duplica</label>
          <label><input type="radio" name="b16" value="d"> Se forma la membrana nueva</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 16</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">Durante la <strong>Interfase</strong>, que ocurre antes de la mitosis, el ADN se <strong>duplica</strong> para asegurarse de que cada célula hija recibirá una copia completa del material genético.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b16" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b16" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B16 → T/F Interfase ADN se duplica'
)

# ══════════════════════════════════════════════════════════
# B17 → Intruso: tres descomponedores, león NO → b
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 17</div>
        <div class="q-text">Los hongos son organismos:</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b17" value="a"> Autótrofos</label>
          <label><input type="radio" name="b17" value="b"> Heterótrofos descomponedores</label>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 17</div>
        <span class="q-type-badge badge-trap">🔍 Encuentra al intruso</span>
        <div class="q-text">Tres de los siguientes son organismos <strong>descomponedores</strong>. ¿Cuál <strong>NO</strong> lo es?</div>
        <div class="options intruso-opts" data-correct="b">
          <label><input type="radio" name="b17" value="a"> 🍄 Hongo del bosque</label>
          <label><input type="radio" name="b17" value="b"> 🦁 León</label>
          <label><input type="radio" name="b17" value="c"> 🦠 Bacteria saprofita</label>
          <label><input type="radio" name="b17" value="d"> 🧫 Moho del pan</label>''',
  'html', 'B17 → Intruso descomponedores'
)

# Necesito cerrar el div de B17 (el original tenía más líneas que aún están)
# Busco el resto del bloque original de b17
px(
  '''          <label><input type="radio" name="b17" value="c"> Autótrofos fotosintéticos</label>
          <label><input type="radio" name="b17" value="d"> Heterótrofos carnívoros</label>
        </div>
      </div>''',
  '''        </div>
      </div>''',
  'html', 'B17 → cerrar bloque intruso'
)

# ══════════════════════════════════════════════════════════
# B18 → Gráfico SVG red trófica: hongo = descomponedor → d
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 18</div>
        <div class="q-text">¿Cuáles son los factores que componen un ecosistema? (Elige 2)</div>
        <div class="options" data-correct="ac" data-type="multi">
          <label><input type="checkbox" name="b18" value="a"> Bióticos</label>
          <label><input type="checkbox" name="b18" value="b"> Económicos</label>
          <label><input type="checkbox" name="b18" value="c"> Abióticos</label>
          <label><input type="checkbox" name="b18" value="d"> Políticos</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 18</div>
        <span class="q-type-badge badge-graph">📊 Pregunta con gráfico</span>
        <div class="q-graphic">
          ''' + SVG_RED + '''
          <figcaption>Red trófica simplificada de un ecosistema</figcaption>
        </div>
        <div class="q-text">Según el diagrama, ¿qué organismo cumple el rol de <strong>descomponedor</strong>?</div>
        <div class="options" data-correct="d">
          <label><input type="radio" name="b18" value="a"> La planta</label>
          <label><input type="radio" name="b18" value="b"> El conejo</label>
          <label><input type="radio" name="b18" value="c"> El zorro</label>
          <label><input type="radio" name="b18" value="d"> El hongo</label>
        </div>
      </div>''',
  'html', 'B18 → Gráfico red trófica descomponedor'
)

# ══════════════════════════════════════════════════════════
# B19 → T/F: contaminación autos = atmosférica → VERDADERO
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 19</div>
        <div class="q-text">La contaminación del aire por los gases de los automóviles es un ejemplo de contaminación:</div>
        <div class="options" data-correct="b">
          <label><input type="radio" name="b19" value="a"> Hídrica</label>
          <label><input type="radio" name="b19" value="b"> Atmosférica</label>
          <label><input type="radio" name="b19" value="c"> Del suelo</label>
          <label><input type="radio" name="b19" value="d"> Acústica</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 19</div>
        <span class="q-type-badge badge-tf">✓✗ Verdadero o Falso</span>
        <div class="q-text">La contaminación producida por los gases que emiten los automóviles se clasifica como <strong>contaminación atmosférica</strong>, porque afecta directamente la calidad del aire.</div>
        <div class="options tf-opts">
          <label><input type="radio" name="b19" value="v"><span class="tf-btn tf-btn-v">✅ VERDADERO</span></label>
          <label><input type="radio" name="b19" value="f"><span class="tf-btn tf-btn-f">❌ FALSO</span></label>
        </div>
      </div>''',
  'html', 'B19 → T/F contaminación atmosférica'
)

# ══════════════════════════════════════════════════════════
# B20 → Texto + MCQ: microorganismos definición → c
# ══════════════════════════════════════════════════════════
px(
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 20</div>
        <div class="q-text">¿Cuáles de los siguientes son microorganismos? (Selecciona los correctos)</div>
        <div class="options" data-correct="abd" data-type="multi">
          <label><input type="checkbox" name="b20" value="a"> Bacterias</label>
          <label><input type="checkbox" name="b20" value="b"> Virus</label>
          <label><input type="checkbox" name="b20" value="c"> Elefantes</label>
          <label><input type="checkbox" name="b20" value="d"> Hongos microscópicos</label>
        </div>
      </div>''',
  '''      <div class="quiz-block">
        <div class="q-num">Pregunta 20</div>
        <span class="q-type-badge badge-text">📄 Lee y responde</span>
        <div class="text-passage">
          Los <strong>microorganismos</strong> son seres vivos tan pequeños que no pueden verse a simple vista y requieren microscopio. Incluyen bacterias, virus, protozoos, hongos microscópicos y algas unicelulares. Son fundamentales para los ecosistemas porque participan en la <strong>descomposición</strong> de materia orgánica y en ciclos como el del nitrógeno.
        </div>
        <div class="q-text">Según el texto, ¿qué característica <strong>define</strong> a todos los microorganismos?</div>
        <div class="options" data-correct="c">
          <label><input type="radio" name="b20" value="a"> Todos son dañinos para la salud humana</label>
          <label><input type="radio" name="b20" value="b"> Todos son bacterias unicelulares</label>
          <label><input type="radio" name="b20" value="c"> No se pueden observar a simple vista y requieren microscopio</label>
          <label><input type="radio" name="b20" value="d"> Todos se reproducen únicamente por mitosis</label>
        </div>
      </div>''',
  'html', 'B20 → Texto microorganismos definición'
)

# ══════════════════════════════════════════════════════════
# JS — correctAnswers biología línea 1
# ══════════════════════════════════════════════════════════
px(
  "      b1:'c',b2:'b',b3:'a',b4:'c',b5:'d',b6:'b',b7:'a',b8:'b',b9:'d',b10:'b',",
  "      b1:'f',b2:'v',b3:'b',b4:'v',b5:'b',b6:'c',b7:'v',b8:'d',b9:'c',b10:'c',",
  'js', 'JS correctAnswers biologia b1-b10'
)

# ══════════════════════════════════════════════════════════
# JS — correctAnswers biología línea 2
# ══════════════════════════════════════════════════════════
px(
  "      b11:'b',b12:'c',b13:'a',b14:'b',b15:'a',b16:'c',b17:'b',b18:'ac',b19:'b',b20:'abd'",
  "      b11:'f',b12:'b',b13:'b',b14:'v',b15:'c',b16:'v',b17:'b',b18:'d',b19:'v',b20:'c'",
  'js', 'JS correctAnswers biologia b11-b20'
)

# ══════════════════════════════════════════════════════════
# Aplicar
# ══════════════════════════════════════════════════════════
total = len(patches)
for i, (old, new, fk, desc) in enumerate(patches, 1):
    if old in data[fk]:
        data[fk] = data[fk].replace(old, new, 1)
        applied += 1
        print(f'  ✅ {i:02d}/{total} — {desc}')
    else:
        print(f'  ⚠️  {i:02d}/{total} NO encontrado — {desc}')

for k, p in paths.items():
    with open(p, 'w', encoding='utf-8') as f:
        f.write(data[k])

print(f'\n{"="*55}')
print(f'{applied}/{total} {"✅  Todo aplicado" if applied == total else "⚠️  Revisa los fallidos"}')
print()
rows = [
  ('B1','✓✗ V/F','Factores abióticos NO son seres vivos → FALSO'),
  ('B2','✓✗ V/F','Mitosis 2 células idénticas → VERDADERO'),
  ('B3','📄 Lectura','Selva amazónica → tipo nutrición plantas (b)'),
  ('B4','✓✗ V/F','Aeróbica más ATP con O₂ → VERDADERO'),
  ('B5','📊 Gráfico','Cadena trófica SVG → saltamontes nivel (b)'),
  ('B6','🔍 Intruso','Extractivas vs fábrica de zapatos (c)'),
  ('B7','✓✗ V/F','CO₂ exceso = efecto invernadero → VERDADERO'),
  ('B8','📄 Lectura','Bacterias formas → esférica = coco (d)'),
  ('B9','📊 Gráfico','Ecosistema SVG → factores bióticos (c)'),
  ('B10','📄 Lectura','Fases mitosis → anafase separación (c)'),
  ('B11','✓✗ V/F','Fermentación aeróbica → FALSO'),
  ('B12','🔍 Intruso','Heterótrofos vs helecho autótrofo (b)'),
  ('B13','📊 Gráfico','Formas bacterias SVG → bacilo = bastón (b)'),
  ('B14','✓✗ V/F','Ácido láctico en músculos → VERDADERO'),
  ('B15','📄 Lectura','Actividades extractivas = de naturaleza (c)'),
  ('B16','✓✗ V/F','Interfase ADN se duplica → VERDADERO'),
  ('B17','🔍 Intruso','Descomponedores vs león carnívoro (b)'),
  ('B18','📊 Gráfico','Red trófica SVG → hongo descomponedor (d)'),
  ('B19','✓✗ V/F','Gases autos = contaminación atmosférica → VERDADERO'),
  ('B20','📄 Lectura','Microorganismos definición → microscopio (c)'),
]
for q, tipo, desc in rows:
    print(f'  {q:3s} → {tipo:12s}: {desc}')
print()
print('git add . → git commit -m "Biología: 20/20 preguntas nuevas" → git push')
