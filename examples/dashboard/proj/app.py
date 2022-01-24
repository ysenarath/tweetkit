import uuid

from flask import Flask
from werkzeug.utils import find_modules, import_string

from proj.models import db
from proj.worker import celery


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('proj.config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # replace secret key from config with random value
    secret_key = app.config.get('SECRET_KEY', None)
    app.config['SECRET_KEY'] = uuid.uuid4().hex if secret_key is None else secret_key

    # init celery
    celery.init_app(app)

    # init database
    db.init_app(app)

    # register all blueprints
    for name in find_modules('proj.view', recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'view'):
            app.register_blueprint(mod.view)

    return app
