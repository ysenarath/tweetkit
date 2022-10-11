"""Reimplements copy with json."""
from tweetkit.utils import json


def deepcopy(data):
    """Implements deep copy with json library.

    Parameters
    ----------
    data: typing.Any
        An object to geet the deep copy from.

    Returns
    -------
    copy: typing.Any
        A deep copy of a provided object.
    """
    return json.loads(json.dumps({'data': data}))['data']
