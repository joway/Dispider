""" 抓取器
从抓取urls
"""
import requests

from utils.constants import HTTPMethod, ProcessType


class FetcherService(object):
    method = HTTPMethod.GET
    headers = {}
    cookies = {}
    timeout = 120
    connect_timeout = 20

    @classmethod
    def init_task(cls, task):
        return {
            'proj_id': task.get('proj_id'),
            'task_id': task.get('task_id'),
            'url': task.get('url'),
            'payload': task.get('payload', {}),
            'rules': task.get('rules', {}),
            'process_type': task.get('process_type', ProcessType.CSS_SELECT),
            'method': task.get('method', cls.method),
            'headers': task.get('headers', cls.headers),
            'cookies': task.get('cookies', cls.method),
            'timeout': task.get('timeout', cls.timeout),
            'connect_timeout': task.get('connect_timeout', cls.connect_timeout),
        }

    @classmethod
    def packed_task(cls, task, request):
        return {
            'proj_id': task['proj_id'],
            'task_id': task['task_id'],
            'url': task['url'],
            'rules': task['rules'],
            'process_type': task['process_type'],
            'content': request.text,
            'encoding': request.encoding,
            'status_code': request.status_code,
        }

    @classmethod
    def fetch(cls, task):
        task = cls.init_task(task)
        if task['method'] == HTTPMethod.GET:
            return cls.fetch_get(task)
        elif task['method'] == HTTPMethod.POST:
            return cls.fetch_post(task)

    @classmethod
    def fetch_get(cls, task):
        req = requests.get(task['url'], params=task['payload'], headers=task['headers'])
        return cls.packed_task(task, req)

    @classmethod
    def fetch_post(cls, task):
        req = requests.post(task['url'], data=task['payload'], headers=task['headers'])
        return cls.packed_task(task, req)
