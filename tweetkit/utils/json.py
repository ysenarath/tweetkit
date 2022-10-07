"""Extended JSON functionality."""
import json as simplejson

import requests
from requests.utils import guess_json_utf

from tweetkit.exceptions import JSONDecodeError

__all__ = [
    'json'
]


def loads(s):
    """Load a JSON string to a dict.

    Parameters
    ----------
    s: str or requests.Response
        A string input.

    Returns
    -------
    data: dict
        Loaded repr.
    """
    if isinstance(s, requests.Response):
        text = s.text
        if not s.encoding and s.content and len(s.content) > 3:
            encoding = guess_json_utf(s.content)
            if encoding is not None:
                try:
                    text = s.content.decode(encoding)
                except UnicodeDecodeError:
                    pass
        s = text
    try:
        data = simplejson.loads(s)
    except simplejson.JSONDecodeError as ex:
        # JSONDecodeError but from local mixin
        raise JSONDecodeError(ex.msg, ex.doc, ex.pos) from ex
    else:
        return data
