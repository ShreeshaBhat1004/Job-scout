# config.py

# Twitter API credentials
API_KEY = "YOUR_API_KEY"
API_KEY_SECRET = "YOUR_API_KEY_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
BEARER_TOKEN = "YOUR_BEARER_TOKEN"

# Specify search parameters for Twitter API
SEARCH_QUERY = """
("Machine Learning" OR "ML Engineer" OR "Data Scientist" OR "AI Engineer" OR "Deep Learning") 
(#hiring OR #job OR #jobopening OR #nowhiring OR #remote OR "work from home") 
lang:en -is:retweet
"""
