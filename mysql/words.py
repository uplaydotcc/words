#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:04:43 2018

@author: jianghao
"""
from sqlalchemy import Column, String, BigInteger, Integer, SmallInteger, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import and_

import constanst
s = URL(drivername='mysql+pymysql', username=constanst.MYSQL_USER,
        password=constanst.MYSQL_PASS, host=constanst.MYSQL_HOST, port=constanst.MYSQL_PORT, database=constanst.MYSQL_DB, query={"charset": constanst.MYSQL_CHARSET})
# engine = create_engine('mysql+pymysql://root:1qazXSW@@localhost:3306/spider_db?charset=utf8')
engine = create_engine(s)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
Base = declarative_base()


class Word(Base):
    # 表的名字:
    __tablename__ = 'word'

    # 表的结构:
    word_id = Column(Integer, primary_key=True, autoincrement=True)

    word = Column(String)

    phonetic_symbol_en = Column(String, nullable=True)

    phonetic_symbol_us = Column(String, nullable=True)

    word_description = Column(String, nullable=True)


class TagRelation(Base):
    # 表的名字:
    __tablename__ = 'tag_relation'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # 表的结构:
    tag_id = Column(Integer)

    type = Column(Integer)

    entity_id = Column(Integer)


class WordOrm:

    session = None

    def __init__(self):
        self.session = DBSession()

    def addList(self, _list, tag_id):

        for data in _list:

            word = Word(**data)

            self.add(word, tag_id)

    def findByWord(self, word):
        _word = self.session.query(Word).filter_by(word=word).first()
        return _word

    def add(self, Word, tag_id):

        _w = self.findByWord(Word.word)

        if _w:
            # if exists word just return False
            return False

        self.session.add(Word)

        self.session.flush()

        last_insert_id = Word.word_id

        print "insert id:" + str(last_insert_id)
        data = {}
        data['tag_id'] = tag_id
        data['type'] = 1
        data['entity_id'] = last_insert_id

        # print data
        tagRelation = TagRelation(**data)

        self.session.add(tagRelation)

        # 提交即保存到数据库:
        self.session.commit()

    def __del__(self):
        self.session.close()
