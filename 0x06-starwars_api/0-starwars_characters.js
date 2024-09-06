#!/usr/bin/node

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
const request = require('request');


request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    // Use Promise.all to ensure the order of the character responses
    const characterPromises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, resp, body) => {
          if (!err && resp.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(err);
          }
        });
      });
    });


Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((err) => console.error('Error fetching character:', err));
  } else {
    console.error('Error:', error);
  }
});
