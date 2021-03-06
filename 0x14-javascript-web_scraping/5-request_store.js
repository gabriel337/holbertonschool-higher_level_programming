#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filename, body, 'utf-8', (err) => {
    if (err) {
      console.error('error:', err);
    }
  });
});
