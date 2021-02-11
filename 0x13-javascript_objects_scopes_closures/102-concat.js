#!/usr/bin/node
const fs = require('fs');

const files = process.argv.slice(2, process.argv.length);

let out = '';

out += fs.readFileSync(files[0]);
out += fs.readFileSync(files[1]);
fs.writeFileSync(files[2], out);
