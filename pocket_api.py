

class PocketClient:
def __init__(self, email=None, password=None, use_demo=True):
self.email = email
self.password = password
self.use_demo = use_demo
self.session = requests.Session()
self.base_url = "https://pocketoption.com/api"
self.authenticated = False
self.login()


def login(self):
if not self.email or not self.password:
raise ValueError("يجب تحديد POCKET_EMAIL و POCKET_PASSWORD")
try:
resp = self.session.post(f"{self.base_url}/login/", data={
"email": self.email,
"password": self.password
})
if resp.status_code == 200 and "success" in resp.text:
self.authenticated = True
print("تم تسجيل الدخول بنجاح")
else:
print("فشل تسجيل الدخول:", resp.text)
except Exception as e:
print("خطأ أثناء تسجيل الدخول:", e)


def place_trade(self, direction='call', amount=2.0):
if not self.authenticated:
return {'status': 'error', 'details': 'not logged in'}
# ⚠️ ملاحظة: هذه مجرد محاكاة. تحتاج تعرف Endpoint الحقيقي لتنفيذ صفقة.
import random
r = random.random()
if r < 0.55:
status = 'win'
else:
status = 'loss'
return {'status': status, 'details': {'simulated': True}}
