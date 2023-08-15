#!/usr/bin/node
const dict = require('./101-data').dict;

const newD = {};
for (const key in dict) {
  const occurrences = dict[key];
  if (newD[occurrences]) {
    newD[occurrences].push(key);
  } else {
    newD[occurrences] = [key];
  }
}
console.log(newD);
