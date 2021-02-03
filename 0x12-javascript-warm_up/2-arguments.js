#!/usr/bin/node

const input = process.argv;
let msg;
if (input.length < 3) {
  msg = 'No argument';
} else {
  msg = (input.length === 3) ? 'Argument found' : 'Arguments found';
}
console.log(msg);
