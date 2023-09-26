#!/usr/bin/node
const req = require('request');

const url = process.argv[2];

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
