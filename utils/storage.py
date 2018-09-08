#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:04:43 2018

@author: jianghao
"""

import os
import constanst
import errno
import hashlib


class file_storage:
    def __init__(self):
        pass

    def get(self, url):

        file_path = self.get_file_path(url)

        if os.path.exists(file_path):
            fileObejct = open(file_path, 'r')
            content = fileObejct.read()
        else:
            content = ''
        print "read:" + file_path
        return content

    def exist_file(self, url):
        file_path = self.get_file_path(url)

        if os.path.exists(file_path):
            return True
        return False

    def save(self, url, content, not_force=True):

        file_path = self.get_file_path(url)

        if os.path.exists(file_path) and not_force:
            return 1
        print "[文件保存了]"
        dir_path = self.get_download_file_dir(url)
        #
        if not os.path.isdir(dir_path):
            try:
                os.makedirs(dir_path)
            # Python >2.5 (except OSError, exc: for Python <2.5)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(dir_path):
                    pass
                else:
                    raise
        print file_path
        fileObejct = open(file_path, 'wb')

        fileObejct.write(content)

        pass

    def get_download_file_dir(self, url):
        relactive_path = self.get_relactive_path(url)
        dir_path = constanst.DOWNLOAD_PATH + relactive_path
        return dir_path

    def get_hash_directory(self, hash_string, deep):
        i = 0
        sublen = 2
        path = ''
        while i < deep:
            path += hash_string[i * 2:i * 2 + sublen] + '/'
            i += 1

        return path

    def get_url_hash_string(self, url):
        return hashlib.md5(url.encode("utf-8")).hexdigest()

    def get_relactive_path(self, url):
        hash_string = self.get_url_hash_string(url)

        relactive_path = self.get_hash_directory(
            hash_string, constanst.HASH_PATH_DEEP)

        return relactive_path

    def get_file_path(self, url):
        dir_path = self.get_download_file_dir(url)

        hash_string = self.get_url_hash_string(url)

        file_path = dir_path + hash_string

        return file_path
