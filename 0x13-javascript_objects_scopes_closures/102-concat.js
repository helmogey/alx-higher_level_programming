#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

let data1 = fs.readFileSync(sourceFile1.toString());
let data2 = fs.readFileSync(sourceFile2.toString());
let combinedContent = data1 + data2;
fs.writeFileSync(destinationFile, combinedContent);
