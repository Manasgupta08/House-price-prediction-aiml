# This code implements a Flask-based API that uses a pre-trained machine learning model (saved as best_model.pkl) to predict an output based on input features provided in a JSON format. 
from flask import Flask, request, jsonify
import joblib
from datetime import datetime

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('best_model.pkl')  # Ensure 'best_model.pkl' is in the same directory
except FileNotFoundError:
    raise Exception("Model file 'best_model.pkl' not found. Ensure the file is in the correct location.")

# Root route for testing
@app.route('/')
def home():
    return "API is working. Use the /predict endpoint to get predictions."

# Prediction route
@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Define all the expected features
        expected_features = [
            'Date', 'bedrooms', 'bathrooms', 'living_area', 'lot_area', 'floors', 
            'waterfront_present', 'number_of_views', 'condition_of_house', 
            'built_year', 'renovation_year', 'postal_code', 'latitude', 'longitude',
            'living_area_renov', 'lot_area_renov', 'number_of_schools_nearby', 'distance_from_airport'
        ]

        # Extract features from the request data
        data = request.get_json()

        # Initialize a list to hold the features
        features = []

        # Convert Date to numeric (e.g., days since 2000-01-01)
        date_str = data['Date']
        date_format = "%Y-%m-%d"
        try:
            date_obj = datetime.strptime(date_str, date_format)
            date_numeric = (date_obj - datetime(2000, 1, 1)).days  # Days since 2000-01-01
            features.append(date_numeric)
        except ValueError:
            features.append(0)  # If the date format is incorrect, append 0

        # Loop through the other features and ensure they are numeric
        for feature in expected_features[1:]:  # Skip 'Date' since it's already handled
            value = data.get(feature, 0)  # Default to 0 if the feature is missing
            
            # Convert the value to numeric, if possible
            try:
                value = float(value)  # Try to convert to float
            except ValueError:
                value = 0  # If conversion fails, set the feature to 0

            features.append(value)

        # Make the prediction using the model
        prediction = model.predict([features])

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})



if __name__ == '__main__':
    app.run(debug=True)




