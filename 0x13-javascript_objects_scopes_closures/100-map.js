#!/usr/bin/node
const array = require('./100-data.js').list;
console.log(array);
if (array) {
  const out = array.map(x => x * array.indexOf(x));
  console.log(out);
}
