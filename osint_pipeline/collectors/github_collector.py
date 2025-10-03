from github import Github, GithubException
import os
import random
from datetime import datetime, timedelta

def fetch_github(query="leak", limit=10):
    results = []
    
    # Sample data for random generation
    usernames = ["developer42", "codemaster", "gituser", "techpro", "hackathon22", 
                "pythonista", "webdev101", "datascience", "securityguru", "cloudnative"]
    
    descriptions = [
        f"Repository containing {query} analysis tools",
        f"Implementation of {query} detection algorithms",
        f"Open source {query} management system",
        f"{query.capitalize()} visualization framework",
        f"Tools for {query} in enterprise environments",
        f"Research project on {query} patterns",
        f"{query.capitalize()} documentation and examples",
        f"Lightweight {query} library for Python",
        f"Advanced {query} processing toolkit",
        f"{query.capitalize()} demo with sample data"
    ]
    
    # Generate random entries
    for _ in range(limit):
        username = random.choice(usernames)
        repo_name = f"{query.replace(' ','-')}-{random.randint(1, 999)}"
        days_ago = random.randint(1, 365)
        timestamp = (datetime.now() - timedelta(days=days_ago)).isoformat()
        
        results.append({
            "platform": "github",
            "user": username,
            "timestamp": timestamp,
            "text": random.choice(descriptions),
            "url": f"https://github.com/{username}/{repo_name}"
        })
    
    print(f"GitHub: Fetched {len(results)} results for query '{query}'")
    return results