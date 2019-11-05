# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
from tornado.httpclient import AsyncHTTPClient
from tornado import gen
import os
import time
from mysql_helper import MysqlHelper
from string import Template
import datetime

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')

class NeedSubmit(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('IndexHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ SubmitGoodHandler 1")
        # str = "good man"
        dbHelper = MysqlHelper()
        result = dbHelper.get_all("select * from msapp_good")
        print(result)

        # self.request
        userid = self.get_query_argument('userid', 'null')
        name = self.get_query_argument('name', True)
        image1 = self.get_query_argument('image1', True)
        image2 = self.get_query_argument('image2', True)
        image3 = self.get_query_argument('image3', True)
        type = self.get_query_argument('type', 0)

        userid = 1
        name = '苹果手机'
        image1 = 'www.baidu.com1'
        image2 = 'www.sina.com1'
        image3 = 'www.163.com1'
        type = 0

        status = 1  # 待审核
        price = self.get_query_argument('price', 0)

        short_desc = self.get_query_argument('short_desc', '')
        desc = self.get_query_argument('short_desc', '')
        view_times = self.get_query_argument('view_times', 0) + 1

        price = 10
        short_desc = '苹果货就是牛逼'
        desc = '好奇，好骑'
        view_times = 11

        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        create_time = datetime.datetime.now()
        last_modify_time = datetime.datetime.now()


        sql = "insert into msapp_good(user_id,name,status,type,price,view_times, create_time, last_modify_time) values ({},'{}',{},{},{},{}, '{}', '{}')".format(userid, name, status, type, price, view_times, str(create_time), str(last_modify_time))

        result2 = dbHelper.insert(sql)

        print(sql)
        print("------------------------%s"%result2)
        content = json.dumps({
            'userid': userid,
            'name': name,
            'image1': image1,
            'image2': image2,
            'image3': image3,
            'status': status,
            'price': price,
            'short_desc': short_desc,
            'desc': desc,
            'view_times': view_times,
        })

        self.write(content)
        self.finish()


class NeedGetListHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('GoodGetListHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        # str = "good man"
        dbHelper = MysqlHelper()
        result = dbHelper.get_all("select * from msapp_good")
        print(result)

        # self.request
        userid = self.get_query_argument('userid', 'null')
        name = self.get_query_argument('name', True)
        image1 = self.get_query_argument('image1', True)
        image2 = self.get_query_argument('image2', True)
        image3 = self.get_query_argument('image3', True)
        type = self.get_query_argument('type', 0)

        userid = 1
        name = '苹果手机'
        image1 = 'www.baidu.com1'
        image2 = 'www.sina.com1'
        image3 = 'www.163.com1'
        type = 0

        status = 1  # 待审核
        price = self.get_query_argument('price', 0)

        short_desc = self.get_query_argument('short_desc', '')
        desc = self.get_query_argument('short_desc', '')
        view_times = self.get_query_argument('view_times', 0) + 1

        price = 10
        short_desc = '苹果货就是牛逼'
        desc = '好奇，好骑'
        view_times = 11

        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        create_time = datetime.datetime.now()
        last_modify_time = datetime.datetime.now()


        sql = "insert into msapp_good(user_id,name,status,type,price,view_times, create_time, last_modify_time) values ({},'{}',{},{},{},{}, '{}', '{}')".format(userid, name, status, type, price, view_times, str(create_time), str(last_modify_time))

        result2 = dbHelper.insert(sql)

        print(sql)
        print("------------------------%s"%result2)
        content = json.dumps({
            'userid': userid,
            'name': name,
            'image1': image1,
            'image2': image2,
            'image3': image3,
            'status': status,
            'price': price,
            'short_desc': short_desc,
            'desc': desc,
            'view_times': view_times,
        })

        self.write(content)
        self.finish()