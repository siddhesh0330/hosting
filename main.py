from flask import Flask, jsonify ,send_file
import os
app = Flask(__name__)
@app.route('/')
def index():
    return ''
@app.route('/<key>')
def get_value(key):
    # Construct the file path
    file_path = f'NLP/{key}.txt'
    if os.path.isfile(file_path):  # Check if file exists
        # Send the file to the client
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "Your Module not found"}), 404
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')


