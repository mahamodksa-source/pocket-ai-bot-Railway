import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class Notifier:
    def send_text(self, message):
        if not TOKEN or not CHAT_ID:
            print("⚠️ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")
            return

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}

        try:
            response = requests.post(url, data=payload)
            if response.status_code != 200:
                print(f"❌ Telegram error: {response.text}")
        except Exception as e:
            print(f"❌ Error sending telegram message: {e}")
