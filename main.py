import os
import requests
from jobs import fetch_jobs

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def send_telegram_message(job):
    message = f"""🚨 *{job['title']}*

🏢 *Company:* {job['company']}
📍 *Location:* {job['location']}

🔗 [Apply Here]({job['link']})"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Sent: {job['title']}")
        else:
            print(f"Failed to send: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    job_list = fetch_jobs()
    for job in job_list:
        send_telegram_message(job)
