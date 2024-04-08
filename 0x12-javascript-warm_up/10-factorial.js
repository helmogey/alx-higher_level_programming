#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (num) {
  const number = parseInt(num);
  if (isNaN(number)) {
    return 1;
  } else if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const result = factorial(args[0]);
console.log(result);
