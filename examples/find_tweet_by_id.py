from tweetkit.auth import BearerTokenAuth
from tweetkit.client import TwitterClient

with open('secrets/bearer_token.txt', 'r', encoding='utf-8') as fp:
    auth = BearerTokenAuth(fp.read())
    assert len(auth.bearer_token) > 0, 'Unable to load the bearer token.'

client = TwitterClient(auth=auth)

tweet_id = 20

reply = client.tweets.find_tweet_by_id(tweet_id)

tweet = reply.content

print(tweet)
