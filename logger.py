import os
import csv

def append_trade(filename, trade_data):
    """
    يضيف صف جديد لملف CSV يحتوي بيانات الصفقة
    trade_data: dict فيه معلومات مثل { 'status': 'win'/'loss', 'signal': 'call'/'put', ... }
    """
    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as csvfile:
        fieldnames = trade_data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # إذا الملف جديد، نكتب الهيدر أول مرة
        if not file_exists:
            writer.writeheader()

        # نكتب بيانات الصفقة
        writer.writerow(trade_data)
        print(f"[Logger] Trade appended: {trade_data}")
