from utils.helpers import url_hash, clean_links, init_task_options
from utils.redis_client import redis_client


class SchedulerService(object):
    @classmethod
    def scheduling_tasks(cls, proj_id: str, links: [], options: []):
        tasks = []
        clean_links(proj_id, links)
        for link in links:
            task = dict({
                'proj_id': proj_id,
                'task_id': url_hash(link),
                'url': link}, **options)
            task = init_task_options(task)
            tasks.append(task)

            cls.scheduling_task(task)
        return tasks

    @classmethod
    def scheduling_task(cls, task):
        redis_client.sadd(task['proj_id'], task['task_id'])
        from spider.fetcher.tasks import fetch
        fetch.delay(task)
