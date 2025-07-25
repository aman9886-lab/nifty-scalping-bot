from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Nifty Scalping Bot is live."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received:", data)
    return {"status": "received"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
