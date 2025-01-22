# House-price-prediction-aiml
This project is an end-to-end machine learning solution to predict real estate prices based on various features. The solution includes a Flask-based REST API that uses a trained machine learning model to provide predictions. The API accepts property details in JSON format and returns the predicted price.
Features

Machine Learning Model: Predicts real estate prices using a regression model.

REST API: Built with Flask, enabling easy integration with other applications.

Customizable Input: Accepts detailed property features for flexible predictions.

Scalable Architecture: Can be deployed locally or on cloud platforms.

Prerequisites

Python 3.7 or above

Required Python Libraries:

Flask

joblib

scikit-learn

pandas (for data manipulation)

Install the required libraries using:

pip install -r requirements.txt

File Structure

app.py: Contains the Flask API implementation.

best_model.pkl: Pre-trained machine learning model.

requirements.txt: Lists the required Python packages.

README.md: Project documentation.

test_request.py: Example Python script for testing the API.

Usage

1. Start the Flask API

Run the following command in your terminal:

python app.py

The API will start running locally at http://127.0.0.1:5000/.

2. Test the API

Send a POST request to the /predict endpoint with property details in JSON format. Example:

{
    "Date": "2025-01-22",
    "bedrooms": 3,
    "bathrooms": 2,
    "living_area": 1500,
    "lot_area": 5000,
    "floors": 2,
    "waterfront_present": 1,
    "number_of_views": 3,
    "condition_of_house": 4,
    "built_year": 2005,
    "renovation_year": 2015,
    "postal_code": 98052,
    "latitude": 47.642,
    "longitude": -122.131,
    "living_area_renov": 1200,
    "lot_area_renov": 4500,
    "number_of_schools_nearby": 3,
    "distance_from_airport": 15
}

Example Request Using requests Library

import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Date": "2025-01-22",
    "bedrooms": 3,
    "bathrooms": 2,
    "living_area": 1500,
    "lot_area": 5000,
    "floors": 2,
    "waterfront_present": 1,
    "number_of_views": 3,
    "condition_of_house": 4,
    "built_year": 2005,
    "renovation_year": 2015,
    "postal_code": 98052,
    "latitude": 47.642,
    "longitude": -122.131,
    "living_area_renov": 1200,
    "lot_area_renov": 4500,
    "number_of_schools_nearby": 3,
    "distance_from_airport": 15
}
response = requests.post(url, json=data)
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)

3. Response

The API will return a JSON response with the predicted price:

{
    "prediction": 450000.0
}

How It Works

Input Parsing: The API accepts JSON input containing property details.

Feature Engineering:

The Date field is converted into numeric days since 2000-01-01.

Missing or invalid fields are replaced with default values (e.g., 0).

Prediction: The model generates a price prediction based on the input features.

Why regression model ?
For the above project, regression models were chosen because the primary goal was to predict a continuous variable: the price of houses. After evaluating several potential models, the following reasons justify the final model choice:

Challenges faced -One of the main challenges I faced was developing an API, as I wasn't very familiar with that aspect of development. Learning how to design and structure the API, handle requests, and manage responses was new to me. Understanding concepts like routing, authentication, and ensuring proper data formatting took time and required a lot of experimentation. Additionally, integrating the API with the machine learning model added complexity, as I needed to ensure that the API could handle the model’s input requirements and deliver accurate predictions in a timely manner.
