import json
import threading

import requests
from bs4 import BeautifulSoup
from lxml import etree

from config.settings import SCHEDULER_CALLBACK_API
from spider.pipeline.tasks import pipeline
from utils.constants import ProcessType
from utils.exceptions import CallbackException


def callback(proj_id, inter_links, retry=True):
    try:
        req = requests.post(url=SCHEDULER_CALLBACK_API, data={
            'proj_id': proj_id,
            'inter_links': inter_links
        })
        return req.json()
    except Exception:
        if retry:
            return callback(proj_id, inter_links, False)
        else:
            # TODO: 报告回调错误
            raise CallbackException


class ProcessorService(object):
    @classmethod
    def process(cls, task):
        process_type = task['process_type']
        if process_type == ProcessType.XPATH:
            handler = cls.process_xpath
        elif process_type == ProcessType.CSS_SELECT:
            handler = cls.process_css_select
        elif process_type == ProcessType.JSON:
            handler = cls.process_json
        else:
            raise Exception

        mapping = handler(task['content'], task['rules'])

        result = cls.prepare_result(task['proj_id'], task['task_id'], mapping)

        # 存储任务
        pipeline.delay(result)

        # 通知 scheduler 进行后续链接爬取
        cls.scheduler_callback(result['proj_id'], result['mapping']['inter_links'])

        return result

    @classmethod
    def process_css_select(cls, content, rules):
        soup = BeautifulSoup(content, 'lxml')
        mapping = {}
        for rule in rules:
            try:
                mapping[rule] = soup.select(rules[rule])[0].get_text()
            except ValueError:
                mapping[rule] = 'Unsupported or invalid CSS selector: "%s"' % rule
        return mapping

    @classmethod
    def process_xpath(cls, content, rules):
        html = etree.HTML(content)
        mapping = {}
        for rule in rules:
            mapping[rule] = html.xpath(rules[rule])
        return mapping

    @classmethod
    def process_json(cls, content, rules):
        mapping = {}
        json_obj = json.loads(content)
        # TODO : json 选择器
        for rule in rules:
            mapping[rule] = json_obj[rule]
        return mapping

    @classmethod
    def prepare_result(cls, proj_id, task_id, mapping):
        if not mapping.get('inter_links', None):
            mapping['inter_links'] = 'a[href]'

        return {
            'proj_id': proj_id,
            'task_id': task_id,
            'mapping': mapping,
        }

    @classmethod
    def scheduler_callback(cls, proj_id, inter_links):
        t = threading.Thread(target=callback, args=(proj_id, inter_links))
        t.start()
