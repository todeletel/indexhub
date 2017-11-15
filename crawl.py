#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘trace_tristan@126.com‘
@license: Apache Licence 
@file: crawl
@time: 14/11/17 下午4:06
"""
import requests
import logging
from page import Page


class Crawl(object):
    def __init__(self, urls_map):
        self._urls_map = urls_map

    def crawl(self):
        pages = []
        for name, url in self._urls_map.items():
            response = requests.get(url)
            pages.append(Page(name, url, response))
        return pages

    @classmethod
    def crawler(cls, name, url):
        response = requests.get(url)
        if response.status_code != 200:
            logging.error("Page is not crawler success:{}".format(url))
            return None
        return Page(name, url, response)
