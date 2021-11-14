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
        const id_kegiatan = req.query.kegiatan;

        results = await client.query('select kode_izin from peraturan where id_kegiatan = $1', [id_kegiatan])
    }
    catch (e) {
        console.log("error")
    }
    finally {
        res.setHeader("content-type", "application/json")
        res.send(JSON.stringify(results.rows))
    }
})