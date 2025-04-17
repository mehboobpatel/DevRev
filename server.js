const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

const port = process.env.PORT || 3000;
const APP_ID = process.env.DEVREV_APP_ID || 'APP_ID_NOT_FOUND';
console.log(`Using APP_ID: ${APP_ID}`);

// Serve static files like CSS, JS
app.use(express.static(__dirname));

app.get('/', (req, res) => {
  // Read the demo.html file
  fs.readFile(path.join(__dirname, 'demo.html'), 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('Error loading demo.html');
      return;
    }
    // Replace placeholder with actual app_id
    const result = data.replace('{{APP_ID}}', APP_ID);
    res.send(result);
  });
});

app.listen(port, () => {
  console.log(`✅ Server running at http://localhost:${port}`);
});
