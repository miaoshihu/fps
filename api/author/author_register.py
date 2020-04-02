# coding:utf8
import tornado.web
import tornado.gen
import logging
import time
import redis
from utils.status_code import Code
from mysql_helper import MysqlHelper
from bean.data import Author
from utils.response import json_error
from utils.response import json_success

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class AuthorRegister(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self.logs("get")
        self._handle_request()

    def post(self):
        self.logs("post")
        self._handle_request()

    def logs(self, text):
        print("AuthorSubmit %s" % text)

    def is_valid_para(self):
        result = True
        self.logs("is_valid_para %b " % result)
        return result

    def response_error_para(self):
        return "error"

    def _handle_request(self):

        self.logs("_handle_request")
        # str = "author man"
        dbHelper = MysqlHelper()

        # step1: 获取参数值
        author_info = self.get_author_info()

        # step2: 参数不合法，返回错误
        if not author_info:
            self.logs("response_error_para error!")
            result = json_error(Code.ERROR_PARA, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        # step3: 储存用户到数据库，直接为审核通过状态
        result = self.insert_author(dbHelper, author_info)

        if not result:
            result = json_error(Code.ERROR_GODD_INSERT, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        # step4: 写到redis

        result = json_success("success")
        self.write(result)
        self.finish()

    def insert_author(self, dbHelper, info):
        """
            +-------------+-------------+------+-----+---------+-------+
            | Field       | Type        | Null | Key | Default | Extra |
            +-------------+-------------+------+-----+---------+-------+
            | id          | varchar(50) | NO   | PRI | NULL    |       |
            | nickname    | varchar(20) | NO   |     | NULL    |       |
            | point       | int(11)     | NO   |     | NULL    |       |
            | status      | int(11)     | NO   |     | NULL    |       |
            | descs       | longtext    | YES  |     | NULL    |       |
            | town        | varchar(20) | YES  |     | NULL    |       |
            | address     | varchar(20) | YES  |     | NULL    |       |
            | phone       | varchar(20) | NO   |     | NULL    |       |
            | create_time | datetime(6) | YES  |     | NULL    |       |
            | time_stamp  | bigint(20)  | YES  |     | NULL    |       |
            +-------------+-------------+------+-----+---------+-------+
        """
        sql = "insert into msapp_author(" \
              "id,nickname,point,status,descs,town,address,phone,create_time,time_stamp) values " \
              "('{}','{}',{},{},'{}', '{}','{}','{}','{}',{})".\
            format(info.id, info.nickname, 0, 1, '', info.town, info.address, info.phone, info.create_time, info.time_stamp)
        self.logs("------------------")
        self.logs(sql)

        result2 = dbHelper.insert(sql)
        self.logs(result2)
        return result2

    def get_author_info(self):
        self.logs("get_author_info--------------------------")

        id = self.get_argument('user_id', None)
        nickname = self.get_argument('user_nickname', None)
        town = self.get_argument('town', None)
        address = self.get_argument('address', None)

        phone = self.get_argument('phone', None)
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time_stamp = (int)(time.time())

        self.logs(id)
        self.logs(nickname)
        self.logs(town)
        self.logs(address)
        self.logs(phone)
        self.logs(create_time)
        self.logs(time_stamp)

        return Author(id, nickname, town, address, phone, create_time, time_stamp)
