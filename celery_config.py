from celery import Celery

app = Celery('celery_config', broker='redis://localhost:6379/0',backend='redis://localhost', include=['celery_blog','tasks', 'hello'])

# celery -A celery_config worker --loglevel=INFO