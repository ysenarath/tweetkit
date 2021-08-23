from tweetkit.twitter import *

with open('secrets/bearer_token.txt', 'r') as fp:
    bearer_token = fp.read().strip()

if __name__ == '__main__':
    auth = dict(bearer_token=bearer_token)
    client = TwitterClient(auth=auth)
    try:
        user = client.users.by('twitterdev')
        user_id = user['id']
        for tweet in client.users.tweets(user_id):
            print(tweet)
    except TwitterException as e:
        print(e)
