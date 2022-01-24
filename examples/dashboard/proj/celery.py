from proj.app import create_app
from proj.worker import celery as app

__all__ = [
    'app',
]

_ = create_app()
