from tweetkit.twitter import *

with open('secrets/bearer_token.txt', 'r') as fp:
    bearer_token = fp.read().strip()

if __name__ == '__main__':
    auth = dict(bearer_token=bearer_token)
    client = TwitterClient(auth=auth)
    # status = client.stream.rules.add([
    #     # {"value": "cat has:media", "tag": "cats with media"},
    #     # {"value": "cat has:media -grumpy", "tag": "happy cats with media"},
    #     # {"value": "meme", "tag": "funny things"},
    #     # {"value": "meme has:images"}
    # ])
    # print(status)
    status = client.stream.rules.get()
    print(status)
    for tweet in client.stream():
        assert client.response['data'] == tweet
        print(tweet)
        break
    status = client.stream.rules.delete()
    print(status)
