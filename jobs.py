from config import JOB_KEYWORDS

def fetch_jobs():
    sample_jobs = [
        {
            "title": "Desktop Support Engineer L1",
            "company": "TechCorp Solutions",
            "location": "Mumbai / Remote",
            "link": "https://example.com/job1"
        },
        {
            "title": "Service Desk Analyst",
            "company": "Global IT Services",
            "location": "Bangalore / Hybrid",
            "link": "https://example.com/job2"
        },
        {
            "title": "IT Helpdesk Technician",
            "company": "InfoTech Pvt Ltd",
            "location": "Delhi NCR",
            "link": "https://example.com/job3"
        }
    ]

    filtered_jobs = []
    for job in sample_jobs:
        title_lower = job["title"].lower()
        if any(keyword.lower() in title_lower for keyword in JOB_KEYWORDS):
            filtered_jobs.append(job)

    return filtered_jobs
