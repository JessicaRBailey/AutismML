const express = require('express');
const app = express();
const port = 3000;
const bodyParser = require('body-parser');
const fs = require('fs');

// Use EJS as the view engine
app.set('view engine', 'ejs');

// Define the survey questions
const surveyQuestions = [
  'Does your child look at you when you call his/her name?',
  'How easy is it for you to get eye contact with your child?',
  'Does your child point to indicate that s/he wants something?',
  'Does your child point to share interest with you? (e.g. a toy that is out of reach)',
  'Does your child pretend? (e.g. care for dolls, talk on a toy phone)',
  'Does your child follow where you are looking?',
  'If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them?',
  'Would you describe your child\'s first words as:',
  'Does your child use simple gestures? (e.g. wave goodbye)',
  'Does your child stare at nothing with no apparent purpose?'
];

// Define the survey options
const options = ['Always', 'Usually', 'Sometimes', 'Rarely', 'Never'];

// Use body-parser middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('survey', { surveyQuestions, options });
});

app.post('/submit', (req, res) => {
  const surveyData = {};

  surveyQuestions.forEach((question) => {
    const selectedOption = req.body[`selectedOption_${question}`];
    surveyData[question] = { selectedOption };
  });

  // Store surveyData in a JSON file
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



