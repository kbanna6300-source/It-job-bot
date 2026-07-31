import feedparser
import urllib.parse

def fetch_jobs():
    jobs = []
    
    # 1. Standard Job Searches (Naukri, LinkedIn Job Search)
    standard_jobs = [
        {
            "title": "Desktop Support Engineer Jobs",
            "company": "Naukri.com",
            "location": "India",
            "link": "https://www.naukri.com/desktop-support-engineer-jobs"
        },
        {
            "title": "IT Helpdesk / Service Desk Jobs",
            "company": "LinkedIn Job Board",
            "location": "India",
            "link": "https://www.linkedin.com/jobs/search/?keywords=desktop%20support"
        }
    ]
    jobs.extend(standard_jobs)

    # 2. LinkedIn Direct User/Recruiter Posts (Google Alerts RSS)
    keywords = ["hiring desktop support", "hiring helpdesk technician"]
    for query in keywords:
        encoded_query = urllib.parse.quote(f'site:linkedin.com/posts "{query}"')
        rss_url = f"https://www.google.com/alerts/feeds/12345678/search?q={encoded_query}"
        
        try:
            feed = feedparser.parse(rss_url)
            for entry in feed.entries[:2]:  # Top 2 posts per keyword
                jobs.append({
                    "title": f"LinkedIn Post: {entry.title}",
                    "company": "Direct Recruiter Post",
                    "location": "Check Post",
                    "link": entry.link
                })
        except Exception as e:
            print(f"RSS Fetch Error: {e}")

    return jobs
