import requests
import os

class TelegramNotifier:
    def __init__(self, token=None, chat_id=None):
        self.token = token or os.getenv("TELEGRAM_TOKEN")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
        self.base_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_text(self, message: str):
        """
        يرسل رسالة نصية إلى تليجرام
        """
        if not self.token or not self.chat_id:
            raise ValueError("Telegram token and chat_id must be set")

        payload = {
            "chat_id": self.chat_id,
            "text": message
        }
        response = requests.post(self.base_url, data=payload)

        if response.status_code != 200:
            print(f"[TelegramNotifier] Failed to send: {response.text}")
        else:
            print(f"[TelegramNotifier] Message sent: {message}")
