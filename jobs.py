import feedparser
import urllib.parse

def fetch_jobs():
    jobs = []
    
    # 1. Direct Search Links (Standard Job Boards)
    standard_jobs = [
        {
            "title": "Desktop Support Engineer L1",
            "company": "LinkedIn Hiring Posts",
            "location": "Mumbai / Remote",
            "link": "https://www.linkedin.com/search/results/content/?keywords=hiring%20desktop%20support"
        },
        {
            "title": "Service Desk & Helpdesk Posts",
            "company": "LinkedIn User Posts",
            "location": "India",
            "link": "https://www.linkedin.com/search/results/content/?keywords=hiring%20service%20desk"
        }
    ]
    jobs.extend(standard_jobs)

    # 2. LinkedIn Posts via Google Alerts RSS
    keywords = ["hiring desktop support", "hiring helpdesk technician"]
    for query in keywords:
        encoded_query = urllib.parse.quote(f'site:linkedin.com/posts "{query}"')
        rss_url = f"https://www.google.com/alerts/feeds/12345678/search?q={encoded_query}"
        
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:3]: # Har query se top 3 posts
            jobs.append({
                "title": f"LinkedIn Post: {entry.title}",
                "company": "Direct Recruiter Post",
                "location": "Check Post Details",
                "link": entry.link
            })

    return jobs
