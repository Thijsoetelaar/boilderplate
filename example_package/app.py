from flask import Flask, jsonify, request
# from example_package.example import add_one
from example import add_one

app = Flask(__name__)

# def add_one(number):
#    return number + 1

@app.route("/add", methods=["POST"])
def number():
    if request.method=='POST':
        posted_data = request.get_json()
        number = posted_data['number']
        return jsonify(f"When you add 1 to {number} you get {add_one(number)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)