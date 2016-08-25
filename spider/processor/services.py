import json
from lxml import etree

from bs4 import BeautifulSoup
from spider.scheduler.tasks import scheduling_append

from spider.pipeline.tasks import pipeline
from utils.constants import ProcessType


class ProcessorService(object):
    def __init__(self):
        pass

    @classmethod
    def process(cls, response):
        process_type = response['process_type']
        if process_type == ProcessType.XPATH:
            handler = cls.process_xpath
        elif process_type == ProcessType.CSS_SELECT:
            handler = cls.process_css_select
        else:
            raise Exception

        mapping = handler(response['content'], response['rules'])
        result = cls.prepare_result(response['proj_id'], response['task_id'], mapping)

        # 存储任务
        pipeline.delay(result)

        # 通知 scheduler 进行后续链接爬取
        scheduling_append.delay(
            result['proj_id'], result['mapping']['inter_links'])

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
        return {
            'proj_id': proj_id,
            'task_id': task_id,
            'mapping': mapping,
        }
