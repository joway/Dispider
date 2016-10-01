#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import pygal
import requests

reCOMM = r'<!--.*?-->'
reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
reTAG = r'<[\s\S]*?>|[ \t\r\f\v]'

# 当前高度 / 最大高度 > BASE_RATE 视作为有效内容
BASE_RATE = 0.3


class Extractor(object):
    def __init__(self, content='', url='', lines_block_size=5):
        self.content = content
        self.url = url
        self.lines_block_size = lines_block_size
        self.ctexts = []
        self.cblocks = []
        self.distribution = []
        self.extracted = ''

        self.init()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.extracted

    def init(self):
        if self.url:
            self.request_url()
        self.normalize()
        self.prepare()
        self.distribute()
        self.modify_extract()

    def normalize(self):
        self.content = re.sub(reCOMM, "", self.content)
        self.content = re.sub(reTRIM.format("script"), "", self.content)
        self.content = re.sub(reTRIM.format("style"), "", self.content)
        self.content = re.sub(reTAG, "", self.content)

    def prepare(self):
        self.ctexts = [x + '\n' for x in self.content.split('\n') if x]
        self.cblocks = [''] * len(self.ctexts)
        for index, line in enumerate(self.ctexts):
            self.cblocks[index] = (
                ''.join([''.join(x.split()) for x in self.ctexts[index:index + self.lines_block_size]]))

    def request_url(self):
        self.content = requests.get(url=self.url).text
        self.normalize()

    def distribute(self):
        self.distribution = [0] * len(self.ctexts)
        lines_size = [len(txt) for txt in self.cblocks]
        for index in range(len(self.ctexts)):
            self.distribution[index] = sum(
                lines_size[index:index + self.lines_block_size])
        return self.distribution

    def extract(self, ctexts, distribution):
        MAX_LEN = max(distribution)
        CONTENT_MID = distribution.index(MAX_LEN)
        content = []
        for i in range(CONTENT_MID, 0, -1):
            if distribution[i] / MAX_LEN > BASE_RATE:
                content.append(ctexts[i])
            else:
                break
        content.reverse()
        for i in range(CONTENT_MID + 1, len(distribution)):
            if distribution[i] / MAX_LEN > BASE_RATE:
                content.append(ctexts[i])
            else:
                break
        return "".join(content)

    def modify_extract(self):
        MID = len(self.distribution) // 2
        PRE_MAX_LEN = max(self.distribution[:MID])
        SUF_MAX_LEN = max(self.distribution[MID:])
        if min(PRE_MAX_LEN, SUF_MAX_LEN) / max(PRE_MAX_LEN, SUF_MAX_LEN) > 0.5:
            # 存在两个峰值
            self.extracted = self.extract(self.ctexts[:MID], self.distribution[:MID]) + \
                             self.extract(self.ctexts[MID:], self.distribution[MID:])
        else:
            self.extracted = self.extract(self.ctexts, self.distribution)


if __name__ == '__main__':

    URLS = [
        'http://blog.rainy.im/2015/09/02/web-content-and-main-image-extractor/',
        # 'https://ruby-china.org/topics/31217',
        # 'https://ruby-china.org/topics/31123',
        # 'http://ent.sina.com.cn/y/2009-11-09/13572762965.shtml',
        # 'http://www.pingwest.com/google-g-suite-wants-to-work/',
        # 'http://news.ifeng.com/a/20160930/50051126_0.shtml',
        # 'https://www.anotherhome.net/2717',
        # 'https://www.anotherhome.net/2648',
    ]
    bar_chart = pygal.Bar()
    for URL in URLS:
        ext = Extractor(url=URL)
        print(ext)
        bar_chart.add(URL[:10], ext.distribution)
    bar_chart.render_in_browser()
