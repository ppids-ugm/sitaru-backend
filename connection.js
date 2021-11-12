const {Pool, Client} = require('pg')

const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'sitaru',
    password: 'postgres',
    port: "5432",
  })

const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'sitaru',
    password: 'postgres',
    port: "5432",
  })  

module.exports = client