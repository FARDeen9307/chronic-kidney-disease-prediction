from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Load your trained model using joblib
model = joblib.load("best_random_forest_model.pkl")

@app.route("/", methods=["GET"])
def home():
    return "CKD Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Receive JSON input
        df = pd.DataFrame([data])  # Convert input to DataFrame
        prediction = model.predict(df)[0]  # Predict class (0 or 1)
        return jsonify({"prediction": int(prediction)})  # Return prediction as int
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("App started")
    app.run(debug=True)



