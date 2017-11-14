#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘trace_tristan@126.com‘
@license: Apache Licence 
@file: test
@time: 14/11/17 下午4:18
"""
from crawl import Crawl

urls_map = {u'知乎日报': 'https://news-at.zhihu.com/api/4/news/latest'}

if __name__ == '__main__':
    crawler = Crawl(urls_map)
    pages = crawler.crawl()
    for p in pages:
        print p.name, p.url, p.status