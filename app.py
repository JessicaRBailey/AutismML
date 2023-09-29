# Import the dependencies.
import os
import numpy as np
import sqlite3
from keras.models import load_model
import joblib
import json
import datetime
from flask import Flask, jsonify, request, g, render_template


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Load the saved neural network model and StandardScaler during application startup
model = load_model('Resources/QChatNN_for_new_survey.h5')
scaler = joblib.load('Resources/scaler.joblib')


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return render_template("index.html")


#################################################
# Survey Page
#################################################
@app.route("/survey", methods=['GET', 'POST'])
    
def survey():
    surveyQuestions = [
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
        'How old is your child (in months)']
    
    if request.method == 'POST':
        # Create a dictionary to store survey responses
        survey_responses = {}
        
        # Loop through the form data to collect responses
        for i in range(1, 12):
            response_key = str(i)
            response_value = request.form.get("option_" + response_key)
            
            # For questions 1 to 10, calculate the value based on "Always," "Usually," "Sometimes," "Rarely," and "Never"
            if i != 11:
                if response_value in ("1", "2", "3"):
                    survey_responses[response_key] = 1
                elif response_value in ("4", "5"):
                    survey_responses[response_key] = 0
                else:
                    # Handle unexpected values or errors here
                    pass
            else:
                # For question 11, store the exact age value as a string
                survey_responses[response_key] = response_value
        
        # Add a timestamp to the survey_responses dictionary
        survey_responses["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"
        
        # Check if the JSON file already exists
        json_filename = 'Resources/survey_responses.json'
        if os.path.exists(json_filename):
            # Load existing data from the JSON file
            with open(json_filename, 'r') as json_file:
                existing_responses = json.load(json_file)
        else:
            existing_responses = []
        
        # Append the new survey responses to the existing data
        existing_responses.append(survey_responses)
        
        # Save the updated JSON data to the file
        with open(json_filename, 'w') as json_file:
            json.dump(existing_responses, json_file, indent=4)
    
    conn = sqlite3.connect('Resources/survey_options.db')
    cursor = conn.cursor()

    optionList = cursor.execute("SELECT option_id, option_name FROM survey_options ORDER BY option_id").fetchall()

    # Close the database connection
    conn.close()
    
    return render_template("survey.html", surveyQuestions=surveyQuestions, optionList=optionList)



#################################################
# Results Page
#################################################

@app.route("/results")
def results():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Resources/survey_responses.db')
        cursor = conn.cursor()

        # Query to retrieve the last entry based on the 'Timestamp' column
        cursor.execute('SELECT A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, Age_Mons FROM survey_responses ORDER BY Timestamp DESC LIMIT 1')

        # Fetch the result (should be one row, the last entry)
        last_entry = cursor.fetchone()

        # Close the database connection
        conn.close()

        input_data = last_entry
        # QChat_df['A10'] = 1 - QChat_df['A10']

        # Convert the input data to a NumPy array
        input_data = np.array(input_data)
        
        # Reshape the input data to be 2D (1 row and n_features columns)
        input_data = input_data.reshape(1, -1)  # -1 automatically computes the number of columns

        # Use the loaded StandardScaler to scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make predictions using the model
        predictions = model.predict(input_data_scaled)

        # Render an HTML template with the predicted results
        return render_template("results.html", predictions=predictions)

    except Exception as e:
        # Handle exceptions, e.g., file not found or database query issues
        return f"An error occurred: {str(e)}"




if __name__ == '__main__':
    app.run(debug=True)
