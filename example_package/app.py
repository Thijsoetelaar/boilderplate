import pandas as pd
from flask import Flask, jsonify, request
from joblib import load
# from example_package.example import add_one
from utils import add_one

app = Flask(__name__)

# def add_one(number):
#    return number + 1

@app.route("/add", methods=["POST"])
def number():
    if request.method=='POST':
        posted_data = request.get_json()
        number = posted_data['number']
        return jsonify(f"When you add 1 to {number} you get {add_one(number)}")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method=='POST':
        posted_data = request.get_json()
        df = pd.DataFrame.from_dict(posted_data, orient="index")

        # Load model, maybe take this out
        clf = load('models/model.joblib')
        result = clf.predict(df) #predict_proba
        return jsonify(f"{result}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)