"""All request types grouped by the major tag."""
from tweetkit.twitter.requests.bookmarks import Bookmarks
from tweetkit.twitter.requests.compliance import Compliance
from tweetkit.twitter.requests.general import General
from tweetkit.twitter.requests.lists import Lists
from tweetkit.twitter.requests.spaces import Spaces
from tweetkit.twitter.requests.tweets import Tweets
from tweetkit.twitter.requests.users import Users

__all__ = [
    'Bookmarks',
    'Compliance',
    'General',
    'Lists',
    'Spaces',
    'Tweets',
    'Users',
]
