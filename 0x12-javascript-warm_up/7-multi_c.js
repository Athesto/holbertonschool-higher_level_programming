#!/usr/bin/node
const times = process.argv[2];
const msg = 'C is fun\n'.repeat(times).slice(0, -1);
console.log(msg);
