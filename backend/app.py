from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import base64
from io import BytesIO
import joblib
import random
import os

app = Flask(__name__)
model = joblib.load("../ml_models/attention_model.pkl")

attention_tips = {
    "low": [
        "Try taking a short break to refocus.",
        "Minimize distractions around you.",
        "Practice deep breathing for 2 minutes."
    ],
    "high": [
        "You're doing great! Keep going!",
        "Maintain this level of focus.",
        "Consider pushing forward on challenging tasks."
    ]
}

def preprocess_image(base64_image):
    image = Image.open(BytesIO(base64.b64decode(base64_image.split(',')[1])))
    image = image.resize((64, 64)).convert('L')
    return np.array(image).reshape(1, -1) / 255.0

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    image_data = data['image']
    features = preprocess_image(image_data)
    prediction = model.predict(features)[0]

    state = "high" if prediction == 1 else "low"
    tip = random.choice(attention_tips[state])

    return jsonify({"state": int(prediction), "tip": tip})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
