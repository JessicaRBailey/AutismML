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
  'Does your child stare at nothing with no apparent purpose?',
];

// Parse the data
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('survey', { surveyQuestions });
});

app.post('/submit', (req, res) => {
  const surveyData = {};

  surveyQuestions.forEach((question, index) => {
    const selectedOption = req.body[`selectedOption_${question}`];
    
    // Adjust the mapping only for the question "Does your child stare at nothing with no apparent purpose"
    let mappedValue = selectedOption === 'Never' || selectedOption === 'Rarely' ? 0 : 1;
    if (question === 'Does your child stare at nothing with no apparent purpose') {
      mappedValue = 1 - mappedValue; 
    }
    
    // Store the mapped response as an integer in the JSON object
    surveyData[index + 1] = mappedValue;
  });

  // Store the response for "How many months old is your child?" in the JSON object
  const childAgeMonths = req.body.childAgeMonths;
  surveyData['11'] = childAgeMonths;

  // Store surveyData in a JSON file
  const filePath = 'resources/survey_responses.json';
  fs.readFile(filePath, (err, data) => {
    let responsesArray = [];
    if (!err) {
      responsesArray = JSON.parse(data);
    }
    surveyData['timestamp'] = new Date(); 
    responsesArray.push(surveyData);

    // Write the data back to the file
    fs.writeFile(filePath, JSON.stringify(responsesArray), (err) => {
      if (err) throw err;
    });

    // Thank you page
    res.send('Thank you for completing the survey!');
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

