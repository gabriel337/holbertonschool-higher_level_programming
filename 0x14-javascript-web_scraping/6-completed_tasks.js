#!/usr/bin/node
// script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dic[tasks[i].userId] === undefined) {
          dic[tasks[i].usedId] = 1;
        } else {
          dic[tasks[i].userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error Code: ' + response.statusCode);
  }
});
