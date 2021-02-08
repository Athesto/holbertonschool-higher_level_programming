#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) { console.log('X'.repeat(this.width)); }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temporal = this.width;
    this.width = this.height;
    this.height = temporal;
  }
}
module.exports = Rectangle;
