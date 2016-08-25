from spider.fetcher.tasks import fetch
task = {
    'url': 'http://www.pingwest.com/',
    'task_id': 1,
    'rules': {
        'test': 'div[class=container]'
    },
    'process_type': 'css_select'
}
res = fetch.delay(task)
res.wait()
print(res)

# req = requests.get(task['url'])
# soup = BeautifulSoup(req.content, 'lxml')
# print(soup.select('h2[class=title]').pop().get_text())
