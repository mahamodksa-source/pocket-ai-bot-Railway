import os
import time
import pandas as pd
from datetime import datetime, timedelta
from strategy import get_signal
from pocket_api import PocketClient
from telegram_bot import TelegramNotifier
from logger import append_trade


# إعداد المتغيرات من البيئة
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
AMOUNT = float(os.environ.get('TRADE_AMOUNT', '2'))
INTERVAL = int(os.environ.get('TRADE_INTERVAL_SECONDS', '60'))
USE_DEMO = os.environ.get('USE_DEMO', 'true').lower() == 'true'


# تهيئة العملاء
pocket = PocketClient(token=os.environ.get('POCKET_TOKEN'), use_demo=USE_DEMO)
notifier = TelegramNotifier(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)


# ملف حفظ الصفقات
CSV_FILE = 'trades.csv'


# دالة التقرير الأسبوعي بسيطة: ترسل كل يوم سبت تقرير
def weekly_report_if_needed(last_report_time):
    now = datetime.utcnow()
    # نرسل تقرير مرة في كل سبت (UTC) عند أول تشغيل بعد بداية اليوم
    if now.weekday() == 5:  # Saturday
        if last_report_time is None or (now - last_report_time) > timedelta(days=6):
            try:
                df = pd.read_csv(CSV_FILE)
                total = len(df)
                wins = len(df[df.status == 'win'])
                losses = len(df[df.status == 'loss'])
                msg = f"📅 تقرير أسبوعي\\nالإجمالي: {total}\\nالرابحة: {wins}\\nالخاسرة: {losses}"
            except FileNotFoundError:
                msg = "📅 تقرير أسبوعي\\nلا توجد صفقات مسجلة بعد."
            notifier.send_text(msg)
            return now
    return last_report_time





def main_loop():
print('بوت التداول شغال...')
last_report_time = None
while True:
try:
signal = get_signal() # 'call' او 'put' او None
if signal:
# تنفيذ صفقة بقيمة ثابتة
resp = pocket.place_trade(direction=signal, amount=AMOUNT)
# resp متوقع أن يحتوي على {'status': 'win'|'loss'|'pending', 'details': ...}
status = resp.get('status', 'pending')
# حفظ
append_trade(CSV_FILE, {
main_loop()
