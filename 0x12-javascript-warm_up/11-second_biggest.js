#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
let Bsec = 0;
if (args.length > 1) {
  Bsec = args.sort((a, b) => (b - a))[1];
}
console.log(Bsec);
