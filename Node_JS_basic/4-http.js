const http = require('http');

const app = http.createServer((req, res) => {
  res.setHeader('content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

app.listen(1245);
module.exports = app;
