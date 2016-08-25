from spider.scheduler import SchedulerService


def callback(proj_id, inter_links):
    # get project and check status
    SchedulerService.scheduling_tasks(proj_id, inter_links)
