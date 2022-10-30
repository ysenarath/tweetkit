import datetime

from tweetkit.auth import BearerTokenAuth
from tweetkit.client import TwitterClient

with open('secrets/bearer_token.txt', 'r', encoding='utf-8') as fp:
    auth = BearerTokenAuth(fp.read())
    assert len(auth.bearer_token) > 0, 'Unable to load the bearer token.'

client = TwitterClient(auth=auth)

start_time = '2022-09-30T00:00:01Z'
end_time = '2022-09-30T12:00:00Z'

paginator = client.tweets.tweets_fullarchive_search(
    '(#Ian OR "Hurricane Ian" OR #HurricaneIan) -is:retweet has:videos',
    start_time=start_time,
    end_time=end_time,
    max_results=100,
    paginate=True,
)

tweets = []

start_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
end_time = datetime.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
percentage_remaining = 0.0
total_period = (end_time - start_time).total_seconds()
for tweet in paginator.content:
    created_at = datetime.datetime.strptime(tweet['data']['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    tweets.append(tweet)
    remaining_period = (end_time - created_at).total_seconds()
    percentage_remaining = round(remaining_period * 100 / total_period, 2)
    print('\rTweet Count: {:3.0f}%, {}'.format(percentage_remaining, len(tweets)), end='')
if percentage_remaining != 100.00:
    print('\rTweet Count: {:3.0f}%, {}'.format(100.00, len(tweets)), end='')

print(tweets)
