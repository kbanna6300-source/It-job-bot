import feedparser

def fetch_jobs():
    jobs = []
    
    # 1. Standard Job Links
    standard_jobs = [
        {
            "title": "Desktop Support Engineer Jobs",
            "company": "Naukri.com",
            "location": "India",
            "link": "https://www.naukri.com/desktop-support-engineer-jobs"
        },
        {
            "title": "IT Helpdesk / Service Desk Jobs",
            "company": "LinkedIn Jobs",
            "location": "India",
            "link": "https://www.linkedin.com/jobs/search/?keywords=desktop%20support"
        }
    ]
    jobs.extend(standard_jobs)

    # 2. Aapka Google Alert Feed (LinkedIn Posts)
    rss_url = "https://www.google.com/alerts/feeds/13318065566925002046/7814502131971754024"
    
    try:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:5]:  # Top 5 latest posts
            jobs.append({
                "title": f"LinkedIn Post: {entry.title}",
                "company": "Direct Recruiter Post",
                "location": "Check Post",
                "link": entry.link
            })
    except Exception as e:
        print(f"Error fetching RSS: {e}")

    return jobs
