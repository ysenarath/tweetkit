from wtforms import (
    validators,
    TextAreaField,
)

from proj.view.forms.tasks.base import TaskForm


class TweetStreamForm(TaskForm):
    rules = TextAreaField('Rules', [validators.Length(min=4, max=25), validators.DataRequired()])
