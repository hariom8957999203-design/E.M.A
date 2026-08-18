import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Environment Variables se Token aur Chat ID uthayega
TELEGRAM_BOT_TOKEN = os.environ.get("8993700626:AAEbPXFm7lIPWMCEHWWQCdUKswUe8aary6k")
TELEGRAM_CHAT_ID = os.environ.get("8993700626")


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{8993700626:AAEbPXFm7lIPWMCEHWWQCdUKswUe8aary6k}/sendMessage"
    payload = {"chat_id": 8993700626, "text": msg, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram Error:", e)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return jsonify({"status": "no data"}), 400

    tf = data.get("timeframe", "N/A")
    sig = data.get("signal", "ALERT")
    strat = data.get("strategy", "5 EMA")

    emoji = "🟢 BUY SIGNAL" if sig == "BUY" else "🔴 SELL SIGNAL"

    msg = (
        f"🚨 *POWER OF STOCKS 5 EMA ALERT* 🚨\n\n"
        f"⏱️ *Timeframe:* {tf}\n"
        f"📊 *Type:* {emoji}\n"
        f"📈 *Strategy:* {strat}\n"
        f"💰 *Filter:* Stocks under ₹500\n\n"
        f"⚡ *Live Market Signal Triggered!*"
    )

    send_telegram(msg)
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
