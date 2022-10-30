from tweetkit.auth import BearerTokenAuth
from tweetkit.client import TwitterClient

rules = [
    {'value': "twitter lang:en", "tag": "twitter messages"}
]

with open('secrets/bearer_token.txt', 'r', encoding='utf-8') as fp:
    auth = BearerTokenAuth(fp.read())
    assert len(auth.bearer_token) > 0, 'Unable to load the bearer token.'

client = TwitterClient(auth=auth)

# get all existing rules
prv_rules = client.tweets.get_rules()

if prv_rules is not None:
    if prv_rules.errors is not None:
        raise prv_rules.errors[0]
    else:
        prv_rules_ids = prv_rules.get('id')
        # delete all rules if exist
        status = None
        if prv_rules_ids:
            print('Deleting rules: [{}]'.format(', '.join(prv_rules_ids)))
            status = client.tweets.add_or_delete_rules({'delete': {'ids': prv_rules_ids}})
        if status is not None and status.errors is not None:
            raise status.errors[0]

# add new rules
status = client.tweets.add_or_delete_rules({'add': rules})

if status.errors is not None and len(status.errors) > 0:
    raise status.errors[0]

collection = []
with client.tweets.search_stream() as stream:
    for tweet in stream.content:
        collection.append(tweet)
        if len(collection) >= 1:
            break

print(collection)
