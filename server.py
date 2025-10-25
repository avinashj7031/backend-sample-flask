from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows React frontend to call API

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/api/data')
def get_data():
    return jsonify({"data": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
