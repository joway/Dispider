from spider.scheduler.tasks import scheduling_task
from task.constants import TaskStatus
from task.models import Task


class TaskService(object):
    @classmethod
    def create_task(cls, project, url):
        return Task.objects.create(proj=project, url=url)

    @classmethod
    def start_task(cls, task):
        proj = task.proj
        sent_task = {
            'proj_id': proj.id,
            'task_id': task.id,
            'url': task.url,
            'rules': proj.rules,
            'payload': proj.payload,
            'process_type': proj.process_type,
            'method': proj.http_method,
            'headers': proj.headers,
            'cookies': proj.cookies
        }
        scheduling_task.delay(sent_task)
        task.status = TaskStatus.RUNNING
        task.save()
        return sent_task
