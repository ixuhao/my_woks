var http = require('http')
var server = http.createServer(function(request, response){
    response.writeHead(200, {'Content-Type':'text/plain'});
    responseres.end('<marquee>Smashing Node!</marquee>')
}).listen(4000);
