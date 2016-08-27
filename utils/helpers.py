import hashlib
import re

from lxml import etree

from utils.exceptions import Base62Exception
from utils.redis import redis_client

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


def remove_duplicates_links(links: []):
    return [l for l in links if not redis_client.sismember(url_hash(l))]
