'use strict';

const getVersionRoutes = (app, config) => {
  app.get('/api/version', (req, res) => {
    res.send(config.version);
  });
};

module.exports = getVersionRoutes;
