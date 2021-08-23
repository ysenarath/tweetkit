from tweetkit.twitter import *

with open('secrets/bearer_token.txt', 'r') as fp:
    bearer_token = fp.read().strip()

if __name__ == '__main__':
    auth = dict(bearer_token=bearer_token)
    client = TwitterClient(auth=auth)
    try:
        for tweet in client.tweets.search('apple', max_results=100, max_retry_count=0):
            print(tweet)
    except TwitterException as e:
        print(e)
