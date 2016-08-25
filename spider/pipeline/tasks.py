from config.celery import app


@app.task(routing_key='pipeline')
def pipeline(result):
    print('test pipeline')
    return 'test pipeline'
