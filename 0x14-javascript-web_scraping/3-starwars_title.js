#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
request
  .get('https://swapi-api.hbtn.io/api/films/' + movieId, function (error, response, body) {
    if (error) console.error('error:', error);
    console.log(JSON.parse(body).title);
  });
