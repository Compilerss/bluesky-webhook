from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

TELEGRAM_TOKEN = "8294549905:AAHV0Exj8kVUM0xrEABwqJLlEOnWEwhn1KY"
CHAT_ID = "17814065"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        raw = request.data.decode("utf-8")
        data = json.loads(raw)
        message = data.get("message", raw)
    except:
        message = request.data.decode("utf-8")
    
    result = send_telegram(message)
    return jsonify({"status": "ok", "telegram": result})

@app.route("/", methods=["GET"])
def health():
    return "BlueSky Webhook is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
