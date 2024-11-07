from utils.twitter_search import search_ml_jobs_twitter
from utils.hackernews_scraper import fetch_remote_hackernews_jobs
from utils.pdf_extractor import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import config

def compute_similarity(profile_text, job_texts):
    documents = [profile_text] + [job['description'] for job in job_texts]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    return cosine_similarities

def recommend_jobs(pdf_path):
    profile_text = extract_text_from_pdf(pdf_path)
    
    hackernews_jobs = fetch_remote_hackernews_jobs()
    twitter_jobs = search_ml_jobs_twitter()
    
    all_jobs = hackernews_jobs + twitter_jobs
    similarities = compute_similarity(profile_text, all_jobs)
    
    ranked_jobs = sorted(
        zip(similarities, all_jobs),
        key=lambda x: x[0],
        reverse=True
    )
    
    print("Top Machine Learning Remote Job Recommendations:\n")
    for score, job in ranked_jobs[:10]:  
        print(f"Job Title: {job['title']}")
        print(f"Job URL: {job['url']}")
        print(f"Similarity Score: {score:.4f}\n")

pdf_path = input("Please provide the path to your resume PDF: ")
recommend_jobs(pdf_path)
