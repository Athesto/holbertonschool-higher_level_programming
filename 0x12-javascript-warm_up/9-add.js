#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const input = process.argv;
add(parseInt(input[2]), parseInt(input[3]));
