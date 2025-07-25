
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data:
        message = data.get("message", "📢 Test Alert from NIFTY Bot 🚀")
        send_telegram_message(message)
        return jsonify({"status": "sent"}), 200
    return jsonify({"error": "no data"}), 400

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

@app.route("/", methods=["GET"])
def home():
    return "✅ NIFTY Scalping Bot is Live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
