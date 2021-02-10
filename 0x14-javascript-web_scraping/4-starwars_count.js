#!/usr/bin/node
const request = require('request');
const characterId = 18;
request.get('https://swapi-api.hbtn.io/api/films/', function (err, resp, body) {
  if (err) console.error(err);
  const info = JSON.parse(body);
  const movies = info.results;
  let characterCounter = 0;
  movies.forEach(function (movie) {
    movie.characters.forEach(function (character) {
      if (character.search('people/' + characterId) > 0) characterCounter++;
    });
  });
  console.log(characterCounter);
});
