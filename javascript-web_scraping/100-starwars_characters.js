#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Fetch and print each character name
  characters.forEach((url) => {
    request(url, (err, res, characterBody) => {
      if (!err) {
        const character = JSON.parse(characterBody);
        console.log(character.name);
      }
    });
  });
});
