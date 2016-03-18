var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
fs = require('fs')

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

var lineReader = require('readline').createInterface({
      input: require('fs').createReadStream('motion.txt')
});

app.get('/current.jpg', function(req, res){
  res.sendFile(__dirname + '/current.jpg');
});


io.on('connection', function(socket){
    console.log('a connection is established!')
    var lineReader = require('readline').createInterface({
          input: require('fs').createReadStream('motion.txt')
    });

    lineReader.on('line', function (line) {
        io.emit('chat message', line);
    });


});

http.listen(80, function(){
  console.log('listening on *:80');
});
