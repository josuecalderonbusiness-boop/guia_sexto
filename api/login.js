const { google } = require('googleapis');

const ADMIN_CODES = ['ADMIN2026']; // ← agrega aquí más códigos admin si quieres

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
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'Método no permitido' });

  const body = req.body;
  const SHEET_ID = process.env.SHEET_ID;

  // ── LOGIN NORMAL ─────────────────────────────────────────────────
  if (body.codigo && !body.adminAgregar && !body.adminEliminar) {
    const codigo = body.codigo.trim().toUpperCase();

    // ¿Es admin?
    if (ADMIN_CODES.includes(codigo)) {
      return res.json({ ok: true, nombre: 'Administrador', codigo, esAdmin: true });
    }

    // Buscar en hoja Usuarios
    try {
      const sheets = await getSheets();
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: 'Usuarios!A:C',
      });
      const rows = r.data.values || [];
      const encontrado = rows.find(row => row[0] && row[0].trim().toUpperCase() === codigo);
      if (!encontrado) {
        return res.json({ ok: false, error: 'Código no encontrado. Pídele el código a tu profe.' });
      }
      const grado = encontrado[2] ? parseInt(encontrado[2]) || encontrado[2] : null;
      return res.json({ ok: true, nombre: encontrado[1] || codigo, codigo, esAdmin: false, grado });
    } catch (e) {
      return res.status(500).json({ ok: false, error: 'Error al verificar código: ' + e.message });
    }
  }

  // ── ADMIN: AGREGAR USUARIO ───────────────────────────────────────
  if (body.adminAgregar) {
    const { codigo, nombre } = body.adminAgregar;
    if (!codigo || !nombre) return res.json({ ok: false, error: 'Faltan datos' });
    try {
      const sheets = await getSheets();
      // Verificar que no existe
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID, range: 'Usuarios!A:B',
      });
      const rows = r.data.values || [];
      const existe = rows.find(row => row[0] && row[0].trim().toUpperCase() === codigo.toUpperCase());
      if (existe) return res.json({ ok: false, error: 'Ese código ya existe' });

      const gradoNuevo = body.adminAgregar.grado || '';
      await sheets.spreadsheets.values.append({
        spreadsheetId: SHEET_ID,
        range: 'Usuarios!A:C',
        valueInputOption: 'RAW',
        requestBody: { values: [[codigo.toUpperCase(), nombre, String(gradoNuevo)]] },
      });
      return res.json({ ok: true });
    } catch (e) {
      return res.status(500).json({ ok: false, error: e.message });
    }
  }

  // ── ADMIN: ELIMINAR USUARIO ──────────────────────────────────────
  if (body.adminEliminar) {
    const { codigo } = body.adminEliminar;
    try {
      const sheets = await getSheets();
      const r = await sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID, range: 'Usuarios!A:B',
      });
      const rows = r.data.values || [];
      const idx = rows.findIndex(row => row[0] && row[0].trim().toUpperCase() === codigo.toUpperCase());
      if (idx === -1) return res.json({ ok: false, error: 'Usuario no encontrado' });

      // Obtener sheetId de la hoja Usuarios
      const meta = await sheets.spreadsheets.get({ spreadsheetId: SHEET_ID });
      const hoja = meta.data.sheets.find(s => s.properties.title === 'Usuarios');
      if (!hoja) return res.json({ ok: false, error: 'Hoja Usuarios no encontrada' });

      await sheets.spreadsheets.batchUpdate({
        spreadsheetId: SHEET_ID,
        requestBody: {
          requests: [{
            deleteDimension: {
              range: {
                sheetId: hoja.properties.sheetId,
                dimension: 'ROWS',
                startIndex: idx,
                endIndex: idx + 1,
              }
            }
          }]
        }
      });
      return res.json({ ok: true });
    } catch (e) {
      return res.status(500).json({ ok: false, error: e.message });
    }
  }

  return res.json({ ok: false, error: 'Solicitud no reconocida' });
};