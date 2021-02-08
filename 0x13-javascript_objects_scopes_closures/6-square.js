#!/usr/bin/node
const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c = 'X') {
    for (let row = 0; row < this.height; row++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
