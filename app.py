from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)
user_locations = {}

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/send-location", methods=["POST"])
def receive_location():
    data = request.json
    ip = request.remote_addr
    lat = data.get("latitude")
    lon = data.get("longitude")
    if lat and lon:
        user_locations[ip] = {
            "latitude": lat,
            "longitude": lon,
            "timestamp": time.time()
        }
    return jsonify({"status": "success"})

# Konumları harita üzerinde göreceğin yeni adres
@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/locations")
def get_locations():
    # Tüm kullanıcıların konumlarını liste olarak gönderir
    return jsonify(list(user_locations.values()))

if __name__ == "__main__":
    # Mac port çakışmasını önlemek için 5001 portu
    app.run(debug=True, port=5001)
