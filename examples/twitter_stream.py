from tweetkit.twitter import *
from tweetkit.twitter.errors import TwitterException

import pprint

with open('secrets/bearer_token.txt', 'r') as fp:
    bearer_token = fp.read().strip()

if __name__ == '__main__':
    auth = dict(bearer_token=bearer_token)
    client = TwitterClient(auth=auth)
    try:
        client.stream.rules.delete()
    except TwitterException as ex:
        pass
    client.stream.rules.add({"value": "cat has:media", "tag": "cats with media"})
    for tweet in client.stream():
        pprint.pprint(tweet)
