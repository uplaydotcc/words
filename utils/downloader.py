#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 17:04:43 2018

@author: jianghao
"""
__version__ = "0.1.0"


from selenium import webdriver
import time


class downloader:

    charset = 'utf8'

    content_type = 'utf8'

    def __init__(self):

        # content_type = 'utf8'

        # charset = ''
        # if content_type != "":
        #    charset = 'utf8'
        # else:
        #    charset = 'utf8'

        pass

    def charset_watch(self, charset):
        return {
            'utf8': 'utf8',
            'utf-8': 'utf8',
            'UTF-8': 'utf8',
            'gbk': 'gbk',
            'GBK': 'gbk',
            'gb2312': 'gb2312',
            'GB2312': 'gb2312'
        }.get(charset, 'utf8')

    def convert_charset(self, content, charset, target_charset):

        content = content.decode(charset, 'ignore').encode(target_charset)
        return content

    def classic_downloader(self, url):

        pass

    def selimun_downloader(self, url):

        browser = webdriver.Chrome()

        browser.get(url)

        content = browser.page_source

        # time.sleep(1.5)  # 休眠1秒
        browser.close()
        browser.quit()

        charset = self.charset_watch(self.charset)

        if charset != 'utf8':
            self.convert_charset(content, charset, self.charset)

        return content
