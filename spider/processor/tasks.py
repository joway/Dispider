from config.celery import app
from spider.pipeline.tasks import pipeline
from spider.processor.services import ProcessorService


@app.task(routing_key='processor')
def process(task):
    result = ProcessorService.process(task)
    # 存储任务
    pipeline.delay(result)
