#!/usr/bin/node
//  script that prints the title of a Star Wars movie
//  where the episode number matches a given integer

const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error Code:' + response.statusCode);
  }
});
