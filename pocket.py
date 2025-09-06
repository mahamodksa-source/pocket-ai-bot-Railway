import os
import random

class PocketClient:
    def __init__(self, email=None, password=None, use_demo=True):
        self.email = email or os.getenv("POCKET_EMAIL")
        self.password = password or os.getenv("POCKET_PASSWORD")
        self.use_demo = use_demo
        self.connected = False

    def connect(self):
        if not self.email or not self.password:
            raise ValueError("❌ لازم تضيف الإيميل والباسورد")
        # هنا محاكاة تسجيل دخول
        print(f"✅ تم تسجيل الدخول ({'Demo' if self.use_demo else 'Real'}) بحساب {self.email}")
        self.connected = True
        return True

    def get_balance(self):
        if not self.connected:
            raise RuntimeError("⚠️ لازم تتصل أول")
        # محاكاة رصيد عشوائي
        return round(random.uniform(50, 150), 2)

    def place_trade(self, asset="EURUSD", direction="call", amount=1, duration=1):
        if not self.connected:
            raise RuntimeError("⚠️ لازم تتصل أول")

        if direction not in ["call", "put"]:
            raise ValueError("❌ الاتجاه لازم يكون call أو put")

        print(f"📈 فتح صفقة {direction} على {asset} بمبلغ {amount}$ لمدة {duration} دقيقة")

        # محاكاة النتيجة
        result = random.choice(["win", "loss"])
        return {
            "status": result,
            "asset": asset,
            "direction": direction,
            "amount": amount,
            "duration": duration
        }
