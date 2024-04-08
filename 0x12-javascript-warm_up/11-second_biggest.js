#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(num => parseInt(num));

  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (const num of numbers) {
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num !== firstMax) {
      secondMax = num;
    }
  }

  console.log(secondMax === -Infinity ? 0 : secondMax);
}
