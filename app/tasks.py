from time import sleep

from app.celerys import app
#app = Celery('tasks', backend='rpc://', broker='amqp://guest:guest@rabbitmq:5672')


@app.task
def seler():
    print('robie cos.')
    sleep(1)
    print('robie cos..')
    sleep(1)
    print('robie cos...')
    sleep(1)
    print('robie cos....')
    sleep(1)
    return 'koniec'
