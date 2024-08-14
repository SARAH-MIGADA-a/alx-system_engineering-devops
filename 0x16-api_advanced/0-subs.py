#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    
    # Define the URL to fetch data from the subreddit's about.json
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set the headers to include a custom User-Agent
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
    }
    
    try:
        # Send the request with no redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            # Parse the response as JSON
            data = response.json()
            # Extract the number of subscribers
            return data['data'].get('subscribers', 0)
        
        # If the subreddit is invalid or other error occurs, return 0
        return 0
    
    except requests.RequestException:
        # In case of a request exception, return 0
        return 0

