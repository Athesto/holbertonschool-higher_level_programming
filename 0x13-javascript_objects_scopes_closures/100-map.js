#!/usr/bin/node
const array = require('./100-data.js').list;
const out = array.map(x => x * array.indexOf(x));
console.log(array);
console.log(out);
