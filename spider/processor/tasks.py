from config.celery import app
from spider.processor.services import ProcessorService


@app.task(routing_key='processor')
def process(task):
    return ProcessorService.process(task)
