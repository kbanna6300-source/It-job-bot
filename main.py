from jobs import fetch_jobs
from telegram import send_telegram_message

def run():
    print("🔍 Searching for IT Jobs...")
    jobs = fetch_jobs()

    if not jobs:
        print("Aapke keywords se match hoti hui koi job nahi mili.")
        return

    print(f"✅ Total {len(jobs)} jobs mili hain! Telegram par bhej rahe hain...\n")

    for job in jobs:
        message = (
            f"🚨 *New IT Job Update!*\n\n"
            f"📌 *Role:* {job['title']}\n"
            f"🏢 *Company:* {job['company']}\n"
            f"📍 *Location:* {job['location']}\n\n"
            f"🔗 [Apply Here]({job['link']})"
        )
        send_telegram_message(message)

if __name__ == "__main__":
    run()
