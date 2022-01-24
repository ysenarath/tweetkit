from flask import Blueprint, render_template, request, url_for, redirect

__all__ = [
    'view',
]

from proj.view.forms.tasks.base import TaskTypeForm
from proj.view.forms.tasks.tweet_search import TweetSearchForm
from proj.view.forms.tasks.tweet_stream import TweetStreamForm
from proj.view.forms.tasks.user_lookup import UserLookupForm
from proj.view.forms.tasks.user_timeline import UserTimelineForm

view = Blueprint('base', __name__, template_folder='templates')


@view.route('/')
def index():
    return render_template('index.html')


@view.route('/discover')
def discover():
    return render_template('discover.html')


@view.route('/tasks', methods=['GET', 'POST'])
def tasks():
    task_type_form = TaskTypeForm(request.form, type='tweet_search')
    task_type = task_type_form.type.data
    if request.method == 'POST' and task_type_form.validate():
        task_type = task_type_form.type.data
    if task_type == 'tweet_search':
        task_form = TweetSearchForm()
    elif task_type == 'tweet_stream':
        task_form = TweetStreamForm()
    elif task_type == 'user_lookup':
        task_form = UserLookupForm()
    elif task_type == 'user_timeline':
        task_form = UserTimelineForm()
    else:
        task_form = None
    return render_template('tasks.html', task_type_form=task_type_form, task_form=task_form)


@view.route('/tasks/<task_id>')
def task(task_id):
    form = TweetSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('tasks.html', form=form)


@view.route('/settings')
def settings():
    return render_template('settings.html')
