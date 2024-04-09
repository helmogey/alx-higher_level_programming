#!/usr/bin/node
const Squareold = require('./5-square');
class Square extends Squareold {
  charPrint (c = 'X') {
    let output = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        output += c;
      }
      output += '\n';
    }
    process.stdout.write(output);
  }
}
module.exports = Square;
