'use strict'

const mysql = require('mysql');
const express = require('express');
const app = express();

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'imanoodle',
    database: 'fox_player'
  });
  
  connection.connect(function(err) {
    if(err){
      console.log('Error connecting to database oooh');
      return;
    }
    console.log('Connection established woooo');
  });


app.use(express.json())
app.use('/', express.static('./assets'))

app.get('/playlists', function(req, res) {
    connection.query('SELECT * FROM playlists;', function(err, result) {
        if(err) {
            console.log(err.toString());
          }
          res.json(result);
    })
})


app.post('/playlists', function(req, res) {
    connection.query('INSERT INTO playlists (playlist) VALUES("' + req.body.playlist + '");', function(err, result) {
        if(err) {
            console.log(err.toString());
        }
          res.json({"Result":"okay"});
    })
})

app.delete('/playlists', function(req, res) {
    connection.query('DELETE FROM playlists WHERE id=' + req.body.id + ';', function(err, result) {
        if(err) {
            console.log(err.toString());
        }
        res.json({"Result":"okay"});
    })
})

app.get('/tracks', function(req, res) {
    connection.query('SELECT * FROM tracks;', function(err, result) {
        if(err) {
            console.log(err.toString());
          }
          res.json(result);
    })
})


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/fox_index.html');    
});

app.listen(8080, function() {
    console.log('server is up on port 8080, good to go!')
})

