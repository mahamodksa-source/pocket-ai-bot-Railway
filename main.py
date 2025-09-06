import os
import time
from datetime import datetime
from notifier import Notifier

# إعدادات
TRADE_INTERVAL_MINUTES = int(os.getenv("TRADE_INTERVAL_minutes", "30"))
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", "2"))
USE_DEMO = os.getenv("USE_DEMO", "true").lower() == "true"

# أنشئ notifier
notifier = Notifier()

def get_signal():
    # دالة وهمية (تعدل لاحقًا بالذكاء الاصطناعي)
    import random
    return random.choice(["call", "put", None])

def main_loop():
    while True:
        try:
            signal = get_signal()
            if signal:
                status = "pending"
                # ترسل إشعار بتنفيذ الصفقة
                notifier.send_text(f"🚀 إشارة جديدة: {signal} | المبلغ: {TRADE_AMOUNT} | الحالة: {status}")
            
            # تنتظر الفترة المحددة
            time.sleep(TRADE_INTERVAL_MINUTES * 60)

        except Exception as e:
            notifier.send_text(f"❌ خطأ: {str(e)}")
            time.sleep(10)  # إعادة المحاولة بعد 10 ثواني

if __name__ == "__main__":
    # رسالة اختبار عند التشغيل
    notifier.send_text("✅ البوت اشتغل الآن!")
    main_loop()
