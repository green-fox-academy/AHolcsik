'use strict'

const express = require('express');
const app = express();

app.use(express.json())
app.use('/assets', express.static('./assets'));


app.get('/', function(req, res) {
    console.log('something')
    res.sendFile(__dirname + '/giphy.html');    
});

// app.get('/', function(req, res) {
//     conn.query('SELECT book_name FROM book_mast;', function(err, result) {
//         if(err) {
//             console.log(err.toString());
//           }
//           res.json(result);
//     })
// })



app.listen(8080, function() {
    console.log('server is up on port 8080, good to go!')
})

