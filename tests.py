# # from spider.fetcher.tasks import fetch
# # task = {
# #     'url': 'http://www.pingwest.com/',
# #     'task_id': 1,
# #     'rules': {
# #         'test': 'div[class=container]'
# #     },
# #     'process_type': 'css_select'
# # }
# # res = fetch.delay(task)
# # res.wait()
# # print(res)
# #
# # # req = requests.get(task['url'])
# # # soup = BeautifulSoup(req.content, 'lxml')
# # # print(soup.select('h2[class=title]').pop().get_text())
# import re
# from urllib.parse import urlparse
#
from utils.helpers import extract_valid_links

URL = 'http://www.qq.com/'
# url = urlparse(URL)
# # r = re.match(r'^http', )
# print(url)

import requests

req = requests.get(URL)
print(extract_valid_links(req.text, r'^https://qian.qq.com'))
