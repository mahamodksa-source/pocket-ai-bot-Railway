import os
import time
import random
from pocketoptionapi.stable_api import PocketOption
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
pocket = PocketOption(EMAIL, PASSWORD)
if not pocket.connect():
    notifier.send_text("❌ فشل تسجيل الدخول إلى Pocket Option")
    exit(1)

balance = pocket.get_balance()
notifier.send_text(f"✅ البوت اشتغل الآن!\n💰 الرصيد الحالي: {balance}")


def get_signal():
    """
    إشارة وهمية (لاحقًا تتغير إلى ذكاء اصطناعي)
    """
    return random.choice(["call", "put", None])


def main_loop():
    while True:
        try:
            signal = get_signal()
            if signal:
                # فتح صفقة
                status, order_id = pocket.buy(
                    amount=TRADE_AMOUNT,
                    asset="EURUSD",
                    direction=signal,
                    duration=1  # دقيقة واحدة
                )

                # إشعار مبدئي
                notifier.send_text(
                    f"🚀 صفقة جديدة: {signal}\n"
                    f"💵 المبلغ: {TRADE_AMOUNT}\n"
                    f"📊 الحالة: {status}\n"
                    f"🆔 رقم العملية: {order_id}"
                )

            # الانتظار للفترة المحددة
            time.sleep(TRADE_INTERVAL_MINUTES * 60)

        except Exception as e:
            notifier.send_text(f"❌ خطأ: {str(e)}")
            time.sleep(10)  # إعادة المحاولة بعد 10 ثواني


if __name__ == "__main__":
    main_loop()
