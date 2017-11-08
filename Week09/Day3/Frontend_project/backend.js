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

app.get('/greeter', function(req,res){
    if (req.query.name && req.query.title){
        res.json (
            {
                "welcome_message": "Oh, hi there " + req.query.name + ", my dear " + req.query.title + "!"
              }
        )
    }
    else if (!req.query.name) {
        res.json (
            {
                "error": "Please provide a name!"
            }
        )
    }
    else if (!req.query.title) {
        res.json (
            {
                "error": "Please provide a title!"
            }
        )
    }
})

app.get('/appenda/:whatever', function(req,res){
    if (req.params.whatever){
        res.json (
            {
                "appended": req.params.whatever + "a"
              }
        )
    }
})

express.json.type = "application/json"
app.use('/assets', express.static('assets'))

app.listen(8080);