from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/location")
def location():
    data = {
        "location": "Classroom",
        "latitude": 10.7905,
        "longitude": 79.1378
    }
    return jsonify(data)

@app.route("/")
def home():
    return "GPS Microservice Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)