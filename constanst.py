#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:17:28 2017

@author: jianghao
"""


class _constant:

    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASS = "1qazXSW@"
    MYSQL_DB = "spider_db"

    MYSQL_CHARSET = "utf8"

    MAIN_HOST = "spider_db"

    DOWNLOAD_PATH = '/Users/jianghao/workspace/python/words/download/'

    HASH_PATH_DEEP = 4

    class ConstantsError(TypeError):
        pass

    def __setattr__(self, key, value):

        if self.__dict__.has_key(key):
            raise self.ConstantsError, "constant reassignment error!"
        self.__dict__[key] = value


import sys
sys.modules[__name__] = _constant()
