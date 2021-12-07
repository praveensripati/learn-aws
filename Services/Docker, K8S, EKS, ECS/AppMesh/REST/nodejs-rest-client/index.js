const express = require('express');
const request = require('request');

const app = express();
const port = 80;

app.get('/', (req, res) => {

    const requestOptions = {
        url: 'http://nodejs-rest-server-service.person.com/person/all',
        method: 'GET'
    };
    request(requestOptions, (err, response, body) => {
        if (err) {
            console.log(err);
        } else if (response.statusCode === 200) {
            res.send(body)
        } else {
            console.log(response.statusCode);
        }
    });

});

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`))
