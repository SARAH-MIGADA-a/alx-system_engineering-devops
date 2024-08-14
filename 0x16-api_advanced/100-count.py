#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, word_count={}, after=None):
    """Recursively queries Reddit API, parses titles of hot articles, and counts occurrences of given keywords."""

    # Prepare the headers and parameters for the API request
    headers = {'User-Agent': 'python:subreddit.keyword.counter:v1.0 (by /u/yourusername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    
    # Make the request to Reddit API
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')
        
        # Normalize the word list to lowercase
        word_list = [word.lower() for word in word_list]
        
        # Parse and count keywords in the titles
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in title.split():
                if word in word_list:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        
        # Recursively fetch the next page if 'after' is not None
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)
        else:
            # Once recursion is complete, sort and print the results
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
            return
    
    except requests.RequestException:
        return


