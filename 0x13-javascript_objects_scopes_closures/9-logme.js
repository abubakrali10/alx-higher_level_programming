#!/usr/bin/node
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
let count = 0;
