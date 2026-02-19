from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)
# Tüm kullanıcıların konum geçmişini tutan liste
all_locations = []

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/send-location", methods=["POST"])
def receive_location():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")
    user_id = request.remote_addr  # IP adresine göre kişileri ayırır
    
    if lat and lon:
        all_locations.append({
            "id": user_id,
            "latitude": lat,
            "longitude": lon,
            "timestamp": time.time()
        })
    return jsonify({"status": "success"})

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/locations")
def get_locations():
    return jsonify(all_locations)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
