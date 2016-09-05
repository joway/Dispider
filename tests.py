# from spider.scheduler.tasks import scheduling
# from utils.constants import ProcessType
#
# url = 'http://www.pingwest.com/the-us-startup-visa-is-real-and-coming/'
# r = scheduling.delay('pingwest', [url], {
#     'rules': {
#         'title': 'h1[class="title"]',
#         'content': 'div[id="sc-container"]'
#     },
#     'process_type': ProcessType.CSS_SELECT,
# })
# print(r)

# j = r'%s' % '{"title": "h1[class=title]","content": "div[id=sc-container]"}'
# print(
#     j
# )
# print(json.loads(j.replace("\\", r"\\")))
from w3lib.url import canonicalize_url

print(url_normalize('https://github.com/niksite/url-normalize?key=1'))
