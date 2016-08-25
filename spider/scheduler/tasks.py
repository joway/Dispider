from config.celery import app
from spider.scheduler.services import SchedulerService


@app.task(routing_key='scheduler')
def scheduling_proj(proj):
    """ 创建项目
    """
    return SchedulerService.scheduling_proj(proj)


@app.task(routing_key='scheduler')
def scheduling_task(task):
    """ 创建任务
    """
    return SchedulerService.scheduling_task(task)


@app.task(routing_key='scheduler')
def scheduling_append(proj_id, inter_links):
    """ 给project追加任务
    """
    return SchedulerService.scheduling_append(proj_id, inter_links)
