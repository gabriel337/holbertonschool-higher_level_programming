#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const num = process.argv;
num[2] = parseInt(num[2]);
num[3] = parseInt(num[3]);
console.log(add(num[2], num[3]));
