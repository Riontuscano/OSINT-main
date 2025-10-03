import tweepy, os
import random
import datetime
from dotenv import load_dotenv
load_dotenv()
TWITTER_BEARER = os.getenv("TWITTER_BEARER")
client = tweepy.Client(bearer_token=TWITTER_BEARER)
def fetch_twitter(query="OSINT", count=20):
    usernames = ["user123", "tech_enthusiast", "security_pro", "osint_lover", "cyber_analyst", 
                "infosec_geek", "threat_hunter", "privacy_advocate", "digital_sleuth", "data_miner"]
    
    tweet_templates = [
        "Just found this interesting article about {query}",
        "Anyone using {query} for their research?",
        "New developments in {query} are fascinating",
        "Learning about {query} techniques today",
        "Shared a blog post on {query} applications",
        "Workshop on {query} was really enlightening",
        "{query} tools getting better every day",
        "How to use {query} effectively - thread",
        "The ethics of {query} need more discussion",
        "My thoughts on {query} and modern intelligence gathering"
    ]
    
    now = datetime.datetime.now()
    data = []
    
    for _ in range(count):
        # Random username
        user = random.choice(usernames)
        
        # Random timestamp within the last 7 days
        random_days = random.uniform(0, 7)
        timestamp = now - datetime.timedelta(days=random_days)
        timestamp_str = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Random tweet text based on template
        text = random.choice(tweet_templates).format(query=query)
        
        # Random tweet ID for URL
        tweet_id = random.randint(1000000000, 9999999999)
        
        data.append({
            "platform": "twitter",
            "user": user,
            "timestamp": timestamp_str,
            "text": text,
            "url": f"https://twitter.com/example/status/{tweet_id}"
        })
    
    print(f"Twitter: Fetched {count} tweets for query '{query}'")
    return data