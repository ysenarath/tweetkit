from tweetkit.twitter import *

with open('secrets/bearer_token.txt', 'r') as fp:
    bearer_token = fp.read().strip()

if __name__ == '__main__':
    auth = TwitterAuth(bearer_token=bearer_token)
    client = TwitterClient(auth=auth)
    try:
        user = client.users.by('twitter')
        print(user)
    except TwitterException as e:
        print(e)
