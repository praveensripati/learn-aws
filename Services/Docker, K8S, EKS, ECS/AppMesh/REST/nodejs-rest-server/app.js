'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const config = require('./config/config');
const app = new express();

// register JSON parser middlewear
app.use(bodyParser.json());

require('./config/cors')(app);
require('./routes/personRoutes')(app);
require('./routes/versionRoutes')(app, config);

app.listen(80, () => {
  /* eslint-disable */
  console.log('Server is up!');
});
