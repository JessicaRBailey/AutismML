# Autistic Spectrum Disorder Screening Predictor Model
![Project Logo](Images/Walk23-hero-web.png)

## Introduction


Our project is an analysis of toddler autism spectrum disorder (ASD) screening data. In this project, we dive deeper into the dataset to uncover valuable insights, trends, and key observations regarding the early detection of autism in young children. Our primary goal is to gain a deeper understanding of the various factors linked with autism's early identification and understand more potential questions that could contribute to developing an early detection system.

We employ a combination of supervised learning techniques and neural network models to achieve these objectives. Additionally, we have designed and deployed a user-friendly survey on our website, seamlessly integrated with a database system, to efficiently collect and manage the essential data for this analysis. In this README, we will provide essential information, instructions, and insights regarding our project, helping you navigate through our findings and methodologies.

Purpose: The main goal behind the project is to create a website with our findings surrounding ASD data to inform parents with children who are curious about their children’s characteristics and behavior and if they could be remotely linked to autism. The primary audience of this website includes any parent inquiring about their child’s behavior and trends. The survey will allow individuals to see based on their results if their child has characteristics or behaviors that have been linked with autism. 

*Disclaimer* It cannot tell if your toddler has or does not have Autism Spectrum Disorder. In addition, the result shown in the survey is predicted using a machine learning algorithm that was created by students for a class project, not trained medical professionals. If you are concerned with your child’s development, we encourage you to discuss your observations with your child's doctor. 


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [CSV to SQLite Database Converter](#csv-to-sqlite-database-converter)
- [Data](#data)
- [Machine Learning](#machine-learning)
- [Data Visualization](#data-visualization)
- [Website](#website)
- [Conclusion](#conclusion)


## Project Overview

Our project utilizes a dataset which can be found online (https://www.kaggle.com/datasets/fabdelja/autism-screening-for-toddlers) and contains the results of 1054 QChat10 survey submissions.  The QChat10 is an early screening tool that helps parents and healthcare professionals decide whether a referral for an autism evaluation would be prudent.  This dataset not only contains their responses, but also whether their child actually had ASD traits, making it an ideal dataset for machine learning.  We trained two machine learning models, one supervised and one neural network, selected the one that performed most accurately, and then built a website that would allow future visitors to submit new survey responses that were fed into the model.  The model predicts the outcome and shares it with the user.  A disclaimer on the website reminds the user that this is not a diagnosis and does not mean that their child does or does not have autism.  The user is encouraged to discuss results with their pediatrician and is pointed to other sources on the internet for more information. 


## Features

    - **Database**

    - **Machine Learning**

    - **Data Visualization**

    - **Website**

## Technologies Used

- Python 3.x
    - Required Python packages (install using pip install package_name):
        - sqlite3: To work with SQLite databases.
        - pandas: For data manipulation and retrieval.
        - NumPy: For handling arrays
        - SciPi: For running correlation tests
        - Flask: For running the website
        - SciKitLearn: For preparing the machine learning models
        - Joblib: For saving scaler to use on new submissions
        - json: For storing submitted data as a json file (though our code still does this, we ultimately stored it directly into the sql database)
        - datetime: For capturing and comparing timestamps, which are currently used as our unique identifier.
        - TensorFlow: For training machine learning algorithms
        - Seaborn: For creating a correlation heatmap

- Tableau
- Html/Css/Bootstrap
- SQLite


## Databases

This project contains 3 databases.

Original Dataset:  SQLITE.db was created using the code in SQLITE.py.  This database contains one table, the original csv file from Kaggle that was used for machine learning. 

Survey Responses:  Resources/survey_responses.db was created using the code in json_to_sql.ipynb.  This database has one table that stores the survey responses from users of the website.  Flask collects those responses, runs them through the neural network model, then also stores the prediction in the same record of the table.  

Survey Options:  Resources/survey_responses.db was created using the code in survey_options_table_creation.ipynb.  This database contains 4 simple tables with 5 records each.  They house the different text options that are displayed as options for questions in the survey.  The id for each option is used to convert the response into a 0 or a 1.  This conversion is done in the flask code.  


## Data

Data for this project came from Kaggle and can be found here:  https://www.kaggle.com/datasets/fabdelja/autism-screening-for-toddlers


## Machine Learning

Two machine learning models were compared.

Supervised Learning:

Neural Network:  We used tensorflow and keras to train a logistic regression model.  Our model used an input layer with 8 nodes and a ReLU activation function, one hidden layer also with 8 nodes and the ReLu activation function, and an output layer with 1 node and a sigmoid activation function.  We trained with all 10 survey questions and the age question.  This removed features that were not correlated with ASD traits and it allowed the use of this model to predict submissions from our website, which only asks for these 11 inputs.  Because all of these were integers, we did not need to use get_dummies or one_hot_encoding, however, we did scale our data so that the age question was not weighted too heavily.  We split our data set into training and testing data, used a binary_crossentropy loss function, and the adam optimizer.  We ran 50 epochs and evaluated both the training and testing data to ensure our model was not overfitting to the data set.  


## Data Visualization

Prior to creating machine learning models, we created visual analyses of the dataset using Tableau Public.  These visualizations show relationships between ethnicities, age, and sex.  Along with the results of correlation tests such as independent t-tests and Chi-squared, we recognized that these were not predictive and we therefore removed them from our final neural network model.  


## Website 
[Project_website_Hp](Images/HomePage.png)

Our wesbite landpage is structured as a the following: Landing Page, Supervised Learning Model, Neural Network Model, Austism Screening Questions. 
[Project_website_Survey](Images/image_survey.png)
[Project_website_SurveyR](Images/image_survey_results.png)
Here is a sample of the survey with and then the result page you might get once you complete it. 



## Conclusion

We are students of UC Berkeley Extension Data Analytics Bootcamp.  As our final project, we have created a machine learning algorithm to predict whether a toddler may have characteristics of ASD.  Future improvements to the project would include creating an actual webpage (project currently runs on a local machine via app.py), testing additional machine learning algorithms to find the best one, and visualization of the new submissions, eventually leading to more refinement of the model.  

A professional and scientific version of this project has been completed and published in a peer reviewed journal.  It can be found here: https://link.springer.com/article/10.1007/s42979-021-00776-5. 

