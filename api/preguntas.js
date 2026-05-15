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
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  if (req.method === 'OPTIONS') return res.status(200).end();

  const { dia, materia } = req.query;
  if (!dia || !materia) {
    return res.status(400).json({ error: 'Faltan parámetros dia y materia' });
  }

  const sheetName = `Dia${dia}_${materia.toUpperCase()}`;

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    const response = await sheets.spreadsheets.values.get({
      spreadsheetId: SHEET_ID,
      range: `${sheetName}!A2:H35`,
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
        video: row[7] || '',
      }));

    res.status(200).json({ ok: true, preguntas, sheetName });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
};
