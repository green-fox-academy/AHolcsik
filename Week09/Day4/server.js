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

conn.connect(function(err){
  if(err){
    console.log('Error connecting to database oooh');
    return;
  }
  console.log('Connection established woooo');
});

app.listen(8080, function() {
    console.log('server is up on port 3000, good to go!')
})

