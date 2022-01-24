from flask import Blueprint, render_template, request, flash, redirect, url_for

from proj.models import db, User
from proj.view.forms.auth.register import RegistrationForm
from proj.view.forms.auth.login import LoginForm

__all__ = [
    'view',
]

view = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')


@view.route('/login')
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, password=form.password.data)
        # authenticate user here
        flash('Thanks for registering')
        return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)


@view.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
