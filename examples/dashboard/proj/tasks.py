from proj.worker import celery


@celery.task
def info():
    return 'Hello, World!'
