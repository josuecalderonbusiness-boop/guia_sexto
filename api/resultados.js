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
  if (req.method === 'OPTIONS') return res.status(200).end();

  const { nombre } = req.query;

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    const response = await sheets.spreadsheets.values.get({
      spreadsheetId: SHEET_ID,
      range: 'Resultados!A2:G500',
    });

    const rows = response.data.values || [];
    const resultados = rows
      .filter(row => row[0] && (!nombre || row[1]?.toLowerCase() === nombre?.toLowerCase()))
      .map(row => ({
        fecha:      row[0] || '',
        nombre:     row[1] || '',
        dia:        row[2] || '',
        materia:    row[3] || '',
        puntaje:    row[4] || '0',
        total:      row[5] || '0',
        porcentaje: (row[6] || '0%').replace('%', ''),
      }));

    res.status(200).json({ ok: true, resultados });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
};
