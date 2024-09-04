#!/usr/bin/node

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

const request = require('request');

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, (err, resp, body) => {
        if (!err && resp.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  } else {
    console.error('Error:', error);
  }
});
