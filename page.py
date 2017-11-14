#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘trace_tristan@126.com‘
@license: Apache Licence 
@file: page
@time: 14/11/17 下午3:58
"""


class Page(object):
    """
    restore a html format data resource.
    """

    def __init__(self, name, url, response):
        """
        :param response: request a requests obj
        """
        self.url = url
        self.name = name
        self.status = response.status_code
        self.headers = response.headers
        self.content = response.content
