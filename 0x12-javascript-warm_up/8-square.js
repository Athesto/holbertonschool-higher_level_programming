#!/usr/bin/node
const times = process.argv[2];
let answer = '';
if (!parseInt(times)) {
  answer = 'Missing size';
} else {
  for (let i = 0; i < times; i++) {
    answer += 'X'.repeat(times);
    answer += '\n';
  }
  answer = answer.slice(0, -1);
}
console.log(answer);
