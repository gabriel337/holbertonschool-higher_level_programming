#!/usr/bin/node
// Script that reads and prints the content of a file

const filename = process.argv[2];
const fs = require('fs');
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
