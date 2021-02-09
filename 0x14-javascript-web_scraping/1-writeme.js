#!/usr/bin/node
const fs = require('fs');
const [path, msg] = process.argv.slice(2, process.argv.length);
fs.writeFile(path, msg, 'utf-8', function (err) {
  if (err) { return console.log(err); }
});
