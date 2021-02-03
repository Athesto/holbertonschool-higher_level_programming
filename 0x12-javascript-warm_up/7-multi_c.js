#!/usr/bin/node
const times = process.argv[2];
let msg;
if (parseInt(times)) { msg = 'C is fun\n'.repeat(times).slice(0, -1); } else { msg = 'Missing number of occurrences'; }
console.log(msg);
