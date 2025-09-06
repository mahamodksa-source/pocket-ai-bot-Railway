# ملف الاستراتيجية (مبسط) — هنا تضع موديل الـ AI أو خوارزمية التداول
# حالياً يعطي إشارة عشوائية كمثال. استبدله بخوارزمية LSTM أو XGBoost أو إشارة خارجية.
import random


def get_signal():
"""ترجع 'call' أو 'put' أو None (لا تنفيذ)."""
# مثال تجريبي: 30% احتمال دخول صفقة، ونختار عشوائياً اتجاه
if random.random() < 0.3:
return random.choice(['call', 'put'])
return None
