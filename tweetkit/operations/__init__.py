"""All request types grouped by the major tag."""
from tweetkit.operations.bookmarks import Bookmarks
from tweetkit.operations.compliance import Compliance
from tweetkit.operations.general import General
from tweetkit.operations.lists import Lists
from tweetkit.operations.spaces import Spaces
from tweetkit.operations.tweets import Tweets
from tweetkit.operations.users import Users

__all__ = [
    'Bookmarks',
    'Compliance',
    'General',
    'Lists',
    'Spaces',
    'Tweets',
    'Users',
]
