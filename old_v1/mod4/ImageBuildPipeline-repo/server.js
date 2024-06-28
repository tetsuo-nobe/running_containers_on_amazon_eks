'use strict';

const express = require('express');
require('date-utils');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  var dt = new Date();
  var formatted = dt.toFormat("YYYY/MM/DD HH24:MI:SS");
  res.send('Hello World 現在日時： ' + formatted);
  console.log('---- Accessed:--' + formatted)
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);