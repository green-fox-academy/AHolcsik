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

let playlist = [
    { "id": 6, "title": "All tracks", "system": 1},    
    { "id": 1, "title": "Favorites", "system": 1},
    { "id": 2, "title": "Music for programming", "system": 0},
    { "id": 4, "title": "Fox house", "system": 0},
    { "id": 5, "title": "Worst of the 90s", "system": 0},
    { "id": 3, "title": "Driving", "system": 0}
]

let tracklist = [
    {
        "author": "MSI",
        "track_name": "Bitches",
        "length": "3:00"
    },
    
    {
        "author": "Turmion Katilot",
        "track_name": "Pyrun nyrkki",
        "length": "3:00"
    },
    
    {
        "author": "Bloodhound Gang",
        "track_name": "Um Tiss Um Tiss Um Tiss",
        "length": "3:00"
    },
    
    {
        "author": "Britney Spears",
        "track_name": "Oops I did it again",
        "length": "3:00"
    }
    ]

app.use(express.json())
app.use('/', express.static('./assets'))

// app.get('/bookstore', function(req, res) {
//     conn.query('SELECT book_name FROM book_mast;', function(err, result) {
//         if(err) {
//             console.log(err.toString());
//           }
//           res.json(result);
//     })
// })


app.get('/playlists', function(req,res){
    res.json(playlist)
})

app.get('/tracks', function(req,res){
    res.json(tracklist)
})

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/fox_index.html');    
});

app.listen(8080, function() {
    console.log('server is up on port 8080, good to go!')
})

