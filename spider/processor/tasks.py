from config.celery import app
from spider.processor.services import ProcessorService


@app.task(routing_key='processor')
def test_processor():
    print('test_processor')
    return 'test_processor'


@app.task(routing_key='processor')
def process(response):
    return ProcessorService.process(response)
