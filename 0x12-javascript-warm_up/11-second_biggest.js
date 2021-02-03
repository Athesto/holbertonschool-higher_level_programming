#!/usr/bin/node
const input = process.argv.slice(2).sort((a, b) => b - a);
const answer = (input[1] == null) ? 0 : parseInt(input[1]);
console.log(answer);
