var express = require('express');
var app = express();
app.use(express.static('public'));
var routes = require('./routes')(app);
app.listen(3000);
