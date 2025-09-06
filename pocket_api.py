import requests
import os

class PocketClient:
    def __init__(self, email=None, password=None, use_demo=True):
        self.email = email or os.getenv("POCKET_EMAIL")
        self.password = password or os.getenv("POCKET_PASSWORD")
        self.use_demo = use_demo
        self.base_url = "https://api.pocketoption.com/demo" if use_demo else "https://api.pocketoption.com/real"

    def connect(self):
        """
        هنا نعمل عملية تسجيل دخول وهمية أو تحقق من القيم
        """
        if not self.email or not self.password:
            raise ValueError("Email and password are required for Pocket Option login")
        
        print(f"[PocketClient] Connected with email={self.email}, demo={self.use_demo}")
        return True

    def place_trade(self, direction="call", amount=1):
        """
        محاكاة تنفيذ صفقة
        direction: 'call' أو 'put'
        amount: المبلغ المراد تداوله
        """
        if direction not in ["call", "put"]:
            raise ValueError("Direction must be 'call' or 'put'")
        
        # هنا ممكن نضيف API حقيقي لو عندك
        print(f"[PocketClient] Placing trade: {direction} with {amount}$")

        # محاكاة استجابة السيرفر
        response = {
            "status": "win",   # أو 'loss' أو 'pending'
            "details": {
                "direction": direction,
                "amount": amount
            }
        }
        return response
