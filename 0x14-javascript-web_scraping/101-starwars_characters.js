#!/usr/bin/node
const request = require('request');
const apiUrlFilm = 'https://swapi-api.hbtn.io/api/films/';
const film = process.argv[2];
request
  .get(apiUrlFilm + film + '/', function (err, response, body) {
    if (err) return console.error(err);
    const info = JSON.parse(body).characters;
    for (const index in info) {
      request
        .get(info[index], function (err, resp, body) {
          if (err) return console.error(err);
          console.log(JSON.parse(body).name);
        });
    }
  });
