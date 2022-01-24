from wtforms import (
    Form, validators,
    StringField,
    SelectField,
)


class TaskTypeForm(Form):
    type = SelectField('Task Type', validators=[validators.DataRequired()], choices=[
        ('tweet_search', 'Search Tweets'),
        ('tweet_stream', 'Filtered Stream'),
        ('user_lookup', 'Users Lookup'),
        ('user_timeline', 'User Tweet Timeline'),
    ])


class TaskForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])
    description = StringField('Description', validators=[validators.Optional()])
