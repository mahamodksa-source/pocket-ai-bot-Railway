import os
from pocketoptionapi.stable_api import PocketOption

EMAIL = os.getenv("POCKET_USERNAME") or os.getenv("POCKET_EMAIL")
PASSWORD = os.getenv("POCKET_PASSWORD")

print(f"Trying login with: {EMAIL}")

pocket = PocketOption(EMAIL, PASSWORD)
connected = pocket.connect()

if connected:
    print("✅ Logged in successfully!")
    print("Balance:", pocket.get_balance())
else:
    print("❌ Failed to login")
