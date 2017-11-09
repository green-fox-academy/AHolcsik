'use strict'

const mysql = require('mysql');
const express = require('express');
const app = express();

app.use(express.json())

var conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'imanoodle',
  database: 'bookstore'
});

conn.connect(function(err) {
  if(err){
    console.log('Error connecting to database oooh');
    return;
  }
  console.log('Connection established woooo');
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/bookstore', function(req, res) {
    conn.query('SELECT book_name FROM book_mast;', function(err, result) {
        if(err) {
            console.log(err.toString());
          }
          res.json(result);
    })
})



app.listen(8080, function() {
    console.log('server is up on port 8080, good to go!')
})

