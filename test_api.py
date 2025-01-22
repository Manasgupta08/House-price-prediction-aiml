# This Python code is a sample script to send a request to a RESTful API for predicting house prices.
import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"  # Replace with your API URL if deployed

# Sample input data with all required features (replace with your own values)
data = {
    "Date": "2025-01-22",  # Date in YYYY-MM-DD format (example date)
    "bedrooms": 3,
    "bathrooms": 2,
    "living_area": 1500,  # Living area in square feet
    "lot_area": 5000,     # Lot area in square feet
    "floors": 2,
    "waterfront_present": 1,  # 1 = yes, 0 = no
    "number_of_views": 3,
    "condition_of_house": 4,  # Assuming condition scale is 1-5 (1 = poor, 5 = excellent)
    "built_year": 2005,
    "renovation_year": 2015,
    "postal_code": 98052,     # Example postal code
    "latitude": 47.642,       # Example latitude
    "longitude": -122.131,    # Example longitude
    "living_area_renov": 1200,  # Renovated living area
    "lot_area_renov": 4500,     # Renovated lot area
    "number_of_schools_nearby": 3,
    "distance_from_airport": 15  # Example distance in miles
}

# Send a POST request with JSON data
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)


