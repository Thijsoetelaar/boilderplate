from flask import Flask, jsonify, request
from example_package.example import add_one

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def numeber():
    if request.method=='POST':
        posted_data = request.get_json()
        number = posted_data['number']
        return jsonify(f"When you add 1 to {number} you get {add_one(number)}")

if __name__ == '__main__':
    app.run(debug=True)