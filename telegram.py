import os
import requests
import feedparser

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def fetch_jobs():
    jobs = []
    
    # 1. Google Alert RSS Feed (Direct Recruiter Hiring Posts)
    google_rss_url = "https://www.google.com/alerts/feeds/13318065566925002046/7814502131971754024"
    try:
        g_feed = feedparser.parse(google_rss_url)
        for entry in g_feed.entries[:5]:
            # Simple clean details extraction
            clean_title = entry.title.replace("<b>", "").replace("</b>", "")
            jobs.append({
                "type": "RECRUITER",
                "title": clean_title,
                "summary": entry.summary if 'summary' in entry else "Direct LinkedIn Recruiter Hiring Post",
                "link": entry.link
            })
    except Exception as e:
        print(f"Error RSS: {e}")

    # 2. Direct India Specific Openings
    jobs.append({
        "type": "DIRECT",
        "title": "Desktop Support / Helpdesk Engineer Openings",
        "company": "Naukri India Jobs",
        "location": "India (PAN India / Remote)",
        "details": "Requirement for L1/L2 Desktop Support, Hardware, Networking & Service Desk Roles.",
        "link": "https://www.naukri.com/desktop-support-engineer-jobs-in-india"
    })

    return jobs

def send_telegram_message(job):
    if job.get("type") == "RECRUITER":
        message = f"""📢 *DIRECT HR / RECRUITER POST*

📌 *Role / Post:* 
{job['title']}

📄 *Details:*
{job['summary']}

💡 *Kevi rite apply karvu?*
1. Niche aapeil link par click karo.
2. Post ma aapeil HR email par CV moklo ya direct message (DM) karo.

🔗 [Click Here to View Post & Apply]({job['link']})"""
    else:
        message = f"""💼 *URGENT IT JOB OPENING*

📌 *Role:* {job['title']}
🏢 *Portal:* {job['company']}
📍 *Location:* {job['location']}

📄 *Skills Required:* 
{job['details']}

💡 *Kevi rite apply karvu?*
1. Link open karine portal par CV upload karo.

🔗 [Apply Here]({job['link']})"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    job_list = fetch_jobs()
    for job in job_list:
        send_telegram_message(job)
