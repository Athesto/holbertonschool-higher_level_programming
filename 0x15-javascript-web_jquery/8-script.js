const urlApi = 'https://swapi-api.hbtn.io/api/films/?format=json';

function listMovies (data) {
  console.log(data.results);
  for (const index in data.results) {
    const title = data.results[index].title;
    const htmlTitle = `<li>${title}</li>`;
    $('ul#list_movies').append(htmlTitle);
    console.log(title);
  }
}

$.get(urlApi, listMovies);
