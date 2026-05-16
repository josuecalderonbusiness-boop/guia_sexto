const { google } = require('googleapis');

async function getSheets() {
  const creds = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  const auth = new google.auth.GoogleAuth({
    credentials: creds,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
  return google.sheets({ version: 'v4', auth: await auth.getClient() });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method !== 'GET') return res.status(405).json({ ok: false });

  const SHEET_ID = process.env.SHEET_ID;
  const { nombre, todos, listaUsuarios } = req.query;

  try {
    const sheets = await getSheets();

    // ── ADMIN: lista de usuarios ─────────────────────────────────
    if (listaUsuarios === '1') {
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: 'Usuarios!A:B',
      });
      const rows = (r.data.values || []).slice(1); // saltar encabezado si hay
      const usuarios = rows
        .filter(row => row[0])
        .map(row => ({ codigo: row[0], nombre: row[1] || row[0] }));
      return res.json({ ok: true, usuarios });
    }

    // ── Leer hoja Resultados ─────────────────────────────────────
    const r = await sheets.spreadsheets.values.get({
      spreadsheetId: SHEET_ID,
      range: 'Resultados!A:H',
    });
    const rows = r.data.values || [];
    if (rows.length <= 1) return res.json({ ok: true, resultados: [] });

    const data = rows.slice(1).map(row => ({
      fecha:      row[0] || '',
      nombre:     row[1] || '',
      dia:        row[2] || '',
      materia:    row[3] || '',
      puntaje:    row[4] || '0',
      total:      row[5] || '0',
      porcentaje: row[6] || '0',
      respuestas: row[7] || '[]',
    }));

    // ── ADMIN: todos los resultados ──────────────────────────────
    if (todos === '1') {
      return res.json({ ok: true, resultados: data });
    }

    // ── ALUMNO: solo sus resultados ──────────────────────────────
    if (!nombre) return res.json({ ok: false, error: 'Falta nombre' });
    const filtrados = data.filter(r =>
      r.nombre.trim().toLowerCase() === nombre.trim().toLowerCase()
    );
    return res.json({ ok: true, resultados: filtrados });

  } catch (e) {
    return res.status(500).json({ ok: false, error: e.message });
  }
};