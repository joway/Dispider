from task.constants import TaskStatus
from task.models import Task


class TaskService(object):
    @classmethod
    def create_task(cls, project, url):
        return Task.objects.create(proj=project, url=url)

    @classmethod
    def start_task(cls, task):
        task.status = TaskStatus.RUNNING
        task.save()
        return
