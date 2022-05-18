#!/usr/bin/node
// script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const tasks = JSON.parse(body);
  const dic = {};

  for (const task of tasks) {
    if (task.completed) {
      const userID = task.userId;
      dic[userID] = (dic[userID] + 1 || 1);
    }
  }
  console.log(dic);
});
