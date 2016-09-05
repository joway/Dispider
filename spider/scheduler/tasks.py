from config.celery import app
from spider.scheduler.services import SchedulerService


@app.task(routing_key='scheduler')
def scheduling(proj_id: str, links: [], options: []):
    print('log: %s' % str(links))
    SchedulerService.scheduling_tasks(proj_id, links, options)
