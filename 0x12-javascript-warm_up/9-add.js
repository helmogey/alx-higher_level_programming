#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  if (isNaN(num1) || isNaN(num2)) {
    return 'Not a number';
  } else {
    return num1 + num2;
  }
}

const result = add(args[0], args[1]);
console.log(result);

