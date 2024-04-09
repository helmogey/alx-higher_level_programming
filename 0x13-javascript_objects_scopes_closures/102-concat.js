#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

let combinedContent = '';

fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  combinedContent += data1;

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    combinedContent += data2;

    fs.writeFile(destinationFile, combinedContent, 'utf8', (err3) => {
    });
  });
});
