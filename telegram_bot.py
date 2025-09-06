from telegram import Bot


class TelegramNotifier:
def __init__(self, token, chat_id):
if not token or not chat_id:
raise ValueError('TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set')
self.bot = Bot(token=token)
self.chat_id = chat_id


def send_text(self, text):
try:
self.bot.send_message(chat_id=self.chat_id, text=text)
except Exception as e:
print('خطأ إرسال رسالة تيليجرام:', e)
