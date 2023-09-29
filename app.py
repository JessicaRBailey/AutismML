# Import the dependencies.
import os
import numpy as np

import sqlite3
from keras.models import load_model
import joblib
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

@app.route("/survey")
def survey():
    return "Survey Page"

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

        # Check the prediction value and decide the message
        prediction_value = predictions[0][0]
        message = "Your child may be at risk for autism." if prediction_value >= 0.75 else "It does not appear that your child is showing signs of autism at this time."

        # Render an HTML template with the predicted results
        return render_template("results.html", message=message)

    except Exception as e:
        # Handle exceptions, e.g., file not found or database query issues
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
