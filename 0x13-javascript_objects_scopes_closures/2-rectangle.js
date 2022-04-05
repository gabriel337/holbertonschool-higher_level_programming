#!/usr/bin/node
// class with attributes width & height if 0 or not positive,
// create empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
