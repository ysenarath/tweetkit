from wtforms import (
    validators,
    StringField,
    TextAreaField,
    DateTimeField,
    SelectMultipleField,
    IntegerField,
)

from proj.view.forms.tasks.base import TaskForm


class TweetSearchForm(TaskForm):
    query = TextAreaField('Query', [validators.Length(min=4, max=25), validators.DataRequired()])
    end_time = DateTimeField('End Time')
    start_time = DateTimeField('Start Time')
    expansions = SelectMultipleField('Expansions')
    max_results = IntegerField('Max Results')
    media_fields = IntegerField('Media Fields')
    next_token = StringField('Next Token')
