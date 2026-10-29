import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY", "").strip()

if not BOT_TOKEN:
    print("[OGOHLANTIRISH] BOT_TOKEN topilmadi! Iltimos, .env faylida BOT_TOKEN ni to'ldiring.")
