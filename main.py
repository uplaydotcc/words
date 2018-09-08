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
    #url = "https://www.shanbay.com/wordlist/34/63685/?page="
    #url = "https://www.shanbay.com/wordlist/34/63688/?page=" --download
    #url = "https://www.shanbay.com/wordlist/34/63691/?page="
    #url = "https://www.shanbay.com/wordlist/34/63694/?page="
    #url = "https://www.shanbay.com/wordlist/34/63697/?page="
    #url = "https://www.shanbay.com/wordlist/34/63700/?page="
    #url = "https://www.shanbay.com/wordlist/34/63703/?page="
    #url = "https://www.shanbay.com/wordlist/34/63706/?page="
    #url = "https://www.shanbay.com/wordlist/34/63709/?page="
    #url = "https://www.shanbay.com/wordlist/34/63712/?page="
    #url = "https://www.shanbay.com/wordlist/34/63715/?page="
    #url = "https://www.shanbay.com/wordlist/34/63718/?page="
    #url = "https://www.shanbay.com/wordlist/34/63721/?page="
    #url = "https://www.shanbay.com/wordlist/34/63724/?page="
    #url = "https://www.shanbay.com/wordlist/34/63727/?page="
    #url = "https://www.shanbay.com/wordlist/34/63730/?page="
    #url = "https://www.shanbay.com/wordlist/34/63733/?page="
    #url = "https://www.shanbay.com/wordlist/34/63736/?page="
    # url = "https://www.shanbay.com/wordlist/34/63739/?page="??
    #url = "https://www.shanbay.com/wordlist/34/63742/?page="
    #url = "https://www.shanbay.com/wordlist/34/63745/?page="
    #url = "https://www.shanbay.com/wordlist/34/63748/?page="
    #url = "https://www.shanbay.com/wordlist/34/63751/?page="
    #url = "https://www.shanbay.com/wordlist/34/63754/?page="
    #url = "https://www.shanbay.com/wordlist/34/63757/?page="
    #url = "https://www.shanbay.com/wordlist/34/63760/?page="
    #url = "https://www.shanbay.com/wordlist/34/63763/?page="
    #url = "https://www.shanbay.com/wordlist/34/63766/?page="
    url = "https://www.shanbay.com/wordlist/34/108313/?page="
    _shanbay = shanbay.shanbay(url, 11)
    _shanbay.run()
