#!/usr/bin/env python2
# -*- coding:utf-8 -*-

"""
Created on Fri Aug 15:21:00 2018
@author: jianghao

"""
import sys
import getopt
import os
from crawler import shanbay

reload(sys)

sys.setdefaultencoding("utf-8")

__version__ = "1.0.0"


def usage():
    print u"Words Crawler: version "+str(__version__)
    print u"Uasage :-h help \n"
    print u"-o operation for job\n"


if __name__ == '__main__':
    append_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(append_dir)

    opts, args = getopt.getopt(sys.argv[1:], "v:o:h")

    operation = ''

    for op, value in opts:
        if op == '-v':
            print u"Words Crawler: version "+str(__version__)
        elif op == '-o':
            operation = value
        elif op == '-h':
            usage()
            sys.exit()

if operation == '':
    print u"-o 参数是必须参数"
    os._exit(1)
elif operation == 'shanbay':
    url = "https://www.shanbay.com/wordlist/34/63685/?page="

    _shanbay = shanbay.shanbay(url, 10)
    _shanbay.run()
