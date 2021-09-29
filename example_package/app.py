import pandas as pd
import os

from flask import Flask, jsonify, request
from joblib import load
from utils import add_one
# from example_package.example import add_one

# Load in model
current_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
clf = load(os.path.join(current_dir,'models/model.joblib'))

app = Flask(__name__)

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
        # df = pd.DataFrame.from_dict(posted_data)
        df = pd.json_normalize(posted_data)
        print(df)

        # Load model, maybe take this out
        class_ = clf.predict(df)[0]
        proba = clf.predict_proba(df)[:, 1] #predict_proba
        return jsonify(f"Class is: {class_} with probability: {proba[0].round(3)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)