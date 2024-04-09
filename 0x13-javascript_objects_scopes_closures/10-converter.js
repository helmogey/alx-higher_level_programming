#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    const digits = '0123456789ABCDEF';
    let convertedString = '';

    function convert (n) {
      if (n === 0) return;

      const remainder = n % base;
      convertedString = digits[remainder] + convertedString;
      convert(Math.floor(n / base));
    }

    convert(num);
    return convertedString;
  };
};
