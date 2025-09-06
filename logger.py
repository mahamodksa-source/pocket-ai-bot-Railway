import os


FIELDNAMES = ['time', 'direction', 'amount', 'status', 'raw']


def append_trade(filename, row: dict):
exists = os.path.exists(filename)
with open(filename, 'a', newline='', encoding='utf-8') as f:
writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
if not exists:
writer.writeheader()
writer.writerow({k: row.get(k, '') for k in FIELDNAMES})
