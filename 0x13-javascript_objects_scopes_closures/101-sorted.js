#!/usr/bin/node
const data = require('./101-data.js').dict;
const out = {};
for (const key in data) {
  if (!out[data[key]]) {
    out[data[key]] = [];
  }
  out[data[key]].push(key);
}
console.log(out);
