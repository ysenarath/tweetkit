"""Extended JSON functionality."""
import collections
import io
import json as simplejson
import os
import typing

import requests
from requests.utils import guess_json_utf

from tweetkit.exceptions import JSONDecodeError

__all__ = [
    'loads',
    'dumps',
    'dump',
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


def dumps(obj, *args, **kwargs):
    """Get JSON string.

    Parameters
    ----------
    obj: typing.Mapping or typing.Sequence or object
        Object(s) to save.
    args: typing.Any
        Other arguments to simplejson.dump.
    kwargs: typing.Any
        Other keyword arguments to simplejson.dump.

    Returns
    -------
    s: str
        The string representation of the input string object.
    """
    return simplejson.dumps(obj, *args, **kwargs)


def dump(obj, fp, *args, **kwargs):
    """Save object to a file.

    Parameters
    ----------
    obj: dict or object
        Object(s) to save.
    fp: str, path object, file-like object, or None, default None
        Path or IO to save the object.
    args: typing.Any
        Other arguments to simplejson.dump.
    kwargs: typing.Any
        Other keyword arguments to simplejson.dump.

    Returns
    -------
    None
    """
    if hasattr(fp, 'name'):
        is_jsonline = os.path.abspath(fp.name).endswith('.jsonl')
    elif isinstance(fp, str):
        is_jsonline = os.path.abspath(fp).endswith('.jsonl')
    else:
        is_jsonline = False
    if is_jsonline:
        output = io.StringIO()
        if not isinstance(obj, collections.Sequence):
            obj = obj,
        for item in obj:
            line = simplejson.dumps(item, *args, **kwargs)
            output.write('{}\n'.format(line))
        lines = output.getvalue()
        output.close()
    else:
        lines = simplejson.dumps(obj, *args, **kwargs)
    if isinstance(fp, str):
        with open(fp, mode='w', encoding='utf-8') as fp:
            fp.write(lines)
    else:
        fp.write(lines)
