# utils/twitter_search.py
import tweepy
import config

def search_ml_jobs_twitter():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    response = client.search_recent_tweets(
        query=config.SEARCH_QUERY, 
        max_results=config.MAX_TWEET_RESULTS,
        tweet_fields=["author_id", "created_at", "text"]
    )
    jobs = []
    for tweet in response.data:
        jobs.append({
            'title': "Tweet - " + tweet.text[:30],
            'url': f"https://twitter.com/user/status/{tweet.id}",
            'description': tweet.text
        })
    return jobs
