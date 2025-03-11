from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load your model
model = pickle.load(open('your_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return "Waiter Tips Prediction Model is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Process input and predict
    prediction = model.predict([[data['total_bill'], data['size']]])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
