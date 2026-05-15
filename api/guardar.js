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
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { nombre, dia, materia, puntaje, total, respuestas, fecha } = req.body;

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    // Ensure Resultados sheet exists by trying to read it first
    try {
      await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: 'Resultados!A1',
      });
    } catch {
      // Sheet might be empty but exists, that's ok
    }

    const fechaStr = fecha || new Date().toISOString().slice(0, 19).replace('T', ' ');
    const porcentaje = Math.round((puntaje / total) * 100) + '%';

    await sheets.spreadsheets.values.append({
      spreadsheetId: SHEET_ID,
      range: 'Resultados!A:H',
      valueInputOption: 'USER_ENTERED',
      requestBody: {
        values: [[
          fechaStr,
          nombre || 'Estudiante',
          `Día ${dia}`,
          materia,
          puntaje,
          total,
          porcentaje,
          JSON.stringify(respuestas || {}),
        ]],
      },
    });

    res.status(200).json({ ok: true });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
};
