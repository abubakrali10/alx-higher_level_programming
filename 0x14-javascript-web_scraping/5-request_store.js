#!/usr/bin/node
const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
req(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(filePath, body, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
});
