from django.db import models

# Create your models here.
from .constants import SITE_TYPE_CHOICES


class Website(models.Model):
    name = models.CharField('网站名', max_length=128)
    site_type = models.IntegerField('分类', choices=SITE_TYPE_CHOICES)
    indexed_count = models.IntegerField('索引数')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
