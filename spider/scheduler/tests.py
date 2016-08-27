import project
from spider.scheduler.tasks import scheduling
from utils.constants import ProcessType

url = 'http://www.pingwest.com/'
r = scheduling.delay({
    'proj_id': 'test',
    'links': [url],
    'options': {
        'rules': {'title': 'title'},
        'process_type': ProcessType.CSS_SELECT,
    },
})
print(r)
