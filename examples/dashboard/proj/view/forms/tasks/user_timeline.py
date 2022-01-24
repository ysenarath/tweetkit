from wtforms import (
    validators,
    IntegerField
)

from proj.view.forms.tasks.base import TaskForm


class UserTimelineForm(TaskForm):
    id = IntegerField('User ID')
    username = IntegerField('Username')
