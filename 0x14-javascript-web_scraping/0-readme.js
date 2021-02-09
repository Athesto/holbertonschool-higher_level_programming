#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2, process.argv.length);
fs.readFile(file[0], 'utf-8', function (err, data) {
  if (err) { return console.log(err); }
  console.log(data);
});
