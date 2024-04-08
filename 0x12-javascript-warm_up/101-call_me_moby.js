#!/usr/bin/node
exports.repeat = function repeat (x, theFunction) {

  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
