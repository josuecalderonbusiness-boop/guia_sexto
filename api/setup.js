const { google } = require('googleapis');

const SHEET_ID = process.env.SHEET_ID;
const MATERIAS = ['MAT', 'BIO', 'QUI', 'SOC', 'LEN'];
const DIAS = [1, 2, 3, 4, 5, 6];

function getAuth() {
  const credentials = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);
  return new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method === 'OPTIONS') return res.status(200).end();

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    // Get existing sheets
    const meta = await sheets.spreadsheets.get({ spreadsheetId: SHEET_ID });
    const existing = meta.data.sheets.map(s => s.properties.title);

    const toCreate = [];
    for (const dia of DIAS) {
      for (const mat of MATERIAS) {
        const name = `Dia${dia}_${mat}`;
        if (!existing.includes(name)) toCreate.push(name);
      }
    }
    if (!existing.includes('Resultados')) toCreate.push('Resultados');

    if (toCreate.length > 0) {
      await sheets.spreadsheets.batchUpdate({
        spreadsheetId: SHEET_ID,
        requestBody: {
          requests: toCreate.map(title => ({
            addSheet: { properties: { title } }
          }))
        }
      });
    }

    // Add headers to each Dia_Materia sheet
    const headerRequests = [];
    for (const dia of DIAS) {
      for (const mat of MATERIAS) {
        const name = `Dia${dia}_${mat}`;
        headerRequests.push({
          range: `${name}!A1:F1`,
          values: [['Pregunta', 'Opción A', 'Opción B', 'Opción C', 'Opción D', 'Respuesta Correcta']]
        });
      }
    }
    headerRequests.push({
      range: 'Resultados!A1:H1',
      values: [['Fecha', 'Nombre', 'Día', 'Materia', 'Puntaje', 'Total', 'Porcentaje', 'Respuestas']]
    });

    await sheets.spreadsheets.values.batchUpdate({
      spreadsheetId: SHEET_ID,
      requestBody: {
        valueInputOption: 'USER_ENTERED',
        data: headerRequests
      }
    });

    res.status(200).json({ ok: true, created: toCreate });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
};
