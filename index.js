const client = require('./module/connection.js')
const express = require('express');
const app = express();
const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log(`app started on port ${PORT}`)
});

var sql = "SELECT fnget_itbx('PENGHIJAUAN', 'Taman Lingkungan', 'Cagar Budaya Bersejarah & Pengetahuan')";

client.connect();

app.get('/itbx', (req, res)=>{
    client.query(sql, function(err, result) {if(!err){
            res.send(result.rows);
        }
    });
    client.end;
  })