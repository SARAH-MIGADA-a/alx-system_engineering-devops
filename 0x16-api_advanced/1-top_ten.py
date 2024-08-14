#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""
    
    # Define the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set the headers with a custom User-Agent
    headers = {
        'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'  # Customize this with your Reddit username
    }
    
    try:
        # Make the request to the Reddit API with no redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            # Check if posts are available
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print("No hot posts found.")
        
        elif response.status_code == 404:
            # Subreddit not found
            print(None)
        
        else:
            # Print None for any other unsuccessful status
            print(None)
    
    except requests.RequestException as e:
        # Print None if there is a request exception
        print(None)

