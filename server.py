from flask import Flask, request, jsonify
from emotion_detector import emotion_predictor


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Emotion Detection API!"


@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content


@app.route('/predict', methods=['POST'])
def predict():
    text = request.json.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = emotion_predictor(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
