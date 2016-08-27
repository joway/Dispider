""" 抓取器
从抓取urls
"""
import requests

from utils.constants import HTTPMethod


class FetcherService(object):
    @classmethod
    def packing_task(cls, task, request):
        return {
            'proj_id': task['proj_id'],
            'task_id': task['task_id'],
            'url': task['url'],
            'rules': task['rules'],
            'valid_link_regex': task['valid_link_regex'],
            'process_type': task['process_type'],
            'content': request.text,
            'encoding': request.encoding,
            'status_code': request.status_code,
        }

    @classmethod
    def fetch(cls, task):
        if task['method'] == HTTPMethod.GET:
            return cls.fetch_get(task)
        elif task['method'] == HTTPMethod.POST:
            return cls.fetch_post(task)

    @classmethod
    def fetch_get(cls, task):
        req = requests.get(task['url'], params=task['payload'], headers=task['headers'])
        return cls.packing_task(task, req)

    @classmethod
    def fetch_post(cls, task):
        req = requests.post(task['url'], data=task['payload'], headers=task['headers'])
        return cls.packing_task(task, req)
