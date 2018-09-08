#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""
Created on Fir Spe 7 17:02:00 2018

@author: jianghao
"""

'''
each
'''
from bs4 import BeautifulSoup
import os
from utils import downloader
from utils import storage
from mysql import words


class shanbay:
    url_prefix = ''
    range_number = 0

    def __init__(self, url_prefix, range_number):
        self.url_prefix = url_prefix
        self.range_number = range_number
        pass

    def config(self, config):
        pass

    def crawl(self):

        # self.download_and_save(url)
        self.download_range_page(self.url_prefix, self.range_number)

        pass

    def download_range_page(self, url_prefix, range_number):

        for i in range(0, range_number):
            url = url_prefix + str(i)
            self.download_and_save(url)

    def download_and_save(self, url):
        _downloader = downloader.downloader()
        _file_storage = storage.file_storage()

        if not _file_storage.exist_file(url):

            content = _downloader.selimun_downloader(
                url)
            _file_storage.save(url, content)

    def get_download_file_content(self, url):
        _downloader = downloader.downloader()
        _file_storage = storage.file_storage()
        if not _file_storage.exist_file(url):
            print u"文件不存在!"
            self.download_and_save(url)

        content = _downloader.get(url)

        self.extract_words_page(content)

    def extract(self):

        _file_storage = storage.file_storage()

        for i in range(0, self.range_number):
            url = self.url_prefix + str(i)
            html = _file_storage.get(url)

            self.extract_words_page(html)
        pass

    def extract_words_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        trs = soup.select(
            'table[class="table table-bordered table-striped"] > tbody > tr')
        _list = []
        for idx, tr in enumerate(trs):
            tr_soup = BeautifulSoup(str(tr), 'html.parser')
            tds = tr_soup.select('td')
            word = tds[0].getText()
            word_description = tds[1].getText()

            item = {'word': word.strip(
            ), 'word_description': word_description.strip()}
            _list.append(item)

        # insert to mysql database
        wordOrm = words.WordOrm()

        wordOrm.addList(_list, 0)
        pass

    def run(self):
        self.crawl()
        self.extract()
        pass
