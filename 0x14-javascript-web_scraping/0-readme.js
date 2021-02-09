#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2, process.argv.length);
const print = (error, msg) => { if (!error) console.log(msg); };
fs.readFile(file[0], 'utf-8', (error, data) => print(error, data.toString()));
