import time
from datetime import datetime, timezone
from pocket_option_api import PocketOption
from notifier import Notifier
from utils import append_trade, get_signal

# إعدادات
AMOUNT = 2  # قيمة الصفقة
CSV_FILE = "trades.csv"
TRADE_INTERVAL_MINUTES = 30  # كل 30 دقيقة

# تهيئة البوت
pocket = PocketOption()
notifier = Notifier()

def main_loop():
    last_report_time = None
    while True:
        try:
            # الحصول على إشارة
            signal = get_signal()  # 'call' أو 'put' أو None
            if signal:
                # تنفيذ الصفقة
                resp = pocket.place_trade(direction=signal, amount=AMOUNT)
                status = resp.get('status', 'pending')

                # حفظ الصفقة في CSV
                append_trade(CSV_FILE, {
                    'time': datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                    'signal': signal,
                    'status': status,
                    'amount': AMOUNT
                })

                # إرسال إشعار
                notifier.send_text(f"📊 صفقة جديدة: {signal} | النتيجة: {status}")

            # الانتظار 30 دقيقة
            time.sleep(TRADE_INTERVAL_MINUTES * 60)

        except Exception as e:
            notifier.send_text(f"❌ خطأ: {e}")
            time.sleep(60)  # لو صار خطأ، انتظر دقيقة وجرب تاني

if __name__ == "__main__":
    notifier.send_text("✅ البوت اشتغل بنجاح")
    main_loop()
