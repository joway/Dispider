from django.db import models

# Create your models here.
from project.models import Project
from task.constants import TASK_STATUS_CHOICES, TaskStatus


class Task(models.Model):
    proj = models.ForeignKey(Project, verbose_name='归属项目')
    task_id = models.AutoField('任务ID', primary_key=True)
    url = models.URLField('爬取链接')
    status = models.IntegerField(choices=TASK_STATUS_CHOICES, default=TaskStatus.WAIT_FOR_START)

    created_at = models.DateTimeField(auto_now_add=True)
