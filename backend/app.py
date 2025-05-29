# app.py
# Flask backend for NeuroLens
from flask import Flask, request, jsonify
import joblib
import numpy as np
from model_utils import preprocess_input
from rag_pipeline import get_rag_response

app = Flask(__name__)
model = joblib.load("ml_models/attention_model.pkl")  # Load your trained model

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = preprocess_input(data["landmarks"])
    prediction = model.predict([features])
    solution = get_rag_response(prediction[0])
    return jsonify({"prediction": int(prediction[0]), "solution": solution})

if __name__ == '__main__':
    app.run(debug=True)
