#!/usr/bin/node
const args = process.argv.slice(2); // Get arguments excluding script name and path

if (args.length >= 2) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log('Not enough arguments! Please provide two arguments.');
}
