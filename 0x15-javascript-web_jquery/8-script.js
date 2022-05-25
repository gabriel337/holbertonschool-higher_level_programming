$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const films = data.results;
    for (const idx in films) {
      $('#list_movies').append('<li>' + films[idx].title + '</li>');
    }
  });
});
