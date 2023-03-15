from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle

# Load the saved XGBoost classifier using pickle
with open('xgb_classifier.pkl', 'rb') as f:
    xgb = pickle.load(f)

# Initialize Flask application
app = Flask(__name__)

# Define endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from HTTP request
    data = request.json
    
    # Convert input data to a single-row DataFrame
    input_data = pd.DataFrame([data])
    
    # Make prediction using XGBoost classifier
    prediction = xgb.predict(data)
    
    # Return prediction as JSON
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5004, debug=True)