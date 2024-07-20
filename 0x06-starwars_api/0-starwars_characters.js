#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${baseUrl}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const chURL = JSON.parse(body).characters;
    const chName = chURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (perr, __, chBody) => {
          if (perr) {
            reject(perr);
          }
          resolve(JSON.parse(chBody).name);
        });
      }));

    Promise.all(chName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
