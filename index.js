const client = require('./connection.js');
const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.listen(port, () => {
    console.log('Server started at http://localhost:' + port)
});

client.connect();

app.get("/", async (req, res) => {
    let results = {}
    results.rows = []
    try {
        const keterangan_tipekegiatans = req.query.tipekegiatan;
        const keterangan_kegiatans = req.query.kegiatan;
        const keterangan_subzonas = req.query.subzona;

        results = await client.query("SELECT izin.keterangan_izin FROM peraturan INNER JOIN tipe_kegiatan on peraturan.kode_tipekegiatan = tipe_kegiatan.kode_tipekegiatan INNER JOIN kegiatan on peraturan.kode_tipekegiatan = kegiatan.kode_tipekegiatan and peraturan.id_kegiatan = kegiatan.id_kegiatan INNER JOIN sub_zona on peraturan.kode_subzona = sub_zona.kode_subzona INNER JOIN zona on sub_zona.kode_zona = zona.kode_zona INNER JOIN izin on peraturan.kode_izin = izin.kode_izin WHERE tipe_kegiatan.keterangan_tipekegiatan = $1 AND kegiatan.keterangan_kegiatan = $2 AND sub_zona.keterangan_subzona = $3",[keterangan_tipekegiatans,keterangan_kegiatans,keterangan_subzonas])
    }
    catch (e) {
        console.log("error")
    }
    finally {
        res.setHeader("content-type", "application/json")
        res.send(JSON.stringify(results.rows))
    }
})
