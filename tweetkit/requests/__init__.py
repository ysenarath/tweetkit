"""All request types grouped by the major tag."""
from tweetkit.requests.bookmarks import Bookmarks
from tweetkit.requests.compliance import Compliance
from tweetkit.requests.general import General
from tweetkit.requests.lists import Lists
from tweetkit.requests.spaces import Spaces
from tweetkit.requests.tweets import Tweets
from tweetkit.requests.users import Users

__all__ = [
    'Bookmarks',
    'Compliance',
    'General',
    'Lists',
    'Spaces',
    'Tweets',
    'Users',
]
