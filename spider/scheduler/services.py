from utils.constants import ProcessType


class SchedulerService(object):
    def __init__(self):
        pass

    @classmethod
    def prepare_task(cls, proj_id, url, options={}):
        return {
            'proj_id': proj_id,
            'task_id': cls.gen_task_id(),
            'url': url,
            'process_type': options.get('process_type', ProcessType.CSS_SELECT),
            'rules': options.get('rules', {'inter_links': 'a[href]'}),
        }

    @classmethod
    def gen_task_id(cls):
        return 'xxx'

    @classmethod
    def scheduling_task(cls):
        pass

    @classmethod
    def scheduling_append(cls, proj_id, inter_links):
        pass

    @classmethod
    def scheduling(cls, task):
        pass

