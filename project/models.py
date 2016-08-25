from django.db import models

# Create your models here.
from spider.scheduler import PROCESS_TYPE_CHOICES, HTTP_METHOD_CHOICES, PROJECT_STATUS_CHOICES, ProjectStatus
from utils.constants import HTTPMethod, ProcessType


class Project(models.Model):
    id = models.AutoField('项目id', primary_key=True)

    name = models.CharField('项目名', max_length=56)
    status = models.IntegerField(choices=PROJECT_STATUS_CHOICES, default=ProjectStatus.WAIT_FOR_START)
    entry_url = models.URLField('入口链接')
    process_type = models.IntegerField('处理类型', choices=PROCESS_TYPE_CHOICES,
                                       default=ProcessType.CSS_SELECT)
    http_method = models.IntegerField('HTTP方法', choices=HTTP_METHOD_CHOICES,
                                      default=HTTPMethod.GET)

    headers = models.TextField('HTTP Headers', null=True)
    cookies = models.TextField('Cookies', null=True)

    valid_url_regexp = models.CharField('合法链接符合正则', max_length=56, default='')
    rules = models.TextField('内容提取映射规则')

    created_at = models.DateTimeField('创建于', auto_now_add=True)
    last_indexed = models.DateTimeField('上一次索引', auto_now_add=True)
