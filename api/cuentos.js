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
  res.setHeader('Cache-Control', 'no-store');
  if (req.method === 'OPTIONS') return res.status(200).end();

  const { serie, capitulo } = req.query;

  try {
    const auth = getAuth();
    const sheets = google.sheets({ version: 'v4', auth });

    const response = await sheets.spreadsheets.values.get({
      spreadsheetId: SHEET_ID,
      range: 'Cuentos!A2:O100',
      valueRenderOption: 'UNFORMATTED_VALUE',
    });

    const rows = response.data.values || [];

    // Si piden una serie y capítulo específico
    if (serie && capitulo) {
      const row = rows.find(r =>
        r[0]?.toString().trim() === serie.trim() &&
        r[1]?.toString().trim() === capitulo.toString().trim()
      );
      if (!row) return res.json({ ok: false, error: 'Capítulo no encontrado' });

      let preguntas = [];
      try { preguntas = JSON.parse(row[14] || '[]'); } catch(e) {}

      return res.json({
        ok: true,
        capitulo: {
          serie:    row[0] || '',
          numero:   row[1] || '',
          titulo:   row[2] || '',
          color:    row[3] || '#0F0F2E',
          bloques: [
            { texto: row[4]  || '', imagen: row[5]  || '' },
            { texto: row[6]  || '', imagen: row[7]  || '' },
            { texto: row[8]  || '', imagen: row[9]  || '' },
            { texto: row[10] || '', imagen: row[11] || '' },
            { texto: row[12] || '', imagen: row[13] || '' },
          ].filter(b => b.texto),
          preguntas,
        }
      });
    }

    // Si no piden capítulo específico → devolver lista de series con sus capítulos
    const series = {};
    rows.forEach(row => {
      if (!row[0]) return;
      const nombreSerie = row[0].toString().trim();
      if (!series[nombreSerie]) {
        series[nombreSerie] = {
          nombre: nombreSerie,
          color:  row[3] || '#0F0F2E',
          capitulos: []
        };
      }
      series[nombreSerie].capitulos.push({
        numero: row[1] || '',
        titulo: row[2] || '',
        imagen: row[5] || '', // imagen del bloque 1 como portada
      });
    });

    return res.json({
      ok: true,
      series: Object.values(series)
    });

  } catch (err) {
    console.error('cuentos.js error:', err.message);
    res.status(500).json({ ok: false, error: err.message });
  }
};
