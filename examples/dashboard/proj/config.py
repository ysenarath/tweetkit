SECRET_KEY = None

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_RESULT_BACKEND = 'rpc://'
CELERY_BROKER_URL = 'amqp://'
