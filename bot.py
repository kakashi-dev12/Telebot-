from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8200264869:AAHvn9drVXLiN_fwr-55jJw1QLgy1kaMtaI"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Received:", data)  # for Render log debug
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        reply = "Aur btao 👀"
        requests.post(URL, json={"chat_id": chat_id, "text": reply})
    return "ok", 200

@app.route('/')
def home():
    return "🤖 Bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
