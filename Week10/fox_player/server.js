'use strict'

const express = require('express');
const app = express();

app.use(express.json())
app.use('/', express.static('./assets'))


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/fox_index.html');    
});

app.listen(8080, function() {
    console.log('server is up on port 8080, good to go!')
})

