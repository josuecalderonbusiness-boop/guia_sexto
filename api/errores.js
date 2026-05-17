const { google } = require('googleapis');

const SHEET_ID = process.env.SHEET_ID;

function getAuth() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  return new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
}

async function findRow(sheets, codigo, dia, materia) {
  const response = await sheets.spreadsheets.values.get({
    spreadsheetId: SHEET_ID,
    range: 'Errores!A2:D500',
  });
  const rows = response.data.values || [];
  const idx = rows.findIndex(r =>
    r[0]?.trim().toUpperCase() === codigo.trim().toUpperCase() &&
    String(r[1]) === String(dia) &&
    r[2]?.trim().toUpperCase() === materia.trim().toUpperCase()
  );
  return { rows, idx, rowNum: idx >= 0 ? idx + 2 : null };
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Cache-Control', 'no-store');
  if (req.method === 'OPTIONS') return res.status(200).end();

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    // GET — leer errores
    if (req.method === 'GET') {
      const { codigo, dia, materia, todos } = req.query;
      if (!codigo) return res.status(400).json({ ok: false, error: 'Falta codigo' });

      // ?todos=1 — devolver todas las entradas del alumno (para sincronizacion)
      if (todos === '1') {
        const response = await sheets.spreadsheets.values.get({
          spreadsheetId: SHEET_ID,
          range: 'Errores!A2:D500',
        });
        const rows = response.data.values || [];
        const entradas = rows
          .filter(r => r[0]?.trim().toUpperCase() === codigo.trim().toUpperCase())
          .map(r => {
            let errores = [];
            try { errores = JSON.parse(r[3] || '[]'); } catch(e) {}
            return { dia: r[1], materia: r[2], errores };
          })
          .filter(e => e.errores.length > 0);
        return res.json({ ok: true, entradas });
      }

      // Lectura individual
      if (!dia || !materia)
        return res.status(400).json({ ok: false, error: 'Faltan parametros dia/materia' });

      const { rows, idx } = await findRow(sheets, codigo, dia, materia);
      if (idx < 0) return res.json({ ok: true, errores: [] });

      const row = rows[idx];
      let errores = [];
      try { errores = JSON.parse(row[3] || '[]'); } catch(e) {}
      return res.json({ ok: true, errores });
    }

    // POST — guardar errores
    if (req.method === 'POST') {
      const { codigo, dia, materia, errores } = req.body;
      if (!codigo || !dia || !materia)
        return res.status(400).json({ ok: false, error: 'Faltan parametros' });

      const values = [[codigo, String(dia), materia, JSON.stringify(errores || [])]];
      const { rowNum } = await findRow(sheets, codigo, dia, materia);

      if (rowNum) {
        await sheets.spreadsheets.values.update({
          spreadsheetId: SHEET_ID,
          range: `Errores!A${rowNum}:D${rowNum}`,
          valueInputOption: 'RAW',
          requestBody: { values },
        });
      } else {
        await sheets.spreadsheets.values.append({
          spreadsheetId: SHEET_ID,
          range: 'Errores!A:D',
          valueInputOption: 'RAW',
          requestBody: { values },
        });
      }
      return res.json({ ok: true });
    }

    // DELETE — borrar errores cuando refuerzo completado al 100%
    if (req.method === 'DELETE') {
      const { codigo, dia, materia } = req.query;
      if (!codigo || !dia || !materia)
        return res.status(400).json({ ok: false });

      const { rowNum } = await findRow(sheets, codigo, dia, materia);
      if (rowNum) {
        await sheets.spreadsheets.values.clear({
          spreadsheetId: SHEET_ID,
          range: `Errores!A${rowNum}:D${rowNum}`,
        });
      }
      return res.json({ ok: true });
    }

    res.status(405).json({ error: 'Method not allowed' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ ok: false, error: err.message });
  }
};
