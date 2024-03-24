from flask import Flask, jsonify

app = Flask(__name__)

# Define your JSON data
data = {
    "1": "one",
    "2": "two"
}

@app.route('/')
def index():
    return 'Welcome to the home page!'

@app.route('/<key>')
def get_value(key):
    if key in data:
        return jsonify(data[key])
    else:
        return jsonify({"error": "Key not found"}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')