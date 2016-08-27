import hashlib
import re
from urllib.parse import urlparse

from lxml import etree

from utils.constants import HTTPMethod, ProcessType
from utils.exceptions import Base62Exception
from utils.redis_client import redis_client

basedigits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
BASE = len(basedigits)


def url_hash(url, length=8):
    return hashlib.md5(url.encode('utf-8')).hexdigest()[:length]


def base62_decode(s: str):
    ret, mult = 0, 1
    for c in reversed(s):
        ret += mult * basedigits.index(c)
        mult *= BASE
    return ret


def base62_encode(num: int):
    if num < 0:
        raise Base62Exception("positive number " + num)
    if num == 0:
        return '0'
    ret = ''
    while num != 0:
        ret = (basedigits[num % BASE]) + ret
        num = int(num / BASE)
    return ret


def extract_valid_links(content, regex):
    html = etree.HTML(content)
    return [a.attrib['href'] for a in html.xpath('//a[@href]')
            if re.match(regex, a.attrib['href'])]


def remove_duplicates_links(proj_id, links: []):
    return [l for l in links if not redis_client.sismember(proj_id, url_hash(l))]


def extract_options_from_task(task):
    return {
        'rules': task['rules'],
        'payload': task['payload'],
        'process_type': task['process_type'],
        'http_method': task['http_method'],
        'headers': task['headers'],
        'cookies': task['cookies']
    }


def init_task_options(task):
    task['http_method'] = task.get('http_method', HTTPMethod.GET)
    task['payload'] = task.get('payload', {})
    task['process_type'] = task.get('process_type', ProcessType.CSS_SELECT)
    task['valid_link_regex'] = task.get('valid_link_regex',
                                        r'^(http://)|(https://)(%s)' % get_hostname(task['url']))
    task['headers'] = task.get('headers', {})
    task['cookies'] = task.get('cookies', {})
    task['is_callback'] = task.get('is_callback', False)
    return task


def get_path(url):
    return urlparse(url).path


def get_hostname(url):
    return urlparse(url).netloc


def get_scheme(url):
    return urlparse(url).scheme
