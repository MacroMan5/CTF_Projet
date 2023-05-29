const express = require('express');
const challengesRouter = require('./routes/challenges');
const app = express();
const port = 3000;

app.use('/challenges', challengesRouter); // Tout ce qui commence par /challenges est redirigé vers le routeur challengesRouter

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});