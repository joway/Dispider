from spider.fetcher.tasks import fetch
from utils.helpers import url_hash

url = 'http://www.pingwest.com/'
r = fetch.delay({
    'proj_id': 1,
    'task_id': url_hash(url),
    'url': url,
    'options': {
        'rules': {'title': 'title'},
    },
})
r.wait()
print(r)