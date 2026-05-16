export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'Método no permitido' });
  }

  const { pregunta, opciones, elegida, correcta } = req.body;

  const prompt = `Eres un profesor amable que explica a un niño de 11-12 años (grado 6) por qué se equivocó en una pregunta de examen.

Pregunta: "${pregunta}"
El niño respondió: Opción ${elegida} — "${opciones[elegida]}"
La respuesta correcta era: Opción ${correcta} — "${opciones[correcta]}"

Explícale en máximo 3 oraciones cortas y simples:
1. Por qué su respuesta estaba mal
2. Por qué la respuesta correcta es la correcta
3. Un tip fácil para recordarlo

Usa lenguaje sencillo, amigable, sin tecnicismos. Empieza directo, sin saludos.`;

  try {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        max_tokens: 300,
        messages: [{ role: 'user', content: prompt }]
      })
    });

    const data = await response.json();
    const texto = data.choices?.[0]?.message?.content;

    if (!texto) {
      return res.status(500).json({ ok: false, error: 'Sin respuesta' });
    }

    return res.status(200).json({ ok: true, explicacion: texto });

  } catch (error) {
    return res.status(500).json({ ok: false, error: error.message });
  }
}