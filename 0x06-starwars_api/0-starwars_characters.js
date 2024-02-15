#!/usr/bin/node

const request = require("request");

request(
  "https://swapi-api.alx-tools.com/api/films" + process.argv[2],
  function (err, res, body) {
    if (err) throw err;
    const actors = JSON.parse(body).characters;
    Order(actors, 0);
  }
);

const Order = (actors, n) => {
  if (n === actors.length) return;
  request(actors[n], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    Order(actors, n + 1);
  });
};
