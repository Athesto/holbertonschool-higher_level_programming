#!/usr/bin/node
const num = process.argv[2];
const answer = (parseInt(num)) ? `My number: ${num}` : 'Not a number';
console.log(answer);
