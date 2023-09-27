#!/usr/bin/node
const req = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
req(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const results = JSON.parse(body).characters;

  for (let i = 0; i < results.length; i++) {
    req(results[i], (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const character = JSON.parse(body).name;
      console.log(character);
    });
  }
});
