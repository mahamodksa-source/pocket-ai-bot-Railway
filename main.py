import os
import time
import pandas as pd
from datetime import datetime, timedelta
from strategy import get_signal
from pocket_api import PocketClient
from telegram_bot import TelegramNotifier
from logger import append_trade

from notifier import TelegramNotifier
import os

notifier = TelegramNotifier(
    token=os.environ.get("TELEGRAM_BOT_TOKEN"),
    chat_id=os.environ.get("TELEGRAM_CHAT_ID")
)

# إعداد المتغيرات من البيئة
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
AMOUNT = float(os.environ.get('TRADE_AMOUNT', '2'))
INTERVAL = int(os.environ.get('TRADE_INTERVAL_SECONDS', '60'))
USE_DEMO = os.environ.get('USE_DEMO', 'true').lower() == 'true'


# تهيئة العملاء
pocket = PocketClient(
    email=os.environ.get("POCKET_EMAIL"),
    password=os.environ.get("POCKET_PASSWORD"),
    use_demo=USE_DEMO
)


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
                msg = f"📅 تقرير أسبوعي\nالإجمالي: {total}\nالرابحة: {wins}\nالخاسرة: {losses}"
            except FileNotFoundError:
                msg = "📅 تقرير أسبوعي\nلا توجد صفقات مسجلة بعد."
            notifier.send_text(msg)
            return now
    return last_report_time






def main_loop():
    print("🚀 بوت التداول شغال...")

    last_report_time = None
    while True:
        try:
            signal = get_signal()  # 'call' أو 'put' أو None
            if signal:
                # تنفيذ صفقة بناءً على الإشارة
                resp = pocket.place_trade(direction=signal, amount=AMOUNT)
                # resp = {'status': 'win'|'loss'|'pending', 'details': ...}
                status = resp.get('status', 'pending')
                # حفظ الصفقة
                append_trade(CSV_FILE, {
                    'time': datetime.utcnow().isoformat(),
                    'signal': signal,
                    'status': status,
                    'amount': AMOUNT
                })
                notifier.send_text(f"📊 صفقة {signal} | النتيجة: {status}")

            # تقرير أسبوعي
            last_report_time = weekly_report_if_needed(last_report_time)

        except Exception as e:
            notifier.send_text(f"❌ خطأ: {str(e)}")

        time.sleep(TRADE_INTERVAL_MINUTES)


# تشغيل البوت
main_loop()
