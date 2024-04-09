#!/usr/bin/node
const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];

let combinedContent = '';

fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  combinedContent += data1;

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    combinedContent += data2;
    console.log(combinedContent);
  });
});
