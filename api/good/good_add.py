# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
import time
import redis
from utils.status_code import Code
from mysql_helper import MysqlHelper
from bean.data import Good, Need, City, GoodSubmitRequest
from utils.response import json_error
from utils.response import json_success
from api.utils.redis import publish_good
import datetime

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
        good = self.get_good()

        # step2: 参数不合法，返回错误
        if not good:
            self.logs("response_error_para error!")
            result = json_error(Code.ERROR_PARA, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        # step3: 储存用户到数据库
        result = self.insert_good(dbHelper, good)

        if not result:
            result = json_error(Code.ERROR_GODD_INSERT, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        # step4: 写到redis agl
        good_id = self.get_good_id(dbHelper, good)
        good.id = good_id

        publish_good(good, False)

        result = json_success("success")
        self.write(result)
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
        time_stamp = (int)(time.time())

        sql = "insert into msapp_good(" \
              "user_nickname, name,status,price,short_desc,descs,address,phone,city_id,create_time,image1,image2,time_stamp, author_id) values " \
              "('{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{}, {})".\
            format(info.user_nickname,info.name, 0, info.price, info.short_desc, info.descs, info.address, info.phone, "hebei.xianghe", datetime.datetime.now(), info.image1, info.image2, time_stamp, info.author_id)
        self.logs("------------------")
        self.logs(sql)

        result2 = dbHelper.insert(sql)
        return result2

    def get_good(self):
        name = self.get_argument('name', None)
        image1 = self.get_argument('image1', None)
        image2 = self.get_argument('image2', None)
        image3 = self.get_argument('image3', None)

        status = 1
        price = self.get_argument('price', None)
        short_desc = self.get_argument('short_desc', None)
        descs = self.get_argument('descs', None)
        address = self.get_argument('address', None)
        phone = self.get_argument('phone', None)
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        city_id = self.get_argument('city_id', None)
        user_id = self.get_argument('user_id', None)
        user_nickname = self.get_argument('user_nickname', None)
        image1 = self.get_argument('image1', None)
        image2 = self.get_argument('image2', None)
        author_id = self.get_argument('author_id', None)

        self.logs(name)
        self.logs(price)
        self.logs(short_desc)
        self.logs(descs)
        self.logs(address)
        self.logs(phone)
        self.logs(create_time)
        self.logs(city_id)
        self.logs(user_id)
        self.logs("-----------image1 and image2-")
        self.logs(image1)
        self.logs(image2)
        self.logs(author_id)

        # self.logs(name + " " + price + " " + short_desc + " " + desc + " " + address + " " + phone + " ")

        # if not (name and image1 and image2 and price and short_desc and desc and phone and city_id and user_id):
        #     return None

        return Good(name, image1, image2, image3, status, price, short_desc, descs, address, phone,
                    create_time, city_id, user_id, user_nickname, author_id)

    def get_good_id(self, dbHelper, info):
        sql = "select id from msapp_good where author_id ='{}' order by id desc limit 1".format(info.author_id)
        self.logs("------------------")
        self.logs(sql)

        result2 = dbHelper.get_one(sql)

        self.logs(result2)
        return result2[0]
