const { google } = require('googleapis');
const https = require('https');

const SHEET_ID = process.env.SHEET_ID;

// ── Currículo completo de Jero (grado 2) ────────────────────────────
const CURRICULO = {
  MAT: [
    'Valor posicional hasta 4 cifras: Unidades, Decenas, Centenas y Unidades de Mil. Lectura y escritura de números en cifras y en palabras. Descomposición aditiva (ej: 1345 = 1000+300+40+5). Equivalencias: cuántas unidades hay en 3 centenas, cuántas decenas forman 1 centena.',
    'Comparación y orden de números hasta 4 cifras: mayor que, menor que e igual a. Número anterior, posterior y entre. Series numéricas ascendentes y descendentes de 2 en 2, de 5 en 5, de 10 en 10 y de 100 en 100. Números ordinales del primero al vigésimo.',
    'Adición hasta 4 dígitos con reagrupación en decenas y centenas simultáneamente. Términos: sumandos y total. Sumas verticales y horizontales. Problemas verbales con palabras clave: agrupar, reunir, en total.',
    'Sustracción hasta 4 dígitos con desagrupación consecutiva. Caso especial: restar a números con ceros intermedios (ej: 500-124). Términos: minuendo, sustraendo y diferencia. Prueba de la resta: sustraendo + diferencia = minuendo.',
    'Multiplicación: tablas del 2 al 9. Multiplicación como adición iterada (ej: 4+4+4+4+4 = 5x4). Arreglos rectangulares filas por columnas. Propiedad conmutativa (3x5 = 5x3). Palabras clave: el triple, el doble, repetir.',
    'División intuitiva: reparto en partes iguales. Mitad (dividir entre 2) y doble (multiplicar por 2). Problemas de repartir objetos en grupos iguales. Relación entre multiplicación y división básica.',
    'Resolución de problemas de un paso con enunciado verbal: identificar palabras clave para elegir la operación correcta entre suma, resta y multiplicación. Extraer datos y redactar respuesta completa.',
    'Resolución de problemas de dos pasos combinando suma y resta. Situaciones de la vida real con compras, frutas, juguetes. Identificar qué operación va primero.',
    'Geometría plana: círculo, triángulo, cuadrado, rectángulo, rombo y óvalo. Contar lados y vértices. Reconocer ángulos rectos y oblicuos. Clasificar figuras por número de lados.',
    'Cuerpos geométricos: cubo, esfera, cilindro, cono y pirámide. Diferencia entre figuras planas y sólidos tridimensionales. Clasificar en los que ruedan y los que no ruedan. Caras, aristas y vértices básico.',
    'Líneas rectas, curvas, abiertas y cerradas. Líneas paralelas y perpendiculares. Simetría: identificar eje de simetría y completar figuras simétricas.',
    'Medición de longitud: centímetros y metros. Uso correcto de la regla desde el cero. Comparar longitudes. Unidades arbitrarias vs estándar.',
    'El reloj analógico: aguja horaria corta y minutero largo. Horas en punto y medias horas. El calendario: días de la semana, meses del año. Problemas con fechas: si hoy es martes 15 qué día será el 18.',
    'Capacidad y masa: comparar objetos en una balanza. Qué recipiente almacena más líquido. Litro como unidad básica. Conceptos de más pesado, más liviano, lleno y vacío.',
    'Gráficas de barras sencillas: leer e interpretar datos. Tablas de conteo con palitos. Responder preguntas: cuál es el mayor, cuál el menor, cuántos más que, cuántos en total.',
    'Operaciones combinadas: elegir la operación correcta entre suma, resta y multiplicación según el contexto. Problemas mixtos con geometría y medidas.',
    'Valor posicional avanzado: descomposición y composición de números de 4 cifras. Forma desarrollada y compacta. Comparar y ordenar series de cuatro números de mayor a menor.',
    'Tablas del 6, 7, 8 y 9. Patrones de multiplicación. Problemas de multiplicación con contexto real. Verificar resultado con suma repetida.',
    'Números ordinales del primero al vigésimo en situaciones reales: carreras, filas, posiciones. Secuencias numéricas con patrones mixtos.',
    'Repaso integral: pensamiento numérico, operaciones con reagrupación, geometría, medidas y estadística. Problemas de dos pasos nivel grado 2 transición a grado 3.',
  ],
  LCA: [
    // Lección 1 — La oración
    'La oración: toda oración tiene dos partes: QUIÉN (la persona, animal o cosa que hace algo) y QUÉ HACE (la acción que realiza). Ejemplo: "El perro corre en el parque" — QUIÉN: el perro / QUÉ HACE: corre en el parque. Identificar si una oración está completa o incompleta. Completar oraciones a las que les falta una parte. Usar oraciones simples con animales, personas y objetos del hogar como contexto.',

    // Lección 2 — Palabras que unen
    'Palabras que unen oraciones: algunas palabras sirven para unir ideas. "Y" une cosas que van juntas (tengo un perro Y un gato). "Pero" muestra algo diferente (quiero jugar PERO debo estudiar). "Porque" explica el motivo (no fui PORQUE llovía). "Entonces" muestra lo que pasa después (llovió, ENTONCES abrí el paraguas). Elegir la palabra correcta para unir dos oraciones cortas. Contexto: situaciones del hogar, el colegio y los amigos.',

    // Lección 3 — Tipos de texto
    'Tipos de texto que leemos y escribimos: el CUENTO tiene personajes, un problema y una solución (Caperucita, el lobo, el bosque). La POESÍA tiene rima y ritmo, se escucha bonita al leer en voz alta. La RECETA tiene una lista de ingredientes y pasos en orden (primero... luego... finalmente...). Identificar qué tipo de texto es un fragmento corto según sus características visibles.',

    // Lección 4 — Nombres de personas y cosas
    'Los nombres en español: algunos nombres son de personas, mascotas o lugares específicos y siempre llevan letra MAYÚSCULA (María, Bogotá, Río Magdalena). Otros nombres son de cosas, animales o personas en general y llevan letra minúscula (mesa, perro, niña). Reconocer cuándo escribir con mayúscula. Identificar el género (masculino/femenino) y el número (uno o varios). Detectar errores como "los gata" en lugar de "las gatas".',

    // Lección 5 — Palabras que describen
    'Palabras que describen cómo son las cosas: algunas palabras nos dicen cómo es algo — grande, pequeño, suave, rápido, feliz, bonito, azul. Estas palabras siempre acompañan al nombre al que describen y deben coincidir: "el gato negro" / "la gata negra" / "los gatos negros". Completar descripciones de personajes y objetos. Elegir la palabra descriptiva correcta en una oración.',

    // Lección 6 — Palabras de acción y tiempo
    'Palabras de acción: los verbos dicen lo que alguien hace o siente (correr, comer, dormir, reír). Lo importante es el TIEMPO de la acción: ANTES (ayer corrí), AHORA (hoy corro), DESPUÉS (mañana correré). Cambiar una oración de "ahora" a "antes" o "después". Identificar cuándo ocurre la acción en una oración corta. Contexto: actividades cotidianas del niño.',

    // Lección 7 — El, la, un, una y yo, tú, él
    'Palabras pequeñas pero importantes: EL / LA / LOS / LAS van antes de los nombres que ya conocemos (el perro, la casa). UN / UNA / UNOS / UNAS van antes de nombres que mencionamos por primera vez (un perro, una casa). YO / TÚ / ÉL / ELLA / NOSOTROS / ELLOS reemplazan nombres para no repetirlos (María come → ELLA come). Elegir la palabra correcta para completar oraciones.',

    // Lección 8 — Palabras parecidas y opuestas
    'Palabras que significan casi lo mismo y palabras contrarias: FELIZ y CONTENTO significan casi lo mismo — son palabras parecidas. FRÍO y CALIENTE son contrarias — son opuestas. Aprender pares: rápido/veloz, grande/enorme, triste/alegre, alto/bajo, encender/apagar, entrar/salir. Elegir la palabra parecida o la opuesta correcta en una oración.',

    // Lección 9 — Sílabas
    'Separar las palabras en partes que se pronuncian de un golpe de voz: ca-sa, ma-ri-po-sa, e-le-fan-te. Contar cuántas partes tiene una palabra. Una parte suena más fuerte que las otras — esa es la parte especial (ma-RI-po-sa). Ordenar palabras de menor a mayor número de sílabas. Completar la separación correcta de una palabra.',

    // Lección 10 — Mayúsculas y puntos
    'Cuándo escribir con letra grande (mayúscula) y cuándo poner un punto: la mayúscula va al inicio de una oración y en nombres propios (Juan, Colombia). El punto va al final de cada idea completa. Los signos ¿? van cuando se pregunta algo — uno al inicio y otro al final. Los signos ¡! van cuando algo nos sorprende o emociona. Identificar errores y corregirlos en oraciones cortas.',

    // Lección 11 — M antes de B y P, y sílabas difíciles
    'Regla fácil: antes de B y antes de P siempre va M, nunca N. Ejemplos: tambor, sombra, campo, impresora, siempre. Sílabas difíciles con dos consonantes juntas: bla, bre, cla, flo, pra, gra, tra, dra — se pronuncian juntas. Palabras: blusa, brazo, clase, flor, prado, grito, tren, dragón. Completar palabras y elegir la escritura correcta.',

    // Lección 12 — Letras que se confunden
    'Letras que suenan parecido y se confunden al escribir: B y V suenan igual (barco/vaca), hay que aprender cuál va en cada palabra. H no suena pero sí se escribe (huevo, hijo, hablar). G y J a veces suenan igual (gente/jinete). LL e Y a veces suenan igual (llave/yoyo). Identificar la escritura correcta entre dos opciones para palabras cotidianas.',

    // Lección 13 — Imágenes que hablan
    'Las imágenes también nos dan información: las señales de tránsito (PARE, cruce de peatones, prohibido) nos dicen qué hacer sin usar palabras. Las historietas o cómics cuentan historias con dibujos y globos de diálogo. Interpretar qué está pasando en una secuencia de imágenes. Relacionar una imagen con su mensaje o con una oración.',

    // Lección 14 — Armar y ordenar textos
    'Ordenar ideas para que tengan sentido: las oraciones de un párrafo deben ir en un orden lógico — primero, luego, después, finalmente. Encontrar la idea más importante de un párrafo corto. Completar un texto con la palabra que falta. Ordenar oraciones desordenadas para formar una historia breve.',

    // Lecciones 15-20 — Repasos
    'Repaso: la oración completa, palabras que unen y tipos de texto. Preguntas mixtas con oraciones y fragmentos cortos de cuentos, poemas y recetas.',
    'Repaso: nombres propios y comunes con mayúsculas, palabras descriptivas, verbos y tiempos. Preguntas mixtas aplicadas a oraciones y textos cortos.',
    'Repaso: palabras parecidas, palabras opuestas y separación en sílabas. Preguntas mixtas de vocabulario y lectura en voz alta.',
    'Repaso: mayúsculas, puntos, signos de pregunta y admiración. M antes de B y P. Sílabas difíciles. Letras confundidas. Detectar y corregir errores.',
    'Repaso: imágenes y señales. Ordenar párrafos y completar textos con palabras correctas.',
    'Evaluación final: todos los temas de Lengua Castellana. Oraciones, tipos de texto, gramática, ortografía y comprensión. Preguntas mixtas nivel grado 2.',
  ],
  ING: [
    'INGLÉS — Saludos y despedidas. Vocabulario: Hello, Hi, Good morning, Good afternoon, Good evening, Goodbye, Bye, See you. TODAS LAS PREGUNTAS EN ESPAÑOL, solo las palabras en inglés aparecen como opciones o dentro de la pregunta. Tipos: ¿Cómo se dice "Buenos días"? (opciones: Good morning / Good night / Goodbye / Hello), elegir el saludo correcto según la hora del día, completar: Good ___, how are you? (morning/evening/bye/hi).',
    'INGLÉS — Presentarse. Frases clave: What is your name? My name is... How are you? I am fine / good / happy. Nice to meet you. PREGUNTAS EN ESPAÑOL. Tipos: ¿Qué significa "What is your name?"?, completar el diálogo con la palabra correcta en inglés, elegir la respuesta correcta a "How are you?"',
    'INGLÉS — Útiles escolares. Vocabulario: pencil, pen, book, notebook, eraser, ruler, sharpener, backpack, desk, chair. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "lápiz"?, ¿Qué significa "eraser"?, completar: I have a ___ (opciones en inglés: pencil/pen/book/eraser).',
    'INGLÉS — El salón de clase. Vocabulario: classroom, teacher, student, board, door, window, table. Comandos: Open your book, Close the door, Listen, Sit down, Stand up. PREGUNTAS EN ESPAÑOL. Tipos: ¿Qué significa "Sit down"?, ¿Cómo se dice "tablero"?, ¿Cuál comando significa "abre tu libro"?',
    'INGLÉS — Familia básica. Vocabulario: mother, father, brother, sister, baby, family. Frase: This is my mother/father/brother/sister. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "hermano"?, ¿Qué significa "father"?, completar: This is my ___ (opciones: mother/father/sister/brother).',
    'INGLÉS — Familia extendida. Vocabulario: grandmother, grandfather, uncle, aunt, cousin, parents, grandparents. Frases: She is my grandmother. He is my uncle. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "abuela"?, ¿Qué significa "uncle"?, completar: He is my ___.',
    'INGLÉS — Describir con adjetivos. Vocabulario: tall, short, big, small, old, young, funny, kind, happy. Frases: My mother is tall. My brother is funny. PREGUNTAS EN ESPAÑOL. Tipos: ¿Qué significa "tall"?, ¿Cuál es el opuesto de "big"?, completar: My father is ___ (opciones: tall/short/old/young).',
    'INGLÉS — Verbo To Be. Formas: I am, You are, He is, She is. Frases: She is my sister. I am happy. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cuál es correcto: "My mother is kind" o "My mother are kind"?, completar: My sister ___ tall (is/am/are/be), ¿Qué significa "I am happy"?',
    'INGLÉS — Repaso: saludos, presentación, útiles, salón y familia. PREGUNTAS EN ESPAÑOL. Tipos: traducción español→inglés, completar diálogos cortos, encontrar la palabra que no pertenece al grupo, corregir el error.',
    'INGLÉS — Colores. Vocabulario: red, blue, green, yellow, orange, purple, pink, black, white, brown. Frases: The apple is red. The sky is blue. PREGUNTAS EN ESPAÑOL. Tipos: ¿De qué color es el cielo en inglés?, completar: The banana is ___, ¿Cómo se dice "verde"?',
    'INGLÉS — Números del 1 al 20. Vocabulario: one, two, three... twenty. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice el número 7 en inglés?, ¿Qué número es "fifteen"?, completar la secuencia: one, two, ___, four.',
    'INGLÉS — Animales. Vocabulario: dog, cat, bird, fish, rabbit, horse, cow, lion, elephant, monkey. Frases: It is a dog. The cat is small. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "perro"?, ¿Qué significa "elephant"?, completar: It is a ___.',
    'INGLÉS — Comida y bebida. Vocabulario: apple, banana, orange, bread, milk, water, juice, egg, rice, chicken. Frases: I eat an apple. I drink milk. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "manzana"?, ¿Qué significa "milk"?, completar: I drink ___.',
    'INGLÉS — Partes del cuerpo. Vocabulario: head, eyes, ears, nose, mouth, hands, arms, legs, feet, hair. Frases: I have two eyes. My nose is small. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "nariz"?, ¿Qué significa "legs"?, completar: I have two ___.',
    'INGLÉS — Repaso: colores, números, animales, comida, cuerpo y familia. PREGUNTAS EN ESPAÑOL. Tipos: traducción directa, completar oraciones, encontrar el intruso, corregir errores.',
    'INGLÉS — Verbos de acción. Vocabulario: run, jump, eat, sleep, play, read, write, draw, swim, walk. Frases: I play. She runs. He sleeps. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "correr"?, ¿Qué significa "sleep"?, completar: I ___ every day.',
    'INGLÉS — La casa. Vocabulario: house, bedroom, bathroom, kitchen, living room, garden, door, window. Frases: I sleep in the bedroom. We eat in the kitchen. PREGUNTAS EN ESPAÑOL. Tipos: ¿Cómo se dice "cocina"?, completar: I sleep in the ___.',
    'INGLÉS — Ropa y clima. Vocabulario: shirt, pants, shoes, jacket, hat, dress. Clima: sunny, rainy, cold, hot. Frase: It is cold. I wear a jacket. PREGUNTAS EN ESPAÑOL. Tipos: ¿Qué ropa usas cuando hace frío? (opciones en inglés), completar: It is ___ today.',
    'INGLÉS — Preguntas básicas. What is this? What color is it? How many? Is it a dog? Yes, it is / No, it is not. PREGUNTAS EN ESPAÑOL. Tipos: completar la pregunta, elegir la respuesta correcta, traducir preguntas y respuestas cortas.',
    'INGLÉS — Evaluación integral A1: saludos, familia, colores, números, animales, comida, cuerpo, verbos, casa. PREGUNTAS EN ESPAÑOL. Traducción, completar, corregir errores y diálogos cortos.',
  ],
  NAT: [
    'Seres vivos e inertes: características de los seres vivos (nacen, crecen, se nutren, respiran, se reproducen y mueren). Diferencia con objetos inertes naturales (rocas, agua) y artificiales (juguetes, ropa).',
    'Las plantas: partes y funciones. Raíz (absorción y fijación), tallo (soporte y transporte), hojas (respiración y fotosíntesis), flores y frutos (reproducción). Necesidades: agua, luz, aire y nutrientes.',
    'Los animales según su alimentación: herbívoros (plantas), carnívoros (carne) y omnívoros (ambos). Ejemplos cotidianos de cada grupo. Identificar de qué se alimenta un animal por sus características físicas.',
    'Los animales según su hábitat y desplazamiento: terrestres (caminan, corren, reptan), acuáticos (nadan) y aéreos (vuelan). Animales que viven en dos medios (anfibios básico).',
    'Animales vertebrados e invertebrados: vertebrados tienen huesos internos (mamíferos, aves, peces, reptiles, anfibios). Invertebrados no tienen huesos (insectos, gusanos, arañas). Clasificar por cubierta corporal: pelos, plumas, escamas, piel desnuda.',
    'Ciclos de vida: la mariposa (huevo, oruga, crisálida, adulto) y la rana (huevo, renacuajo, rana joven, adulto). Comparar etapas y cambios en cada ciclo.',
    'Los cinco sentidos: órganos y funciones. Ojos/visión, oídos/audición, lengua/gusto, nariz/olfato, piel/tacto. Funciones de protección y adaptación. Cuidado de los órganos de los sentidos.',
    'El cuerpo humano: tres zonas. Cabeza (cara, cráneo), tronco (pecho, abdomen, espalda) y extremidades superiores e inferiores. Órganos internos básicos: corazón, pulmones, estómago.',
    'Hábitos saludables: alimentos saludables (frutas, verduras, proteínas) vs no saludables (dulces, ultraprocesados). Higiene corporal: lavado de manos, cepillado de dientes. Ejercicio y sueño adecuado.',
    'Estados de la materia: sólido (forma y volumen definidos), líquido (toma la forma del recipiente) y gaseoso (sin forma ni volumen definidos, se expande). Ejemplos cotidianos de cada estado.',
    'Cambios de estado: fusión (sólido a líquido: hielo que se derrite), evaporación (líquido a gas: agua que hierve), condensación (gas a líquido: vapor que forma gotas). Causa: cambio de temperatura.',
    'Propiedades de los objetos: textura (suave, áspero, rugoso), peso (pesado, liviano) y flexibilidad (rígido, elástico). Propiedades ópticas: transparente (vidrio), translúcido (papel mantequilla) y opaco (madera).',
    'Fuentes de luz: naturales (Sol, estrellas, luciérnagas) y artificiales (bombillo, linterna, pantalla). El sonido como resultado de vibración. Ruidos fuertes vs suaves. Fuentes de sonido.',
    'El planeta Tierra: agua (ríos, mares, lagos), suelo (tierra, rocas, montañas) y aire (atmósfera). Importancia de cada recurso para la vida. Cómo cuidarlos.',
    'El día y la noche: presencia del Sol define el día (luz y calor), ausencia define la noche. Actividades diurnas y nocturnas de animales y personas.',
    'El clima y el tiempo atmosférico: soleado, lluvioso, nublado, ventoso, frío, caliente. Cómo el clima afecta la vestimenta, las actividades y los seres vivos.',
    'La cadena alimenticia básica: productor (plantas), consumidor primario (herbívoro), consumidor secundario (carnívoro) y descomponedor (hongos, bacterias). Construir cadenas simples.',
    'Fuerzas básicas: empujar y jalar para mover objetos. Concepto intuitivo de gravedad (los objetos caen). Flotación: por qué algunos objetos flotan y otros se hunden.',
    'Los recursos naturales: renovables (agua, aire, plantas, animales) y no renovables (petróleo, carbón, minerales). Acciones para cuidar el medio ambiente: ahorro de agua, no contaminar, reciclar.',
    'Repaso integral: seres vivos, cuerpo humano, materia y energía, tierra y universo. Preguntas de pensamiento científico: clasificar, comparar y explicar relaciones causa-efecto. Nivel grado 2 transición a grado 3.',
  ],
  SOC: [
    'El tiempo en mi vida: el PASADO es lo que ya pasó (cuando era bebé, ayer), el PRESENTE es lo que pasa ahora (hoy, este momento) y el FUTURO es lo que va a pasar (mañana, cuando sea grande). Ordenar eventos de la vida propia: primero nací, luego aprendí a caminar, después entré al colegio.',
    'Mi familia: en la familia hay personas que nos quieren y cuidan. Hay familias grandes y pequeñas. Los papás cuidan y protegen, los abuelos tienen más experiencia, los hermanos son compañeros de juego. Cada persona tiene un parentesco: papá, mamá, abuelos, tíos, primos.',
    'Cómo han cambiado las cosas: el teléfono de antes era grande y con cable, hoy es pequeño y sin cable. Los carros de antes eran lentos, hoy son rápidos. La gente de antes usaba cartas, hoy usa mensajes. Comparar el antes y el ahora en objetos cotidianos.',
    'Los símbolos de Colombia: la BANDERA tiene tres franjas — amarilla (riquezas del suelo), azul (ríos y mares) y roja (sangre de los héroes). El ESCUDO representa los recursos del país. El HIMNO es la canción oficial. Fechas importantes: 20 de julio (Independencia).',
    'Dónde estoy y hacia dónde voy: derecha, izquierda, adelante, atrás, arriba, abajo. Los cuatro puntos cardinales: Norte (N), Sur (S), Este (E), Oeste (O). El Sol sale por el Este cada mañana y se oculta por el Oeste cada tarde.',
    'Los planos y los mapas: un plano es un dibujo de un lugar visto desde arriba. Nos ayuda a saber dónde está cada cosa en una casa o un colegio. En los mapas, los símbolos representan lugares: una cruz roja = hospital, un libro = biblioteca. Los mapas tienen referencias para orientarse.',
    'El campo y la ciudad: en el CAMPO hay naturaleza, cultivos, animales de granja, silencio y casas separadas. En la CIUDAD hay edificios altos, mucho tráfico, tiendas, ruido y personas viviendo muy cerca. Las personas del campo y la ciudad se necesitan mutuamente.',
    'Mi barrio: en el barrio hay lugares importantes para todos — el parque para jugar, el hospital para cuidar la salud, el colegio para aprender, la tienda para comprar. En el barrio debemos respetarnos: no hacer ruido de noche, no botar basura en la calle.',
    'Las profesiones: los médicos curan enfermedades, los bomberos apagan incendios, los profesores enseñan, los agricultores cultivan la comida, los policías cuidan el orden. Cada profesión es importante para que la comunidad funcione bien.',
    'Las autoridades: en casa mandan los papás, en el colegio manda el rector, en la ciudad manda el alcalde, en el país manda el presidente. Las autoridades existen para que todos vivamos en orden y en paz.',
    'Los derechos de los niños: todos los niños tienen derecho a tener un nombre, a vivir en familia, a estudiar, a jugar, a recibir atención médica y a ser tratados con respeto. Nadie puede quitarles estos derechos.',
    'Los deberes de los niños: así como tenemos derechos, también tenemos deberes — estudiar, respetar a los demás, cuidar nuestras cosas y el colegio, ayudar en casa. Los derechos y los deberes van de la mano.',
    'Vivir juntos en paz: para convivir bien decimos "por favor", "gracias" y "disculpa". Pedimos la palabra antes de hablar, escuchamos cuando otro habla y no hacemos lo que nos haría daño a nosotros o a los demás.',
    'Resolver problemas sin pelear: cuando hay un conflicto, el diálogo es la mejor solución. Pasos: 1) calmarse, 2) escuchar al otro, 3) decir cómo me siento, 4) buscar una solución juntos. Nunca se resuelve un problema con golpes o gritos.',
    'El semáforo y las normas de tránsito: ROJO = parar, AMARILLO = precaución, VERDE = seguir. La cebra peatonal es para que los peatones crucen seguros. En la calle debemos caminar por el andén y mirar a los dos lados antes de cruzar.',
    'Cuidar el planeta: el agua es un recurso valioso — hay que cerrar la llave. Apagar la luz cuando no se usa ahorra energía. Reciclar significa separar la basura: papel, plástico, vidrio, orgánico. El planeta necesita nuestra ayuda.',
    'Los medios de transporte: terrestres (carro, bus, bicicleta, moto, tren), acuáticos (barco, canoa, lancha) y aéreos (avión, helicóptero, globo). Antes solo había caballos y carretas; hoy tenemos muchos más medios para movernos.',
    'Los medios de comunicación: el teléfono, la televisión, la radio, el periódico y el internet nos permiten comunicarnos y enterarnos de lo que pasa. Antes solo existían cartas y tambores. Debemos usar el internet con responsabilidad.',
    'Dónde vivimos: hay casas, apartamentos, cabañas y otros tipos de vivienda. Cada parte del hogar tiene una función: la cocina para cocinar, el cuarto para dormir, el baño para el aseo. Las casas se construyen con ladrillo, madera, cemento o paja.',
    'Repaso integral: tiempo histórico, orientación en el espacio, vida en comunidad y formación ciudadana. Preguntas mixtas de análisis y aplicación. Nivel grado 2 transición a grado 3.',
  ],
};

const NOMBRES_MATERIA = {
  MAT: 'Matemáticas',
  LCA: 'Lengua Castellana',
  ING: 'Inglés',
  NAT: 'Ciencias Naturales',
  SOC: 'Ciencias Sociales',
};

// ── Materias que requieren texto base (ninguna por ahora) ────────────
const MATERIAS_CON_TEXTO_BASE = {};

function necesitaTextoBase(mat, leccion) {
  const config = MATERIAS_CON_TEXTO_BASE[mat];
  if (!config) return false;
  return config.leccionesConTexto.includes(leccion);
}

function getAuth() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  return new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
}

function callOpenAI(prompt) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      model: 'gpt-4o-mini',
      max_tokens: 4000,
      temperature: 0.7,
      messages: [{ role: 'user', content: prompt }],
    });
    const options = {
      hostname: 'api.openai.com',
      path: '/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
        'Content-Length': Buffer.byteLength(body),
      },
    };
    const req = https.request(options, (r) => {
      let data = '';
      r.on('data', chunk => data += chunk);
      r.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          resolve(parsed.choices?.[0]?.message?.content || '');
        } catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// ── Verificador automático de respuestas ────────────────────────────
// Segunda llamada a la IA que revisa cada pregunta y corrige la respuesta
// si está mal marcada, antes de guardar en Sheets.
async function verificarRespuestas(preguntas, mat, nombreMateria) {
  const esIngles = mat === 'ING';

  const bloques = preguntas.map((p, i) => {
    return `PREGUNTA ${i + 1}:
Enunciado: ${p.pregunta}
A) ${p.opciones?.A}
B) ${p.opciones?.B}
C) ${p.opciones?.C}
D) ${p.opciones?.D}
Respuesta marcada: ${p.respuesta}`;
  }).join('\n\n');

  const instrIngles = esIngles
    ? 'Las preguntas son de inglés básico para niño de 7 años colombiano. Las preguntas están en español y las opciones son palabras en inglés. Verifica que la traducción marcada sea realmente correcta.'
    : '';

  const prompt = `Eres un profesor experto en ${nombreMateria} para niños de 7 años de Colombia (grado 2).
${instrIngles}

Tu tarea es revisar cada pregunta y verificar si la respuesta marcada es CORRECTA o no.

INSTRUCCIONES:
- Si la respuesta marcada ES correcta → escribe "OK"
- Si la respuesta marcada ES INCORRECTA → escribe la letra correcta (A, B, C o D)
- Si ninguna opción es correcta → escribe "X"
- Sé muy preciso. Comprueba cada respuesta como si fuera un examen real.

${bloques}

Responde ÚNICAMENTE con un JSON así (sin texto adicional, sin markdown):
{"correcciones": ["OK", "B", "OK", "C", "OK", "OK", "A", "OK", "OK", "OK", "OK", "D", "OK", "OK", "OK"]}

El array debe tener exactamente ${preguntas.length} elementos, uno por pregunta en orden.`;

  try {
    const raw = await callOpenAI(prompt);
    const clean = raw.replace(/```json|```/g, '').trim();
    const parsed = JSON.parse(clean);
    const correcciones = parsed.correcciones || [];

    let corregidas = 0;
    const preguntasCorregidas = preguntas.map((p, i) => {
      const corr = (correcciones[i] || 'OK').toString().trim().toUpperCase();
      if (corr === 'OK' || corr === 'X') return p; // X = problema grave, dejar como está
      if (['A','B','C','D'].includes(corr) && corr !== p.respuesta) {
        corregidas++;
        console.log(`Pregunta ${i+1}: respuesta corregida de ${p.respuesta} → ${corr}`);
        return { ...p, respuesta: corr };
      }
      return p;
    });

    console.log(`Verificación completada: ${corregidas} respuestas corregidas de ${preguntas.length}`);
    return preguntasCorregidas;

  } catch (e) {
    // Si el verificador falla, devolver las preguntas originales sin bloquear
    console.error('Error en verificación de respuestas (no bloqueante):', e.message);
    return preguntas;
  }
}

async function sheetExiste(sheets, nombre) {
  const meta = await sheets.spreadsheets.get({ spreadsheetId: SHEET_ID });
  return meta.data.sheets.some(s => s.properties.title === nombre);
}

async function crearHoja(sheets, nombre) {
  await sheets.spreadsheets.batchUpdate({
    spreadsheetId: SHEET_ID,
    requestBody: { requests: [{ addSheet: { properties: { title: nombre } } }] },
  });
}

// ── Temas de lecciones anteriores para el bloque de repaso ──────────
function temasRepaso(mat, leccionActual) {
  const curriculum = CURRICULO[mat] || [];
  const anteriores = curriculum.slice(0, leccionActual - 1);
  if (!anteriores.length) return [];
  const mezclados = anteriores.sort(() => Math.random() - 0.5);
  return mezclados.slice(0, Math.min(3, mezclados.length));
}

// ── Construir el prompt tipo Duolingo ────────────────────────────────
function buildPrompt(grado, mat, leccion, tema) {
  const conTexto = necesitaTextoBase(mat, leccion);
  const config = MATERIAS_CON_TEXTO_BASE[mat];
  const instrExtra = conTexto && config ? config.instruccionesExtra(leccion) : '';

  const temasAnteriores = leccion > 1 ? temasRepaso(mat, leccion) : [];
  const hayRepaso = temasAnteriores.length > 0;

  // ── Reglas especiales por materia ───────────────────────────────────
  const reglasIngles = mat === 'ING' ? `
REGLAS ESPECIALES PARA INGLÉS — OBLIGATORIAS:
- El niño es principiante absoluto (Duolingo Etapa 2, Sección 1, Score 10)
- TODAS las preguntas e instrucciones van escritas en ESPAÑOL
- Las palabras o frases en inglés solo aparecen dentro de la pregunta como dato o como opciones de respuesta
- NUNCA escribas una pregunta larga en inglés — máximo 5 palabras en inglés por pregunta
- Formato correcto: "¿Qué significa la palabra 'dog'?" / "¿Cómo se dice 'perro' en inglés?"
- Las 4 opciones son palabras sueltas en inglés (dog / cat / bird / fish)
- La explicación va 100% en español, en lenguaje muy simple para niño de 7 años
- VERIFICA que la opción marcada como correcta realmente sea la traducción correcta
` : '';

  const reglasLCA = mat === 'LCA' ? `
REGLAS ESPECIALES PARA LENGUA CASTELLANA — OBLIGATORIAS:
- El niño tiene 7 años — NUNCA uses términos técnicos como "núcleo del sujeto", "predicado nominal", "conector adversativo" o "morfema"
- En su lugar usa lenguaje cotidiano: "la parte que dice quién", "la palabra que une", "la palabra de acción"
- Las preguntas deben usar oraciones sobre animales, juguetes, comida, el colegio o la familia
- Si el tema involucra una regla, EXPLÍCALA en la pregunta antes de preguntar (no asumas que ya la sabe)
- Las preguntas tipo "completar" son mejores que las teóricas para este nivel
` : '';

  // ── Estructura progresiva tipo Duolingo ─────────────────────────────
  const bloqueRepaso = hayRepaso ? `
BLOQUE C — REPASO (preguntas 11 a 15):
Repasa temas de lecciones anteriores. Más cortas y directas.
Temas anteriores disponibles:
${temasAnteriores.map((t, i) => `- ${t.substring(0, 100)}...`).join('\n')}` : '';

  const estructura = hayRepaso
    ? `ESTRUCTURA OBLIGATORIA — 15 preguntas en 3 bloques progresivos:

BLOQUE A — APRENDE (preguntas 1 a 5): ⭐ MÁS FÁCILES
El niño NO ha visto este tema antes. Cada pregunta debe ENSEÑAR mientras pregunta.
- Incluir un ejemplo o mini-explicación dentro del enunciado de la pregunta
- Respuestas directas y obvias si se leyó bien el enunciado
- Contexto: situaciones de la vida diaria del niño (casa, colegio, animales, familia)
- Ejemplo de estructura: "En español, las palabras de acción se llaman verbos. ¿Cuál de estas es una palabra de acción?" 

BLOQUE B — PRACTICA (preguntas 6 a 10): ⭐⭐ DIFICULTAD MEDIA
El niño ya vio el concepto en el Bloque A. Ahora lo aplica.
- Sin explicación en el enunciado — confía en lo aprendido antes
- Situaciones reales o pequeñas historias de 1-2 oraciones
- Un distractor muy creíble (error típico de niños de 7 años)
${bloqueRepaso}`
    : `ESTRUCTURA OBLIGATORIA — 15 preguntas en 3 bloques progresivos:

BLOQUE A — APRENDE (preguntas 1 a 5): ⭐ MÁS FÁCILES
Enseña el concepto mientras pregunta. Incluir mini-explicación o ejemplo en el enunciado.

BLOQUE B — PRACTICA (preguntas 6 a 10): ⭐⭐ DIFICULTAD MEDIA
Aplica el concepto en situaciones reales. Sin explicación en el enunciado.

BLOQUE C — RAZONA (preguntas 11 a 15): ⭐⭐⭐ MÁS DIFÍCILES
Situaciones más elaboradas. El niño debe pensar más. Un solo distractor muy creíble.`;

  const campoContexto = conTexto
    ? `\n      "contexto": "TEXTO COMPLETO aquí (el MISMO en todas las preguntas del bloque nuevo)",`
    : '';

  const instrContexto = conTexto ? `
⚠️ REGLA CRÍTICA: Esta lección usa COMPRENSIÓN LECTORA.
1. Inventa UN SOLO texto de 120-180 palabras para niños de 7-8 años
2. Pon ese texto completo en el campo "contexto" de las preguntas 1 a 10
3. Las preguntas 11-15 de repaso NO llevan contexto
4. El texto debe tener personajes con nombre, lugar y acciones claras
${instrExtra}` : '';

  return `Eres un profesor experto creando preguntas de examen estilo DUOLINGO para un niño de 7 años (grado ${grado}, Colombia).

TEMA DE ESTA LECCIÓN: ${tema}
MATERIA: ${NOMBRES_MATERIA[mat] || mat}
${instrContexto}
${reglasIngles}
${reglasLCA}

${estructura}

REGLAS OBLIGATORIAS PARA TODAS LAS PREGUNTAS:
1. Lenguaje MUY simple — como le hablarías a un niño de 7 años en el recreo
2. 4 opciones (A, B, C, D), UNA sola correcta
3. Sin LaTeX ni símbolos raros. Usar texto plano: 3/4, raiz(16), 2x3
4. Distractores CREÍBLES pero claramente incorrectos para quien leyó bien
5. Distribución de respuestas correctas: A×4, B×4, C×4, D×3 — SIN PATRÓN visible (no pongas todas las respuestas en A o en B)
6. ⚠️ VERIFICACIÓN OBLIGATORIA: antes de escribir cada pregunta, confirma que la opción marcada como "respuesta" ES REALMENTE LA CORRECTA. Comprueba mentalmente: si un niño elige esa opción, ¿está bien?
7. La explicación debe decirle al niño POR QUÉ esa respuesta es correcta, en 1-2 oraciones simples
8. Devuelve ÚNICAMENTE JSON válido, sin texto adicional ni bloques markdown

Formato JSON exacto:
{
  "preguntas": [
    {
      "pregunta": "texto de la pregunta",${campoContexto}
      "opciones": { "A": "opción a", "B": "opción b", "C": "opción c", "D": "opción d" },
      "respuesta": "B",
      "explicacion": "explicación simple en 1-2 oraciones para el niño de 7 años"
    }
  ]
}`;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'Método no permitido' });

  const { grado, materia, leccion } = req.body;
  if (!grado || !materia || !leccion) {
    return res.status(400).json({ ok: false, error: 'Faltan grado, materia o leccion' });
  }

  const mat = materia.toUpperCase();
  const lNum = parseInt(leccion);
  const lStr = String(lNum).padStart(2, '0');
  const sheetName = `G${grado}_${mat}_L${lStr}`;
  const tema = CURRICULO[mat]?.[lNum - 1];

  if (!tema) {
    return res.status(400).json({ ok: false, error: `No hay tema definido para ${mat} lección ${lNum}` });
  }

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    // Verificar si la hoja ya existe y tiene contenido
    const existe = await sheetExiste(sheets, sheetName);
    if (existe) {
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: `${sheetName}!A2:I20`,
        valueRenderOption: 'UNFORMATTED_VALUE',
      });
      if ((r.data.values || []).length > 0) {
        return res.json({ ok: true, sheetName, generado: false, mensaje: 'Ya existía' });
      }
    }

    // Construir prompt y llamar a OpenAI
    const prompt = buildPrompt(grado, mat, lNum, tema);
    const raw = await callOpenAI(prompt);

    let parsed;
    try {
      const clean = raw.replace(/```json|```/g, '').trim();
      parsed = JSON.parse(clean);
    } catch (e) {
      return res.status(500).json({ ok: false, error: 'OpenAI devolvió JSON inválido', raw });
    }

    let preguntas = parsed.preguntas || [];
    if (preguntas.length < 10) {
      return res.status(500).json({ ok: false, error: `Solo ${preguntas.length} preguntas generadas`, raw });
    }

    // ── Segunda pasada: verificar y corregir respuestas incorrectas ──
    preguntas = await verificarRespuestas(preguntas, mat, NOMBRES_MATERIA[mat] || mat);

    const conTexto = necesitaTextoBase(mat, lNum);

    const rows = preguntas.map(p => {
      let enunciado = p.pregunta || '';
      if (conTexto && p.contexto) {
        enunciado = `📖 ${p.contexto}\n\n❓ ${p.pregunta}`;
      }
      return [
        enunciado,
        p.opciones?.A || '',
        p.opciones?.B || '',
        p.opciones?.C || '',
        p.opciones?.D || '',
        (p.respuesta || 'A').toUpperCase(),
        '',                    // G: imagen
        '',                    // H: video
        p.explicacion || '',   // I: explicación popup
      ];
    });

    // Crear hoja si no existía
    if (!existe) await crearHoja(sheets, sheetName);

    // Escribir en el Sheet
    await sheets.spreadsheets.values.update({
      spreadsheetId: SHEET_ID,
      range: `${sheetName}!A2:I${rows.length + 1}`,
      valueInputOption: 'RAW',
      requestBody: { values: rows },
    });

    return res.json({
      ok: true,
      sheetName,
      generado: true,
      total: preguntas.length,
      tema,
      conTextoBase: conTexto,
    });

  } catch (e) {
    console.error('Error generar-leccion:', e);
    return res.status(500).json({ ok: false, error: e.message });
  }
};
