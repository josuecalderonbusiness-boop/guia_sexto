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

// ── Currículo completo de Tomás (grado 6) ───────────────────────────
const CURRICULO_G6 = {
  MAT: [
    'Números enteros: positivos, negativos y el cero. Representación en la recta numérica. Orden y comparación de enteros. Valor absoluto. Opuesto de un número. Situaciones reales: temperatura bajo cero, deudas, pisos bajo tierra.',
    'Operaciones con números enteros: suma y resta de enteros con regla de signos. Casos: positivo+positivo, negativo+negativo, signos diferentes. Multiplicación y división: signo del resultado según combinación de signos. Jerarquía de operaciones con enteros.',
    'Números racionales: concepto de fracción como parte de un todo y como cociente. Fracciones propias, impropias y números mixtos. Equivalencia y simplificación de fracciones. Comparación con signo mayor, menor e igual.',
    'Operaciones con fracciones: suma y resta con igual y diferente denominador (mínimo común múltiplo). Multiplicación de fracciones. División de fracciones (multiplicar por el inverso). Problemas verbales con fracciones.',
    'Números decimales: lectura y escritura hasta milésimas. Conversión entre fracciones y decimales. Operaciones: suma, resta, multiplicación y división de decimales. Redondeo y aproximación.',
    'Potenciación: base, exponente y potencia. Potencias de 10. Cuadrados y cubos perfectos. Raíz cuadrada exacta y aproximada. Notación científica básica.',
    'Múltiplos y divisores: criterios de divisibilidad (2, 3, 5, 10). Números primos y compuestos. Descomposición en factores primos. Mínimo Común Múltiplo (MCM) y Máximo Común Divisor (MCD) con descomposición.',
    'Razones y proporciones: concepto de razón como comparación. Proporción: términos y propiedad fundamental. Proporcionalidad directa e inversa. Regla de tres simple directa e inversa. Aplicaciones en recetas, mapas y velocidad.',
    'Porcentajes: concepto como fracción de 100. Conversión porcentaje-fracción-decimal. Calcular el porcentaje de una cantidad. Porcentaje de aumento y descuento. Aplicaciones: descuentos en tiendas, notas escolares.',
    'Álgebra básica: expresiones algebraicas. Variables, coeficientes y términos. Operaciones con monomios: suma, resta y multiplicación. Valor numérico de una expresión. Ecuaciones lineales de una variable: resolución y verificación.',
    'Geometría plana: ángulos (agudo, recto, obtuso, llano, completo). Clasificación de triángulos por lados y ángulos. Suma de ángulos internos de un triángulo. Cuadriláteros: paralelogramos, rectángulo, rombo, trapecio.',
    'Perímetro y área: fórmulas de figuras planas (cuadrado, rectángulo, triángulo, círculo). Número Pi. Circunferencia y área del círculo. Problemas de aplicación con unidades de medida.',
    'Estadística: recolección y organización de datos. Tablas de frecuencia. Gráficas de barras, circulares y de líneas. Medidas de tendencia central: media aritmética, mediana y moda. Interpretación de gráficas.',
    'Probabilidad: experimento aleatorio, espacio muestral y evento. Probabilidad simple: número de casos favorables sobre total de posibles. Escala de 0 a 1. Eventos seguros, posibles e imposibles.',
    'Pensamiento métrico: unidades de longitud (mm, cm, m, km), masa (g, kg, ton), capacidad (ml, l) y tiempo. Conversión entre unidades. Perímetro y área en problemas del mundo real. Escala en mapas.',
    'Sistemas de coordenadas: plano cartesiano, ejes X e Y, cuadrantes. Ubicar y leer puntos en los cuatro cuadrantes. Distancia entre dos puntos con la misma coordenada. Aplicaciones en mapas y gráficas.',
    'Transformaciones geométricas: traslación, reflexión y rotación en el plano cartesiano. Figuras congruentes y semejantes. Eje de simetría. Aplicaciones en arte y diseño.',
    'Sólidos geométricos: prismas, pirámides, cilindros, conos y esferas. Elementos: caras, aristas y vértices. Fórmulas de volumen de prismas y cilindros. Superficie lateral y total del prisma rectangular.',
    'Repaso numérico y algebraico: enteros, fracciones, decimales, potencias, razones, porcentajes y ecuaciones. Problemas integrados de varios pasos.',
    'Repaso geométrico y estadístico: ángulos, figuras planas, coordenadas, transformaciones, sólidos, estadística y probabilidad. Problemas de aplicación nivel grado 6.',
  ],
  LEN: [
    'La comunicación: elementos del proceso comunicativo (emisor, receptor, mensaje, canal, código, contexto). Funciones del lenguaje: referencial, expresiva, apelativa, poética, fática y metalingüística. Identificar función en textos cortos.',
    'Comprensión lectora nivel literal: identificar información explícita en el texto. Preguntas de quién, qué, cuándo, dónde y cómo. Idea principal e ideas secundarias. Secuencia de eventos. Vocabulario en contexto.',
    'Comprensión lectora nivel inferencial: deducir información no dicha directamente. Inferir el propósito del autor. Identificar el tema central. Relaciones causa-efecto implícitas. Significado de palabras por contexto.',
    'Comprensión lectora nivel crítico: opinión del lector sobre el texto. Identificar punto de vista y posición del autor. Distinguir hecho de opinión. Evaluar argumentos. Relacionar el texto con experiencias propias.',
    'Géneros literarios: narrativo (cuento, novela, fábula, mito, leyenda, epopeya). Lírico (poema, oda, elegía, soneto). Dramático (obra de teatro, monólogo, diálogo). Características y elementos de cada género.',
    'El texto narrativo: narrador (primera persona, omnisciente, testigo, segunda persona). Personajes (principal, secundario, antagonista). Estructura: planteamiento, nudo y desenlace. Tiempo y espacio en la narración.',
    'La poesía: verso y estrofa. Rima consonante y asonante. Figuras literarias: metáfora, símil, personificación, hipérbole, aliteración y anáfora. Identificar y analizar figuras en poemas.',
    'El texto dramático: estructura (actos y escenas). Acotaciones escénicas. Diálogo y monólogo. Diferencias entre texto dramático y representación. Elementos del teatro: escenografía, personajes, conflicto.',
    'Tipos de texto: narrativo, descriptivo, expositivo, argumentativo e instructivo. Características de cada tipo. Identificar el tipo de texto según su propósito comunicativo. Estructura interna de cada tipo.',
    'La descripción: descripción de personas (prosopografía, etopeya, retrato). Descripción de lugares y objetos. Uso de adjetivos y recursos descriptivos. Orden espacial y lógico en la descripción.',
    'Clases de palabras: sustantivo (género, número, tipos). Adjetivo (calificativo, determinativo, grado). Verbo (persona, número, tiempo, modo). Adverbio. Pronombre. Preposición. Conjunción. Interjección.',
    'El verbo: modos verbales (indicativo, subjuntivo, imperativo). Tiempos del indicativo: presente, pretérito perfecto simple, pretérito imperfecto, futuro. Conjugación de verbos regulares e irregulares comunes.',
    'Ortografía: uso de b/v, c/s/z, g/j, h, ll/y, r/rr, x. Acento ortográfico: palabras agudas, graves y esdrújulas. Tilde diacrítica básica (más/mas, sí/si, él/el). Signos de puntuación: coma, punto, dos puntos, punto y coma.',
    'La oración: sujeto (núcleo y modificadores) y predicado (verbo y complementos). Tipos de oración según la actitud del hablante: enunciativa, interrogativa, exclamativa, imperativa y dubitativa. Concordancia sujeto-verbo.',
    'El párrafo: oración temática y oraciones de apoyo. Coherencia y cohesión textual. Conectores lógicos: adición (además, también), oposición (pero, sin embargo), causa (porque, ya que), consecuencia (por lo tanto).',
    'Textos informativos: la noticia (qué, quién, cuándo, dónde, cómo, por qué). El artículo de opinión. El reportaje. El informe. Características y estructura de cada uno. Identificar fuentes de información.',
    'Sinonimia, antonimia, polisemia y homonimia. Campo semántico y campo léxico. Familia de palabras: raíz, prefijos y sufijos. Formación de palabras: composición y derivación.',
    'El texto argumentativo: tesis, argumentos y conclusión. Tipos de argumentos: de autoridad, de ejemplo, estadístico, de analogía. Identificar la posición del autor. Contraargumentos. Escribir un párrafo argumentativo.',
    'Producción textual: pasos del proceso de escritura (planear, redactar, revisar, corregir). Coherencia (unidad temática) y cohesión (conectores, sinónimos, pronombres). Escribir textos cortos con propósito definido.',
    'Repaso integral: comprensión lectora (literal, inferencial, crítico), géneros literarios, gramática, ortografía y producción textual. Preguntas tipo Prueba Saber nivel grado 6.',
  ],
  BIO: [
    'La célula: unidad básica de la vida. Célula procariota (sin núcleo definido, ej: bacterias) y eucariota (con núcleo, ej: animales y plantas). Partes de la célula eucariota: membrana, citoplasma, núcleo, mitocondria, ribosoma. Célula animal vs vegetal.',
    'Tejidos, órganos y sistemas: niveles de organización del ser vivo. Tejido epitelial, muscular, nervioso y conectivo. Ejemplos de órganos: corazón, pulmón, estómago. Diferencia entre órgano y sistema. Homeostasis básica.',
    'Sistema digestivo: boca, faringe, esófago, estómago, intestino delgado, intestino grueso. Proceso de digestión mecánica y química. Absorción de nutrientes. Función del hígado y páncreas en la digestión.',
    'Sistema circulatorio: corazón (aurículas y ventrículos), arterias, venas y capilares. Circulación mayor y menor. El papel de los glóbulos rojos, glóbulos blancos y plaquetas. Presión arterial básica.',
    'Sistema respiratorio: fosas nasales, faringe, laringe, tráquea, bronquios y pulmones. Proceso de inspiración y espiración. Intercambio gaseoso en los alvéolos: oxígeno entra, dióxido de carbono sale.',
    'Sistema nervioso: sistema nervioso central (encéfalo y médula espinal) y periférico. Neurona: estructura y función. Arco reflejo. Sistema nervioso autónomo. Importancia del sueño para el sistema nervioso.',
    'Sistema óseo y muscular: funciones del esqueleto (soporte, protección, movimiento). Tipos de huesos. Articulaciones: fijas, semimóviles y móviles. Músculo esquelético, liso y cardíaco. Relación hueso-músculo en el movimiento.',
    'Sistema excretor: riñones, uréteres, vejiga y uretra. Formación de la orina. Función del sudor y los pulmones como vías excretoras. Importancia de la hidratación.',
    'Nutrición en los seres vivos: autótrofos (fotosíntesis) y heterótrofos (herbívoros, carnívoros, omnívoros, detritívoros). Macronutrientes: carbohidratos, proteínas y lípidos. Micronutrientes: vitaminas y minerales. Dieta equilibrada.',
    'Fotosíntesis: cloroplasto y clorofila. Ecuación de la fotosíntesis: CO2 + H2O + luz → glucosa + O2. Factores que la afectan: luz, CO2 y temperatura. Importancia para la vida en la Tierra.',
    'Reproducción: asexual (fisión binaria, gemación, esporulación, reproducción vegetativa) y sexual (fertilización interna y externa). Reproducción humana: sistema reproductor masculino y femenino básico. Fecundación y desarrollo embrionario.',
    'Clasificación de los seres vivos: criterios de clasificación. Cinco reinos: Monera, Protista, Fungi, Plantae, Animalia. Características de cada reino. Sistema binomial de nomenclatura de Linneo. Taxonomía básica.',
    'Ecosistemas: componentes bióticos (productores, consumidores, descomponedores) y abióticos (luz, agua, temperatura, suelo). Tipos de ecosistemas: terrestre (bosque, desierto, pradera) y acuático (marino, dulceacuícola).',
    'Cadenas y redes alimenticias: productor → consumidor primario → secundario → terciario → descomponedor. Flujo de energía. Pirámides ecológicas de número, biomasa y energía. Impacto de la extinción de un eslabón.',
    'Ciclos biogeoquímicos: ciclo del agua (evaporación, condensación, precipitación, escorrentía). Ciclo del carbono (fotosíntesis, respiración, combustión). Ciclo del nitrógeno básico. Importancia para los ecosistemas.',
    'Biomas del mundo: tropical húmedo, desierto, sabana, bosque templado, taiga, tundra y océano. Características climáticas y biodiversidad de cada bioma. Biomas de Colombia: Amazonía, Orinoquia, Andes, Pacífico, Caribe.',
    'Genética básica: ADN como portador de información genética. Gen, cromosoma y genoma. Concepto de herencia. Rasgos dominantes y recesivos. Cuadro de Punnett simple. Ejemplos: color de ojos, grupo sanguíneo.',
    'Evolución: Darwin y la selección natural. Adaptación al ambiente. Fósiles como evidencia de evolución. Homología y analogía. Árbol filogenético básico. Extinción de especies: causas naturales y humanas.',
    'Salud y enfermedad: enfermedades infecciosas (bacterianas, virales, parasitarias) y no infecciosas (crónicas, genéticas). Sistema inmunológico: barreras físicas, respuesta inespecífica y específica. Vacunas y antibióticos.',
    'Ecología y medio ambiente: problemas ambientales (deforestación, contaminación, cambio climático, pérdida de biodiversidad). Desarrollo sostenible. Acciones individuales y colectivas para proteger el ambiente. Áreas protegidas en Colombia.',
  ],
  QUI: [
    'La materia: definición y propiedades generales (masa, volumen, densidad, inercia). Propiedades específicas: punto de fusión, punto de ebullición, solubilidad, conductividad eléctrica y térmica. Métodos para medir propiedades.',
    'Estados de la materia: sólido (forma y volumen definidos, partículas muy juntas), líquido (volumen definido, fluye) y gaseoso (sin forma ni volumen fijos). Estado plasma. Cambios de estado: fusión, solidificación, evaporación, condensación, sublimación.',
    'Cambios físicos y químicos: cambios físicos (no cambia la composición: romper, disolver, cambiar de estado). Cambios químicos (nueva sustancia: oxidación, combustión, fermentación). Evidencias de cambio químico: color, olor, gas, precipitado, luz o calor.',
    'Mezclas: homogéneas (soluciones: soluto + solvente, ej: agua con sal) y heterogéneas (fases visibles, ej: agua con arena). Métodos de separación: filtración, decantación, evaporación, destilación, cristalización, imantación, tamización.',
    'Sustancias puras: elementos (un solo tipo de átomo, ej: O₂, Fe) y compuestos (átomos diferentes combinados, ej: H₂O, NaCl). Diferencia entre mezcla y compuesto. Ley de composición definida.',
    'El átomo: partículas subatómicas (protón +, neutrón 0, electrón -). Número atómico (Z) y número másico (A). Isótopos. Modelo atómico de Bohr: niveles de energía y electrones de valencia.',
    'La tabla periódica: historia y organización. Periodos y grupos. Metales, no metales y metaloides. Propiedades periódicas: electronegatividad, radio atómico, energía de ionización. Elementos más comunes en la naturaleza.',
    'El enlace químico: por qué los átomos se unen (regla del octeto). Enlace iónico (metal + no metal, transferencia de electrones, ej: NaCl). Enlace covalente (no metal + no metal, compartir electrones, ej: H₂O, CO₂). Enlace metálico básico.',
    'Fórmulas y nomenclatura química básica: fórmula molecular vs empírica. Nomenclatura de óxidos básicos (metal + O₂). Nomenclatura de hidróxidos (metal + OH). Nomenclatura de ácidos básicos (H + no metal). Lectura de fórmulas comunes.',
    'Reacciones químicas: reactivos y productos. Ley de conservación de la masa (Lavoisier). Balanceo de ecuaciones simples por tanteo. Tipos de reacción: síntesis, descomposición, sustitución simple y doble sustitución.',
    'El agua: molécula polar (H₂O). Propiedades del agua: cohesión, adhesión, tensión superficial, calor específico alto. El agua como solvente universal. Ciclo del agua. Contaminación del agua y tratamiento básico.',
    'Ácidos y bases: concepto de Arrhenius. Propiedades de los ácidos (sabor agrio, corrosivos, pH<7) y las bases (sabor amargo, resbaladizos, pH>7). Escala de pH de 0 a 14. Indicadores: papel tornasol y fenolftaleína. Neutralización.',
    'Soluciones: soluto y solvente. Tipos de solución: diluida, concentrada, saturada y sobresaturada. Formas de expresar concentración: porcentaje en masa, partes por millón (ppm). Factores que afectan la solubilidad.',
    'Metales y no metales: propiedades de los metales (brillo, maleabilidad, ductilidad, conductividad). No metales: propiedades opuestas. Metaloides: propiedades intermedias. Usos cotidianos de metales (hierro, aluminio, cobre, oro).',
    'Carbono y compuestos orgánicos básicos: propiedades únicas del carbono (tetravalente, forma cadenas). Hidrocarburos: alcanos, alquenos y alquinos (concepto). Grupos funcionales básicos: alcohol (-OH), ácido carboxílico (-COOH). Importancia en la vida.',
    'Combustión: reacción de un combustible con oxígeno que produce CO₂, H₂O y energía. Combustión completa vs incompleta. Combustibles fósiles: petróleo, carbón y gas natural. Impacto ambiental de la combustión.',
    'Oxidación y corrosión: reacción del metal con el oxígeno del aire. Óxido de hierro (herrumbre). Factores que aceleran la corrosión: humedad, sal. Métodos de protección: pintura, galvanizado, recubrimiento. Oxidación en alimentos.',
    'Energía química: la energía almacenada en los enlaces químicos. Reacciones exotérmicas (liberan energía, ej: combustión) y endotérmicas (absorben energía, ej: fotosíntesis). Energía de activación. Catalizadores.',
    'Química y vida cotidiana: jabón y detergente (moléculas anfipáticas, emulsificación). Medicamentos como compuestos químicos. Plásticos: polímeros básicos. Fertilizantes y pesticidas: uso y riesgos. Química verde y sostenibilidad.',
    'Repaso integral: materia, cambios, mezclas, sustancias puras, átomo, tabla periódica, enlaces, reacciones, ácidos y bases, y química cotidiana. Preguntas tipo Prueba Saber nivel grado 6.',
  ],
  SOC: [
    'La Tierra en el universo: el sistema solar, planetas y sus características. Movimientos de la Tierra: rotación (día y noche) y traslación (estaciones). Coordenadas geográficas: latitud y longitud. Husos horarios.',
    'Mapas y cartografía: elementos del mapa (título, escala, convenciones, rosa de los vientos). Tipos de mapa: político, físico, temático. Escala numérica y gráfica. Proyecciones cartográficas básicas. Lectura e interpretación de mapas.',
    'Relieve terrestre: capas de la Tierra (corteza, manto, núcleo externo e interno). Placas tectónicas y deriva continental. Formación de montañas, volcanes y terremotos. Relieve colombiano: cordilleras, valles, llanuras y costas.',
    'Clima y tiempo atmosférico: factores del clima (latitud, altitud, corrientes marinas, vientos). Elementos del clima: temperatura, precipitación, humedad, presión, vientos. Zonas climáticas de la Tierra. Climas de Colombia.',
    'Hidrografía: el ciclo hidrológico. Cuencas hidrográficas de Colombia (Magdalena, Cauca, Amazonas, Orinoco, Atrato). Mares que rodean a Colombia: Caribe y Pacífico. Importancia de los ríos para el desarrollo.',
    'Regiones naturales de Colombia: Caribe, Pacífica, Andina, Orinoquía, Amazonía e Insular. Características físicas, clima, flora, fauna y población de cada región. Importancia de la biodiversidad colombiana.',
    'Población: concepto de demografía. Natalidad, mortalidad y crecimiento natural. Migración: interna y externa. Densidad de población. Distribución de la población en Colombia. Etnias: mestizos, indígenas, afrocolombianos, raizales.',
    'Culturas precolombinas: grandes civilizaciones de América (Mayas, Aztecas, Incas). Características culturales, económicas y políticas. Culturas indígenas de Colombia: Muiscas, Taironas, Quimbayas. Legado cultural precolombino.',
    'La Conquista española: llegada de Colón en 1492. Proceso de conquista de América. La Conquista de Colombia: Gonzalo Jiménez de Quesada y fundación de Bogotá. Consecuencias para los pueblos indígenas. El sistema de encomienda.',
    'La Colonia en Colombia: organización política (Virreinato de la Nueva Granada). Sociedad colonial: españoles, criollos, mestizos, indígenas y esclavos africanos. Economía colonial: minería, agricultura y comercio. La Iglesia en la Colonia.',
    'Independencia de Colombia: causas (Ilustración, Revolución Francesa, independencia de EE.UU., crisis española). El Grito de Independencia del 20 de julio de 1810. Principales líderes: Simón Bolívar, Francisco de Paula Santander, Antonio Nariño. Batallas clave.',
    'Formación de la República: La Gran Colombia y su disolución. República de la Nueva Granada. Conflictos entre federalistas y centralistas. Constituciones del siglo XIX. La Regeneración y la Constitución de 1886.',
    'Colombia en el siglo XX: La Guerra de los Mil Días. La separación de Panamá (1903). La Violencia (1948). El Frente Nacional. El narcotráfico y sus consecuencias. La Constitución de 1991: derechos y participación ciudadana.',
    'Organización del Estado colombiano: Constitución de 1991. Ramas del poder público: Ejecutiva (Presidente), Legislativa (Congreso) y Judicial (Cortes). Organismos de control. Entidades territoriales: municipios, departamentos.',
    'Derechos humanos: Declaración Universal de los Derechos Humanos. Derechos fundamentales en la Constitución colombiana. Mecanismos de protección: tutela, derecho de petición, habeas corpus. Responsabilidades ciudadanas.',
    'Economía básica: necesidades y bienes. Factores de producción: tierra, trabajo y capital. Sectores económicos: primario (agricultura, minería), secundario (industria) y terciario (servicios). Economía de Colombia: exportaciones e importaciones.',
    'Globalización e interdependencia: qué es la globalización. Organismos internacionales: ONU, OEA, FMI, Banco Mundial. Tratados de libre comercio. Ventajas y desventajas de la globalización. Colombia en el contexto mundial.',
    'Problemas sociales en Colombia: pobreza y desigualdad. Desplazamiento forzado. Conflicto armado interno. Proceso de paz. Retos del posconflicto. Organizaciones sociales y movimientos ciudadanos.',
    'Medio ambiente y desarrollo sostenible: problemas ambientales globales (cambio climático, deforestación, contaminación). Acuerdos internacionales: Protocolo de Kioto, Acuerdo de París. Colombia: biodiversidad y recursos naturales. Desarrollo sostenible.',
    'Repaso integral: geografía física y humana, historia de Colombia, organización política, economía y problemas sociales. Preguntas tipo Prueba Saber nivel grado 6.',
  ],
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

function callGemini(prompt) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: {
        temperature: 0.4,
        maxOutputTokens: 16000,
      }
    });
    const apiKey = process.env.GEMINI_API_KEY;
    const path = `/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
    const options = {
      hostname: 'generativelanguage.googleapis.com',
      path,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
      },
    };
    const req = https.request(options, (r) => {
      let data = '';
      r.on('data', chunk => data += chunk);
      r.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          const text = parsed.candidates?.[0]?.content?.parts?.[0]?.text || '';
          resolve(text);
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

  const nivelStr = mat === 'MAT' || mat === 'LEN' || mat === 'BIO' || mat === 'QUI'
    ? 'estudiantes de 11-12 años de Colombia (grado 6)'
    : 'niños de 7 años de Colombia (grado 2)';
  const prompt = `Eres un profesor experto en ${nombreMateria} para ${nivelStr}.
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
    const raw = await callGemini(prompt);
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
        const opcionCorrecta = p.opciones?.[corr] || '';
        const nuevaExplicacion = `La respuesta correcta es ${corr}) "${opcionCorrecta}". ${p.explicacion || ''}`;
        return { ...p, respuesta: corr, explicacion: nuevaExplicacion };
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
function temasRepaso(mat, leccionActual, grado) {
  const curriculoBase = grado === 6 ? CURRICULO_G6 : CURRICULO;
  const curriculum = curriculoBase[mat] || [];
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

  const temasAnteriores = leccion > 1 ? temasRepaso(mat, leccion, grado) : [];
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
    ? `ESTRUCTURA OBLIGATORIA — 10 preguntas en 2 bloques progresivos:

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

BLOQUE B — PRACTICA (preguntas 6 a 10): ⭐⭐ DIFICULTAD MEDIA
Aplica el concepto en situaciones reales. Sin explicación en el enunciado.`;

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
5. Distribución de respuestas correctas: A×3, B×3, C×2, D×2 — SIN PATRÓN visible (no pongas todas las respuestas en A o en B)
6. ⚠️ VERIFICACIÓN OBLIGATORIA pregunta por pregunta: ANTES de escribir la "respuesta", lee las 4 opciones y confirma cuál es la correcta. Escribe primero la opción correcta en su lugar (A, B, C o D) y luego escribe la explicación basada en ESA opción.
7. La explicación debe mencionar EXPLÍCITAMENTE la opción correcta: "La respuesta es [letra]) [texto de la opción] porque..." — NUNCA expliques una opción diferente a la marcada en "respuesta".
8. TRAMPA FRECUENTE A EVITAR: si marcas "respuesta": "B", la explicación debe hablar de la opción B, no de A, C o D.
9. El campo "tip" es un concepto de ayuda ANTES de responder: define el concepto clave de la pregunta en 1-2 oraciones simples con un ejemplo corto. Ejemplo: "El valor absoluto es la distancia de un número al cero, siempre positiva. Ejemplo: |−5| = 5 y |5| = 5."
8. Devuelve ÚNICAMENTE JSON válido, sin texto adicional ni bloques markdown

Formato JSON exacto:
{
  "preguntas": [
    {
      "pregunta": "texto de la pregunta",${campoContexto}
      "opciones": { "A": "opción a", "B": "opción b", "C": "opción c", "D": "opción d" },
      "respuesta": "B",
      "explicacion": "explicación simple en 1-2 oraciones para el niño de 7 años",
      "tip": "concepto clave en 1-2 oraciones con un ejemplo corto"
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
  const curriculoActivo = parseInt(grado) === 6 ? CURRICULO_G6 : CURRICULO;
  const tema = curriculoActivo[mat]?.[lNum - 1];

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
    const raw = await callGemini(prompt);

    let parsed;
    try {
      // Extraer JSON aunque Gemini agregue texto antes o después
      let clean = raw.replace(/```json|```/g, '').trim();
      // Buscar el primer { y el último } para extraer solo el JSON
      const start = clean.indexOf('{');
      const end = clean.lastIndexOf('}');
      if (start !== -1 && end !== -1) clean = clean.slice(start, end + 1);
      parsed = JSON.parse(clean);
    } catch (e) {
      return res.status(500).json({ ok: false, error: 'Gemini devolvió JSON inválido', raw });
    }

    let preguntas = parsed.preguntas || [];
    if (preguntas.length < 5) {
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
        p.tip || '',           // J: tip de ayuda
      ];
    });

    // Crear hoja si no existía
    if (!existe) await crearHoja(sheets, sheetName);

    // Escribir en el Sheet
    await sheets.spreadsheets.values.update({
      spreadsheetId: SHEET_ID,
      range: `${sheetName}!A2:J${rows.length + 1}`,
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

