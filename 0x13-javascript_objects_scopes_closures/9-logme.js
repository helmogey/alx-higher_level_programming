#!/usr/bin/node
exports.logMe = (function () {
  let count = 0;

  return function (item) {
    count++;
    console.log(`${count}: ${item}`);
  };
})();
