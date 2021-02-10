#!/usr/bin/node
const request = require('request');
const apiUrlFilm = 'https://swapi-api.hbtn.io/api/films/';
const apiUrlPeople = 'https://swapi-api.hbtn.io/api/people/';
const film = process.argv[2];
request
  .get(apiUrlPeople, function (err, response, body) {
    if (err) return console.error(err);
    const info = JSON.parse(body).results;
    for (const index in info) {
      if (info[index].films.includes(apiUrlFilm + film + '/')) {
        console.log(info[index].name);
      }
    }
  });
