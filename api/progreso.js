const { google } = require('googleapis');

const SHEET_ID = process.env.SHEET_ID;

function getAuth() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  return new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
}

async function findRow(sheets, codigo) {
  const response = await sheets.spreadsheets.values.get({
    spreadsheetId: SHEET_ID,
    range: 'Progreso!A2:G200',
  });
  const rows = response.data.values || [];
  const idx = rows.findIndex(r => r[0]?.trim().toUpperCase() === codigo.trim().toUpperCase());
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

    // GET — obtener progreso del usuario
    if (req.method === 'GET') {
      const { codigo } = req.query;
      if (!codigo) return res.status(400).json({ ok: false, error: 'Falta codigo' });

      const { rows, idx } = await findRow(sheets, codigo);
      if (idx < 0) return res.status(200).json({ ok: true, progreso: null });

      const row = rows[idx];
      return res.status(200).json({
        ok: true,
        progreso: {
          codigo:    row[0],
          dia:       row[1],
          materia:   row[2],
          idx:       parseInt(row[3] || '0'),
          puntaje:   parseInt(row[4] || '0'),
          total:     parseInt(row[5] || '0'),
          respuestas: JSON.parse(row[6] || '[]'),
        }
      });
    }

    // POST — guardar progreso
    if (req.method === 'POST') {
      const { codigo, dia, materia, idx, puntaje, total, respuestas } = req.body;
      if (!codigo) return res.status(400).json({ ok: false, error: 'Falta codigo' });

      const { rowNum } = await findRow(sheets, codigo);
      const values = [[codigo, dia, materia, idx, puntaje, total, JSON.stringify(respuestas || [])]];

      if (rowNum) {
        // Actualizar fila existente
        await sheets.spreadsheets.values.update({
          spreadsheetId: SHEET_ID,
          range: `Progreso!A${rowNum}:G${rowNum}`,
          valueInputOption: 'USER_ENTERED',
          requestBody: { values },
        });
      } else {
        // Agregar nueva fila
        await sheets.spreadsheets.values.append({
          spreadsheetId: SHEET_ID,
          range: 'Progreso!A:G',
          valueInputOption: 'USER_ENTERED',
          requestBody: { values },
        });
      }

      return res.status(200).json({ ok: true });
    }

    // DELETE — borrar progreso al terminar examen
    if (req.method === 'DELETE') {
      const { codigo } = req.query;
      if (!codigo) return res.status(400).json({ ok: false });

      const { rowNum } = await findRow(sheets, codigo);
      if (rowNum) {
        await sheets.spreadsheets.values.clear({
          spreadsheetId: SHEET_ID,
          range: `Progreso!A${rowNum}:G${rowNum}`,
        });
      }
      return res.status(200).json({ ok: true });
    }

    res.status(405).json({ error: 'Method not allowed' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ ok: false, error: err.message });
  }
};
