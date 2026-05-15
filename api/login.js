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
  res.setHeader('Cache-Control', 'no-store');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { codigo } = req.body;
  if (!codigo) return res.status(400).json({ ok: false, error: 'Falta el código' });

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    const response = await sheets.spreadsheets.values.get({
      spreadsheetId: SHEET_ID,
      range: 'Usuarios!A2:B100',
    });

    const rows = response.data.values || [];
    const usuario = rows.find(row => 
      row[0]?.trim().toUpperCase() === codigo.trim().toUpperCase()
    );

    if (!usuario) {
      return res.status(200).json({ ok: false, error: 'Código incorrecto. Verifica con tu profe.' });
    }

    res.status(200).json({ ok: true, nombre: usuario[1] || usuario[0], codigo: usuario[0] });
  } catch (err) {
    console.error(err);
    res.status(500).json({ ok: false, error: 'Error del servidor' });
  }
};
