const express = require('express');
const app = express();
const port = 3000;
const bodyParser = require('body-parser');
const fs = require('fs');

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Define the survey questions
const surveyQuestions = [
  'What is your name?',
  'How old are you?',
  'What is your favorite color?'
];

// Define the survey options
const options = ['Always', 'Usually', 'Sometimes', 'Rarely', 'Never'];

// Use body-parser middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('survey', { surveyQuestions, options });
});

app.post('/submit', (req, res) => {
  const responses = surveyQuestions.map((question) => req.body[question]);
  const selectedOption = req.body.selectedOption;

  // Store responses and selected option in a JSON file
  const surveyData = {
    responses,
    selectedOption
  };

  fs.readFile('survey_responses.json', (err, data) => {
    let responsesArray = [];
    if (!err) {
      responsesArray = JSON.parse(data);
    }
    responsesArray.push(surveyData);
    fs.writeFile('survey_responses.json', JSON.stringify(responsesArray), (err) => {
      if (err) throw err;
    });
  });

  res.send('Thank you for completing the survey!');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});