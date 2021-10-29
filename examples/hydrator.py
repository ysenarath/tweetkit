from tweetkit.twitter import *

with open('secrets/bearer_token.txt', 'r') as fp:
    bearer_token = fp.read().strip()

with open('hydrator_input.txt', 'r') as fp:
    tweet_ids = fp.read().strip().split('\n')

if __name__ == '__main__':
    auth = TwitterAuth(bearer_token=bearer_token)
    client = TwitterClient(auth=auth)
    try:
        for tweet_id in tweet_ids:
            tweet = client.tweets.get(tweet_id)
            print(tweet)
    except TwitterException as e:
        print(e)
