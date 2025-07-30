from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = "Aur btao 👀"
        requests.post(URL, json={"chat_id": chat_id, "text": text})
    return "ok"

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run()
