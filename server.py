# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests (so phones can access)

# store last known location
last_location = {"lat": None, "lon": None}

@app.route('/update', methods=['POST'])
def update_location():
    global last_location
    data = request.json
    last_location["lat"] = data.get("lat")
    last_location["lon"] = data.get("lon")
    return jsonify({"status": "ok", "message": "Location updated"})

@app.route('/get', methods=['GET'])
def get_location():
    return jsonify(last_location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
