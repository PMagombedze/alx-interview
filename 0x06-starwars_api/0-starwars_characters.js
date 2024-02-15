#!/usr/bin/node

const request = require('request'); // Use request for HTTP requests

function fetchCharacterNames(filmId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

  request(url, async (err, res, body) => {
    if (err) {
      console.error('Error fetching data:', err);
      return;
    }

    const characters = JSON.parse(body).characters;

    const characterNames = await Promise.all(
      characters.map((characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (err, res, charBody) => {
            if (err) {
              console.error('Error fetching character data:', err);
              reject(err);
            } else {
              resolve(JSON.parse(charBody).name);
            }
          });
        });
      })
    );

    characterNames.forEach((name) => console.log(name));
  });
}

const filmId = process.argv[2];
fetchCharacterNames(filmId);
