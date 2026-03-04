from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8294549905:AAHV0Exj8kVUM0xrEABwqJLlEOnWEwhn1KY"
CHAT_ID = "17814065"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", str(data))
    result = send_telegram(f"📊 <b>BlueSky Alert</b>\n\n{message}")
    return jsonify({"status": "ok", "telegram": result})

@app.route("/", methods=["GET"])
def health():
    return "BlueSky Webhook is running! ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## File 2: `requirements.txt`
```
flask
requests
gunicorn
```

---

## File 3: `Procfile`
```
web: gunicorn app:app