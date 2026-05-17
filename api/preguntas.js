const { google } = require('googleapis');

const SHEET_ID = process.env.SHEET_ID;

function getAuth() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  return new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
res.setHeader('Cache-Control', 'no-store');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  if (req.method === 'OPTIONS') return res.status(200).end();

  const { dia, materia, grado, leccion } = req.query;

  // Modo Jero (grado 2): G2_MAT_L01
  // Modo Tomas (grado 6): Dia1_MAT
  let sheetName;
  if (grado && leccion) {
    const lNum = String(leccion).padStart(2, '0');
    sheetName = `G${grado}_${(materia||'').toUpperCase()}_L${lNum}`;
  } else {
    if (!dia || !materia) {
      return res.status(400).json({ error: 'Faltan parámetros dia y materia' });
    }
    sheetName = `Dia${dia}_${materia.toUpperCase()}`;
  }

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    const response = await sheets.spreadsheets.values.get({
      spreadsheetId: SHEET_ID,
      range: `${sheetName}!A2:I35`,
valueRenderOption: 'UNFORMATTED_VALUE',
    });

    const rows = response.data.values || [];
    const preguntas = rows
      .filter(row => row[0])
      .map((row, i) => ({
        id: i + 1,
        pregunta: row[0] || '',
        opciones: {
          A: row[1] || '',
          B: row[2] || '',
          C: row[3] || '',
          D: row[4] || '',
        },
        respuesta: (row[5] || 'A').toUpperCase(),
        imagen: row[6] || '',
        video: row[7] && row[7].startsWith('http') ? row[7] : '',
        explicacion: row[8] || '',
      }));

    res.status(200).json({ ok: true, preguntas, sheetName });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
};
