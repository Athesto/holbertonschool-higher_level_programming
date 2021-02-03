#!/usr/bin/node

const input = process.argv;
let msg;
if (input.length < 3) { msg = 'No argument'; } else { msg = 'Argument found'; }
console.log(msg);
