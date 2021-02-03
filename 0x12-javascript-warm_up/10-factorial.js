#!/usr/bin/node
function factor (num) {
  if (Number.isNaN(num) || num <= 1) { return (1); }
  return (num * (factor(num - 1)));
}

const num = factor(parseInt(process.argv[2]));
console.log(num);
