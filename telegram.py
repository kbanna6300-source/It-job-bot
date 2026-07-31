import os
import requests
import feedparser

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def fetch_jobs():
    jobs = []
    
    # 1. GOOGLE ALERT RSS (LinkedIn Recruiter Posts)
    google_rss_url = "https://www.google.com/alerts/feeds/13318065566925002046/7814502131971754024"
    try:
        g_feed = feedparser.parse(google_rss_url)
        for entry in g_feed.entries[:5]:
            jobs.append({
                "type": "RECRUITER_POST",
                "title": entry.title,
                "summary": entry.summary if 'summary' in entry else "LinkedIn post details available in link.",
                "link": entry.link
            })
    except Exception as e:
        print(f"Error RSS: {e}")

    # 2. DIRECT PORTALS
    jobs.append({
        "type": "PORTAL",
        "title": "Desktop Support / Helpdesk Urgent Openings",
        "company": "Naukri & LinkedIn Direct Search",
        "location": "Pan India / Remote",
        "role_details": "L1/L2 Desktop Support, Hardware & Networking, Troubleshooting, Service Desk",
        "link": "https://www.naukri.com/desktop-support-jobs"
    })

    return jobs

def send_telegram_message(job):
    if job.get("type") == "RECRUITER_POST":
        # Recruiter direct post format
        message = f"""📢 *DIRECT RECRUITER / HR POST*

📌 *Post Heading:*
{job['title']}

📄 *Details & Requirements:*
{job['summary'][:300]}...

💡 *Kevi Rite Apply Karvu?*
1. Niche aapeli link par click karo.
2. Direct Recruiter/HR ni LinkedIn post kholse.
3. Post ma aapeil HR Email ID par CV moklo OR Direct Message (DM) karo.

🔗 *Direct Post Link:*
{job['link']}"""

    else:
        # Standard Job Portal format
        message = f"""💼 *DIRECT COMPANY JOB BOARD*

📌 *Role:* {job['title']}
🏢 *Portal/Company:* {job['company']}
📍 *Location:* {job['location']}

📄 *Required Skills:* 
{job['role_details']}

💡 *Kevi Rite Apply Karvu?*
1. Link kholi ne portal par login karo.
2. "Apply" button par click karine tamaro Updated CV upload karo.

🔗 *Apply Link:*
{job['link']}"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False  # Enabels Photo/Link Preview inside Telegram!
    }
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    job_list = fetch_jobs()
    for job in job_list:
        send_telegram_message(job)
