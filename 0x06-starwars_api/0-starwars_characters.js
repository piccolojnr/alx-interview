#!/usr/bin/node
const request = require("request");
const API = "https://swapi-api.hbtn.io/api";

if (process.argv.length > 2) {
  request(`${API}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const chUrl = JSON.parse(body).characters;
    const chName = chUrl.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (pErr, __, chReqB) => {
            if (pErr) {
              reject(pErr);
            }
            resolve(JSON.parse(chReqB).name);
          });
        })
    );

    Promise.all(chName)
      .then((names) => console.log(names.join("\n")))
      .catch((allErr) => console.log(allErr));
  });
}
