var express = require('express');

var app = express();

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
})

app.get('/doubling', function(req,res){
    var toDouble = req.query.input
    var parsedToDouble = parseInt(toDouble)
    if (!parsedToDouble){
        res.send (
            {
                "error": "Please provide an input!"
              }
    )}
    else {
        res.send (
            {
                "received": parsedToDouble,
                "result": parsedToDouble * 2
              }
        )
    }
})

express.json.type = "application/json"
app.use('/assets', express.static('assets'))

app.listen(8080);