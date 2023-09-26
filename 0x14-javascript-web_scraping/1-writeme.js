#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const strContent = process.argv[3];

fs.writeFile(filePath, strContent, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
