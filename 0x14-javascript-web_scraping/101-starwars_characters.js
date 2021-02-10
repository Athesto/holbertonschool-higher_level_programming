#!/usr/bin/node
const request = require('request');
const apiUrlFilm = 'https://swapi-api.hbtn.io/api/films/';
const film = process.argv[2];

const ans = {};
request
  .get(apiUrlFilm + film + '/', function (err, response, body) {
    if (err) return console.error(err);
    const info = JSON.parse(body).characters;
    for (const index in info) {
      request
        .get(info[index], function (err, resp, body) {
          if (err) return console.error(err);
          ans[index] = JSON.parse(body).name;
        });
    }
  });
setTimeout(() => print(ans), 2000);

function print (dict) {
  for (const idx in dict) {
    console.log(dict[idx]);
  }
}
