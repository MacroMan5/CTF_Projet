const express = require('express');
const challengesRouter = require('./routes/challenges');
const path = require('path');
const app = express();
const port = 3000;

// Static files middleware
app.use(express.static(path.join(__dirname, 'public'))); // Assuming your index.html is in a directory named 'public' 

app.use('/challenges', challengesRouter); // All requests starting with /challenges are redirected to the challengesRouter

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
}); 
