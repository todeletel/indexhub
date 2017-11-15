#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘trace_tristan@126.com‘
@license: Apache Licence 
@file: commit_monitor
@time: 14/11/17 下午6:46
"""
from datetime import date
from bs4 import BeautifulSoup
from crawl import Crawl
from utils import email_util
from _local_settings import SMTP_SETTING
git_homepage = 'https://github.com/Sengege'


def send_warning():
    content = u'<h1>今天的commit 为0,请提交代码'
    email_util.send_email(SMTP_SETTING['mail_report_receivers'],
                      SMTP_SETTING['mail_report_ccs'],
                      'git commit monitor warning',
                      html_text=content)


def check_today_commit(homepage):
    page = Crawl.crawler('git', homepage)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(attrs={"data-date": str(date.today())})
    print result
    if int(result['data-count']) == 0:
        send_warning()


if __name__ == '__main__':
    check_today_commit(git_homepage)