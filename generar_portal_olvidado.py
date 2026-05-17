import json
import os
import urllib.request

# ── CONFIGURACION ─────────────────────────────────────────────────────
SHEET_ID  = '136hBOy2daTJy3-rcNyrumBhbqroniMrvYWPz8ueN9yg'
KEY_FILE  = r'C:\Users\Usuario\Downloads\examen-ninos-fd3bf54ba69e.json'
OPENAI_KEY = os.environ.get('OPENAI_API_KEY', '')

SERIE = 'El Portal Olvidado'
COLOR = '#0F0F2E'

CAPITULOS = [
    {
        'num': 1,
        'titulo': 'La Llave Sin Puerta',
        'resumen': 'Mateo, un nino de 9 anos curioso y solitario, encuentra en el fondo de su mochila una llave oxidada que jura no haber visto nunca. En el colegio conoce a Isla, una nina nueva con ojos de distinto color, que al ver la llave palidece y susurra: eso no deberia estar aqui. Esa noche, la llave empieza a brillar sola.',
    },
    {
        'num': 2,
        'titulo': 'El Mapa que Respira',
        'resumen': 'Isla le cuenta a Mateo que su abuelo desaparecio buscando los Portales Olvidados, puertas entre dimensiones que el mundo olvido a proposito. En la biblioteca encuentran un libro viejo con un mapa que parece moverse cuando nadie lo mira directamente. El bibliotecario, el senor Voss, los observa desde la sombra con una sonrisa que no llega a sus ojos.',
    },
    {
        'num': 3,
        'titulo': 'La Primera Puerta',
        'resumen': 'Siguiendo el mapa, Mateo e Isla llegan a un callejon sin salida detras de la panaderia del barrio. La llave encaja en una grieta de la pared. El portal se abre y del otro lado ven un cielo con dos lunas y un bosque de arboles de cristal. Antes de decidir si entrar, algo desde adentro los jala.',
    },
    {
        'num': 4,
        'titulo': 'El Lado Espejo',
        'resumen': 'Al otro lado encuentran una version extrana de su barrio donde todo esta al reves y los edificios flotan invertidos. Conocen a Eco, una nina que es la version espejo de Isla pero fria y calculadora. Eco dice saber como encontrar al abuelo de Isla pero pide algo a cambio: la llave.',
    },
    {
        'num': 5,
        'titulo': 'Lo Que Dejaron Atras',
        'resumen': 'Mateo e Isla deben decidir si confiar en Eco. Descubren que el senor Voss tambien esta en esta dimension y parece conocer el lugar perfectamente. El abuelo de Isla aparece por fin, pero algo en el ha cambiado. Logran regresar, pero al llegar notan que la llave ahora tiene grabado un numero: 2. Hay mas portales.',
    },
]

PROMPT_BASE = """Eres un escritor experto en literatura infantil de misterio y fantasia.
Escribes como una mezcla entre Stephen King (suspenso, atmosfera densa, personajes con secretos)
y J.K. Rowling (mundo magico detallado, humor suave, amistad profunda),
adaptado perfectamente para un nino de 8 anos: sin violencia grafica,
sin terror real, con vocabulario claro pero rico.

SERIE: El Portal Olvidado

PERSONAJES:
- Mateo: 9 anos, curioso, solitario, observador. Le cuesta hacer amigos pero es muy inteligente. Le da miedo la oscuridad aunque nunca lo admite.
- Isla: 9 anos, nueva en el colegio, ojos de distinto color (uno verde, uno gris). Guarda secretos sobre su familia. Es valiente pero impulsiva.
- Senor Voss: bibliotecario del colegio. Siempre sonrie pero sus ojos no acompanan la sonrisa. Sabe mas de lo que dice.
- Eco: version espejo de Isla del otro lado del portal. Fria, calculadora, con un dolor profundo que no muestra.
- Abuelo de Isla: desaparecio hace 2 anos buscando los portales. Aparece cambiado en el capitulo 5.

REGLAS:
1. Divide el capitulo en exactamente 5 bloques de texto
2. Cada bloque tiene entre 80 y 120 palabras
3. Termina cada bloque con una frase que genere suspenso o curiosidad
4. El ultimo bloque termina ABIERTO, algo queda sin resolver
5. Incluye al menos una mini historia interna de un personaje secundario
6. Usa descripciones sensoriales: olores, sonidos, texturas
7. Texto limpio en espanol correcto con tildes y caracteres especiales

CAPITULO {num}: {titulo}
Resumen: {resumen}

Devuelve UNICAMENTE JSON valido sin texto adicional ni bloques de codigo markdown:
{{
  "bloque1": "texto bloque 1",
  "bloque2": "texto bloque 2",
  "bloque3": "texto bloque 3",
  "bloque4": "texto bloque 4",
  "bloque5": "texto bloque 5",
  "preguntas": [
    {{
      "pregunta": "pregunta de comprension",
      "opciones": {{"A": "opcion", "B": "opcion", "C": "opcion", "D": "opcion"}},
      "respuesta": "A",
      "explicacion": "explicacion breve y amigable para el nino"
    }}
  ]
}}

Genera exactamente 8 preguntas distribuidas asi:

--- BLOQUE 1: COMPRENSION LECTORA (5 preguntas) ---

2 LITERALES (lo que esta explicito en el texto):
- Identificacion de personajes principales y secundarios
- Lugar, tiempo y secuencia de eventos
- Ejemplo: Que paso primero, que hizo X, donde ocurrio, quien encontro la llave

2 INFERENCIALES (lo que se deduce pero no esta escrito):
- Deducir sentimientos o motivaciones de los personajes
- Predecir resultados: si el personaje hizo esto, que crees que pasara ahora
- Deducir el proposito del texto o la ensenanza
- Ejemplo: Por que crees que Mateo sintio miedo, que crees que hara Isla ahora

1 CRITICA (opinion personal sustentada):
- El nino debe tomar posicion y justificarla con lo que leyo
- Ejemplo: Estas de acuerdo con lo que hizo Eco, que habrias hecho tu en lugar de Mateo

--- BLOQUE 2: GRAMATICA APLICADA AL TEXTO (3 preguntas) ---
Usa oraciones TEXTUALES o muy cercanas al cuento para hacer preguntas de gramatica.
No inventes oraciones nuevas — usa frases que aparecen en el capituloq que escribiste.

1 pregunta de SUSTANTIVOS o ADJETIVOS:
- Identificar el sustantivo propio o comun en una frase del cuento
- Identificar el adjetivo que describe a un personaje u objeto del cuento
- Ejemplo: En la frase "una llave oxidada", el adjetivo que describe la llave es...

1 pregunta de VERBOS Y TIEMPOS VERBALES:
- Identificar el verbo en una frase del cuento
- Identificar en que tiempo esta: pasado, presente o futuro
- Ejemplo: En la frase "Mateo encontro la llave", el verbo esta en tiempo...

1 pregunta de SINONIMOS, ANTONIMOS o CONECTORES:
- Encontrar un sinonimo o antonimo de una palabra usada en el cuento
- Identificar el conector logico usado en una frase del cuento y su funcion
- Ejemplo: En el cuento, la palabra "curioso" significa lo mismo que...

REGLAS para todas las preguntas:
- 4 opciones creibles (A, B, C, D), una sola correcta
- Los distractores deben ser errores tipicos que cometen los ninos de 8 anos
- La explicacion debe ser breve, amigable y usar frases del cuento como evidencia
- Lenguaje simple y claro para nino de 8 anos
"""

def llamar_openai(prompt):
    if not OPENAI_KEY:
        raise Exception('OPENAI_API_KEY no esta definida. Corre primero: $env:OPENAI_API_KEY="sk-..."')
    body = json.dumps({
        'model': 'gpt-4o-mini',
        'max_tokens': 3000,
        'temperature': 0.85,
        'messages': [{'role': 'user', 'content': prompt}]
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://api.openai.com/v1/chat/completions',
        data=body,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {OPENAI_KEY}'
        }
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode('utf-8'))
    return data['choices'][0]['message']['content']

def guardar_en_sheets(cap_num, titulo, bloques, preguntas, sheets_service):
    fila = [
        SERIE,
        str(cap_num),
        titulo,
        COLOR,
        bloques.get('bloque1', ''),
        '',
        bloques.get('bloque2', ''),
        '',
        bloques.get('bloque3', ''),
        '',
        bloques.get('bloque4', ''),
        '',
        bloques.get('bloque5', ''),
        '',
        json.dumps(preguntas, ensure_ascii=False)
    ]
    sheets_service.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range='Cuentos!A:O',
        valueInputOption='RAW',
        body={'values': [fila]}
    ).execute()

def main():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    sheets = build('sheets', 'v4', credentials=creds)

    print('Generando El Portal Olvidado - 5 capitulos\n')

    for cap in CAPITULOS:
        print(f'Capitulo {cap["num"]}: {cap["titulo"]}...')
        prompt = PROMPT_BASE.format(
            num=cap['num'],
            titulo=cap['titulo'],
            resumen=cap['resumen']
        )
        try:
            raw = llamar_openai(prompt)
            clean = raw.replace('```json', '').replace('```', '').strip()
            data = json.loads(clean)
            bloques   = {k: v for k, v in data.items() if k.startswith('bloque')}
            preguntas = data.get('preguntas', [])
            guardar_en_sheets(cap['num'], cap['titulo'], bloques, preguntas, sheets)
            print(f'   OK - {len(preguntas)} preguntas guardadas\n')
        except Exception as e:
            print(f'   ERROR: {e}\n')

    print('Serie completa! Revisa la hoja Cuentos en el Sheet.')
    print('Ahora genera las imagenes en Gemini y pega las URLs en columnas F, H, J, L, N')

if __name__ == '__main__':
    main()
