#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit."""
    
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set the headers with a custom User-Agent
    headers = {
        'User-Agent': 'python:subreddit.hot.articles:v1.0 (by /u/yourusername)'
    }
    
    # Define the parameters, including 'after' for pagination
    params = {'after': after, 'limit': 100}
    
    try:
        # Make the request to the Reddit API with no redirects
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')
            
            # Append the titles of the articles to the hot_list
            hot_list.extend([article.get('data', {}).get('title') for article in articles])
            
            # If 'after' is not None, recurse with the next page
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        
        else:
            # Return None if the subreddit is invalid
            return None
    
    except requests.RequestException:
        # Return None if there is a request exception
        return None

