from flask import Flask, jsonify, request
import os
import subprocess

app = Flask(__name__)

# Get greeting from environment variable or default to "Hello, World!"
GREETING = os.environ.get("GREETING", "Hello, World!")

@app.route("/")
def hello():
    return GREETING

@app.route("/data")
def data():
    data = {
        "samples": [
            {"name": "one", "id": "7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed"},
            {"name": "two", "id": "3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3"},
            {"name": "three", "id": "8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f"}
        ]
    }

    # Check if the request is made from a browser
    user_agent = request.headers.get('User-Agent')
    if 'Mozilla' in user_agent:
        # Run parse_data.py only if the request is made from a browser
        subprocess.run(["python", "parse_data.py"])

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
