from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Nifty Scalping Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)
    return jsonify({"status": "success", "data": data})