# Info
# docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
# celery -A tasks worker --loglevel=INFO


from celery import Celery
from celery_config import app

# app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://guest@localhost//')
# app = Celery('tasks', broker='redis://localhost')
# app = Celery('tasks', backend='rpc://', broker='pyamqp://')
# app = Celery('tasks',  broker='pyamqp://guest:guest@localhost') 
# app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://guest:guest@localhost')

@app.task
def add(x, y):
    return x + y

#celery -A tasks worker --loglevel=INFO