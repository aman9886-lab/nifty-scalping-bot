from flask import Flask, request
import telegram
import os

app = Flask(__name__)
bot = telegram.Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
chat_id = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/")
def home():
    return "NIFTY Scalping Bot is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = f"🔔 *NIFTY Scalping Signal*\n\n📈 Entry: {data.get('entry')}\n🎯 Target 1: {data.get('target1')}\n🎯 Target 2: {data.get('target2')}\n🛑 Stop Loss: {data.get('sl')}\n💰 Premium: {data.get('premium')}\n\n#NIFTY #Options #Scalping"
    bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    return "Alert sent", 200