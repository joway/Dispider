from spider.fetcher.tasks import fetch
from utils.helpers import url_hash, remove_duplicates_links
from utils.redis import redis_client


class SchedulerService(object):
    @classmethod
    def scheduling_tasks(cls, proj_id: str, links: [], options: []):
        tasks = []
        remove_duplicates_links(links)
        for link in links:
            task = options + {
                'proj_id': proj_id,
                'task_id': url_hash(link),
                'url': link}
            tasks.append(task)

            cls.scheduling_task(task)
        return tasks

    @classmethod
    def scheduling_task(cls, task):
        redis_client.sadd(task['proj_id'], task['task_id'])
        fetch.delay(task)
