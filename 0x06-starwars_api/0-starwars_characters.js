#!/usr/bin/node

const request = require("request");

function getCharacters(movieId) {
  const swapiUrl = "https://swapi.dev/api";

  request(`${swapiUrl}/films/${movieId}/`, (error, response, body) => {
    if (error) {
      console.error("Error fetching data:", error);
      return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error("Error fetching character data:", charError);
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  });
}

const movieId = process.argv[2];
getCharacters(movieId);
