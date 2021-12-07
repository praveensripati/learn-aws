'use strict';

const Router = require('express');
const personRepo = require('../repo/personRepository');

const getPersonRoutes = app => {
  const router = new Router();

  router
    .get('/get/:id', (req, res) => {
      const id = parseInt(req.params.id);
      const result = personRepo.getById(id);
      res.send(result);
    })
    .get('/all', (req, res) => {
      const result = personRepo.getAll();
      res.send(result);
    })
    .get('/remove', (req, res) => {
      personRepo.remove();
      const result = 'Last person remove. Total count: ' + personRepo.persons.size;
      res.send(result);
    })
    .post('/save', (req, res) => {
      const person = req.body;
      const result = personRepo.save(person);
      res.send(result);
    });

  app.use('/person', router);
};

module.exports = getPersonRoutes;
