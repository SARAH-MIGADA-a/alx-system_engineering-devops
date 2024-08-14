import requests

def count_words(subreddit, word_list, after='', word_count={}):
    # Normalize word_list to lowercase
    word_list = [word.lower() for word in word_list]

    # Setup the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python:subreddit.keyword.counter:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}

    # Make the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        return

    # Parse the JSON response
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after')

    # Count occurrences of each word in the word_list
    for post in posts:
        title = post.get('data', {}).get('title', '').lower().split()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + title.count(word)

    # If there are more pages, call the function recursively
    if after:
        return count_words(subreddit, word_list, after, word_count)

    # Sorting the word count dictionary
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    # Printing the results
    for word, count in sorted_word_count:
        if count > 0:
            print(f'{word}: {count}')


# Example Usage:
# count_words('programming', ['python', 'java', 'javascript'])

