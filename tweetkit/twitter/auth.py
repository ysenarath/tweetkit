from marshmallow import Schema, fields, post_load, validate

__all__ = [
    'TwitterAuth',
    'TwitterAuthSchema',
]

TOKEN_TYPES = [
    'access_token',
    'bearer_token',
    'basic',
]


class TwitterAuth:
    def __init__(self, bearer_token=None):
        if bearer_token is not None:
            self.type = 'bearer_token'
        self.bearer_token = bearer_token

    def __repr__(self):
        return '<TwitterAuth {}>'.format(self.type)

    def to_dict(self):
        schema = TwitterAuthSchema(many=False)
        return schema.dump(self)


class TwitterAuthSchema(Schema):
    type = fields.String(validate=validate.OneOf(TOKEN_TYPES), dump_only=True)
    bearer_token = fields.String()

    @post_load
    def to_object(self, data, **kwargs):
        return TwitterAuth(**data)
