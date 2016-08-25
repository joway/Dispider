from config.celery import app
from spider.pipeline.services import PipelineService


@app.task(routing_key='pipeline')
def pipeline(result):
    print('test pipeline')
    PipelineService.pipeline(result)
    return 'test pipeline'
