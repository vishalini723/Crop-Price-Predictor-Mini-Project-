from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    temperature = float(request.form['temperature'])
    rainfall = float(request.form['rainfall'])
    commodity = request.form['commodity']

    # Prepare input for model
    commodity_potato = 1 if commodity == 'Potato' else 0
    commodity_pulses = 1 if commodity == 'Pulses' else 0

    # Make prediction
    features = np.array([[temperature, rainfall, commodity_potato, commodity_pulses]])
    predicted_price = model.predict(features)[0]

    return render_template('index.html', 
                           price=round(predicted_price, 2),
                           temperature=temperature,
                           rainfall=rainfall,
                           commodity=commodity)

if __name__ == '__main__':
    app.run(debug=True)
