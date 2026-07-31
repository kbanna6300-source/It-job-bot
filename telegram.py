import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

def send_telegram_message(text: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHANNEL_ID:
        print("❌ Error: BOT_TOKEN ya CHANNEL_ID missing hai!")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }

    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if result.get("ok"):
            print("✅ Telegram par message chala gaya!")
            return True
        else:
            print(f"❌ Telegram API Error: {result}")
            return False
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        return False
