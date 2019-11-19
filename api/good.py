# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
import time
from utils.status_code import Code
from mysql_helper import MysqlHelper
from bean.data import Good, Need, City, GoodSubmitRequest
from utils.response import json_error

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class GoodSubmit(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self.logs("get")
        self._handle_request()

    def post(self):
        self.logs("post")
        self._handle_request()

    def logs(self, text):
        print("GoodSubmit %s" % text)

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
        good_info = self.get_good_info()

        # step2: 参数不合法，返回错误
        if not good_info:
            self.logs("response_error_para error!")
            result = json_error(Code.ERROR_PARA, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        # step3: 储存用户到数据库
        result = self.insert_good(dbHelper, good_info)

        if not result:
            self.write("error")
            self.finish()
            return

        self.write("finish")
        self.finish()

    def insert_good(self, dbHelper, info):
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

        sql = "insert into msapp_good(" \
              "user_id,user_nickname, name,status,price,short_desc,descs,address,phone,city_id) values " \
              "('{}','{}','{}',{},{},'{}','{}','{}','{}','{}')".\
            format(info.user_id, info.user_nickname,info.name, 1, info.price, info.short_desc, info.descs, info.address, info.phone, "hb_xianghe")
        self.logs("------------------")
        self.logs(sql)

        result2 = dbHelper.insert(sql)
        return result2

    def get_good_info(self):
        name = self.get_argument('name', None)
        image1 = self.get_argument('image1', None)
        image2 = self.get_argument('image2', None)
        image3 = self.get_argument('image3', None)

        status = 1
        price = self.get_argument('price', None)
        short_desc = self.get_argument('short_desc', None)
        descs = self.get_argument('desc', None)
        address = self.get_argument('address', None)
        phone = self.get_argument('phone', None)
        view_times = 0
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        city_id = self.get_argument('city_id', None)
        user_id = self.get_argument('user_id', None)
        user_nickname = self.get_argument('user_nickname', None)
        user_id = "123456a"
        user_nickname = "勇敢的心"

        self.logs(name)
        self.logs(price)
        self.logs(short_desc)
        self.logs(descs)
        self.logs(address)
        self.logs(phone)
        self.logs(create_time)
        self.logs(city_id)
        self.logs(user_id)

        # self.logs(name + " " + price + " " + short_desc + " " + desc + " " + address + " " + phone + " ")

        # if not (name and image1 and image2 and price and short_desc and desc and phone and city_id and user_id):
        #     return None

        return Good(name, image1, image2, image3, status, price, short_desc, descs, address, phone, view_times,
                    create_time, last_modify_time, city_id, user_id, user_nickname)


class GoodGetList(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('GoodGetListHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        # str = "good man"
        pass
