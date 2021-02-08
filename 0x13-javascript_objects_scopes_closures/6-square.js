#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let row = 0; row < this.height; row++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
