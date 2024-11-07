import requests

def fetch_remote_hackernews_jobs():
    job_ids_url = 'https://hacker-news.firebaseio.com/v0/jobstories.json'
    job_ids = requests.get(job_ids_url).json()
    remote_keywords = ["remote", "work from home", "telecommute"]
    
    jobs = []
    for job_id in job_ids[:50]:  
        job_url = f'https://hacker-news.firebaseio.com/v0/item/{job_id}.json'
        job = requests.get(job_url).json()
        title = job.get('title', '').lower()
        description = job.get('text', '').lower()
        if any(keyword in title or keyword in description for keyword in remote_keywords):
            jobs.append({
                'title': job.get('title', 'No Title'),
                'url': job.get('url', f'https://news.ycombinator.com/item?id={job_id}'),
                'description': job.get('text', '')
            })
    return jobs
