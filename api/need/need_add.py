# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
import time
from utils.status_code import Code
from mysql_helper import MysqlHelper
from utils.response import json_error
from utils.response import json_success
from bean.data import Need

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class NeedSubmit(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self.logs("get")
        self._handle_request()

    def post(self):
        self.logs("post")
        self._handle_request()

    def logs(self, text):
        print("NeedSubmit %s" % text)

    def is_valid_para(self):
        result = True
        self.logs("is_valid_para %b " % result)
        return result

    def response_error_para(self):
        return "error"

    def _handle_request(self):

        self.logs("_handle_request")
        # str = "good man"
        dbHelper = MysqlHelper()

        # step1: 获取参数值
        need_info = self.get_need_info()

        # step2: 参数不合法，返回错误
        if not need_info:
            self.logs("response_error_para error!")
            result = json_error(Code.ERROR_PARA, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        # step3: 储存用户到数据库
        result = self.insert_need(dbHelper, need_info)

        if not result:
            result = json_error(Code.ERROR_GODD_INSERT, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        result = json_success("success");
        self.write(result)
        self.finish()

    def insert_need(self, dbHelper, info):
        """
            +------------------+------------------+------+-----+---------+----------------+
            | Field            | Type             | Null | Key | Default | Extra          |
            +------------------+------------------+------+-----+---------+----------------+
            | id               | int(11)          | NO   | PRI | NULL    | auto_increment |
            | user_id          | varchar(50)      | NO   |     | NULL    |                |
            | user_nickname    | varchar(20)      | YES  |     | NULL    |                |
            | name             | varchar(10)      | NO   |     | NULL    |                |
            | image1           | varchar(200)     | YES  |     | NULL    |                |
            | image2           | varchar(200)     | YES  |     | NULL    |                |
            | image3           | varchar(200)     | YES  |     | NULL    |                |
            | status           | int(11)          | NO   |     | NULL    |                |
            | price            | int(10) unsigned | NO   |     | NULL    |                |
            | short_desc       | varchar(20)      | YES  |     | NULL    |                |
            | descs            | longtext         | YES  |     | NULL    |                |
            | address          | varchar(20)      | YES  |     | NULL    |                |
            | phone            | int(10) unsigned | NO   |     | NULL    |                |
            | view_times       | int(10) unsigned | NO   |     | NULL    |                |
            | create_time      | datetime(6)      | YES  |     | NULL    |                |
            | last_modify_time | datetime(6)      | YES  |     | NULL    |                |
            | city_id          | varchar(20)      | NO   | MUL | NULL    |                |
            +------------------+------------------+------+-----+---------+----------------+
            17 rows in set (0.03 sec)
        """

        sql = "insert into msapp_need(" \
              "user_id,user_nickname, name,status,price,descs,address,phone,city_id) values " \
              "('{}','{}','{}',{},{},'{}','{}','{}','{}')".\
            format(info.user_id, info.user_nickname, info.name, 1, info.price, info.descs, info.address, info.phone, "hb_xianghe")
        self.logs("------------------")
        self.logs(sql)

        result2 = dbHelper.insert(sql)
        return result2

    def get_need_info(self):
        name = self.get_argument('name', None)

        price = self.get_argument('price', None)
        descs = self.get_argument('desc', None)
        address = self.get_argument('address', None)
        phone = self.get_argument('phone', None)
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        city_id = self.get_argument('city_id', None)
        user_id = self.get_argument('user_id', None)
        user_nickname = self.get_argument('user_nickname', None)

        self.logs(name)
        self.logs(price)
        self.logs(descs)
        self.logs(address)
        self.logs(phone)
        self.logs(create_time)
        self.logs(city_id)
        self.logs(user_id)

        # self.logs(name + " " + price + " " + short_desc + " " + desc + " " + address + " " + phone + " ")

        # if not (name and image1 and image2 and price and short_desc and desc and phone and city_id and user_id):
        #     return None

        return Need(name, price, descs, address, phone, create_time, city_id, user_id, user_nickname)
