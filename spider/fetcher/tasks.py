
from config.celery import app
from spider.fetcher.services import FetcherService
from spider.processor.tasks import process


@app.task(routing_key='fetcher')
def test_fetcher():
    print('test_fetcher')
    return 'test_fetcher'


@app.task(routing_key='fetcher')
def fetch(task):
    resp = FetcherService.fetch(task=task)
    process.delay(resp)
