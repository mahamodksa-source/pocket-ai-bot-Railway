import os
import time
import random
from pocket import PocketClient
from notifier import Notifier

# ====== إعدادات من المتغيرات ======
TRADE_INTERVAL_MINUTES = int(os.getenv("TRADE_INTERVAL_MINUTES", "30"))
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", "2"))
USE_DEMO = os.getenv("USE_DEMO", "true").lower() == "true"
EMAIL = os.getenv("POCKET_EMAIL")
PASSWORD = os.getenv("POCKET_PASSWORD")

# ====== notifier للتليجرام ======
notifier = Notifier()

# ====== تسجيل الدخول إلى Pocket Option ======
pocket = PocketClient(EMAIL, PASSWORD, use_demo=USE_DEMO)
if not pocket.connect():
    notifier.send_text("❌ فشل تسجيل الدخول إلى Pocket Option")
    exit(1)

balance = pocket.get_balance()
notifier.send_text(f"✅ البوت اشتغل الآن!\n💰 الرصيد الحالي: {balance}$")


def get_signal():
    """ إشارة وهمية (لاحقًا تتغير إلى ذكاء اصطناعي) """
    return random.choice(["call", "put", None])


def main_loop():
    while True:
        try:
            signal = get_signal()
            if signal:
                trade = pocket.place_trade(
                    asset="EURUSD",
                    direction=signal,
                    amount=TRADE_AMOUNT,
                    duration=1
                )
                notifier.send_text(
                    f"🚀 صفقة جديدة: {trade['direction']}\n"
                    f"💵 المبلغ: {trade['amount']}\n"
                    f"⏳ المدة: {trade['duration']} دقيقة\n"
                    f"📊 النتيجة: {trade['status']}"
                )

            time.sleep(TRADE_INTERVAL_MINUTES * 60)

        except Exception as e:
            notifier.send_text(f"❌ خطأ: {str(e)}")
            time.sleep(10)


if __name__ == "__main__":
    main_loop()
