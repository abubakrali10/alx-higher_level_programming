#!/usr/bin/node
const req = require('request');

const url = process.argv[2];
req(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasks = JSON.parse(body);
  const dict = {};

  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      const uID = tasks[i].userId;
      if (uID in dict) {
        dict[uID]++;
      } else {
        dict[uID] = 1;
      }
    }
  }
  console.log(dict);
});
