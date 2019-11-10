# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
import time
from mysql_helper import MysqlHelper
from bean.data import Good, Need, City, User, GoodSubmitRequest

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
        request_info = self.get_request_info()
        self.logs("request_info =  " + request_info.__str__())

        # step2: 参数不合法，返回错误
        if not request_info:
            self.logs("response_error_para error!")
            # result = self.response_error_para()
            self.write("error para")
            self.finish()
            return

        # step3: 检查是否已有此用户
        has_user = self.is_user_exit(request_info, dbHelper)

        # step4: 储存用户到数据库
        result = self.insert_user_and_good(request_info, has_user)

        if not result:
            self.write("error")
            self.finish()
            return

        self.write("finish")
        self.finish()

    def insert_user_and_good(self, request_info, has_user):
        pass

    def is_user_exit(self, request_info, dbHelper):
        user = request_info.user
        result = dbHelper.get_all("select * from msapp_user where id = %s" % user.id)
        self.logs("result = {} " % result)

    def get_request_info(self):
        good = self.get_good_info()
        user = self.get_user_info()
        if not good:
            return None
        if not user:
            return None
        request_info = GoodSubmitRequest(good, user)
        return request_info

    def get_good_info(self):
        name = self.get_argument('name', None)
        image1 = self.get_argument('image1', None)
        image2 = self.get_argument('image2', None)
        image3 = self.get_argument('image3', None)

        status = 1
        price = self.get_argument('price', None)
        short_desc = self.get_argument('short_desc', None)
        desc = self.get_argument('desc', None)
        address = self.get_argument('address', None)
        phone = self.get_argument('phone', None)
        view_times = 0
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        city_id = self.get_argument('city_id', None)
        user_id = self.get_argument('user_id', None)

        self.logs(name)
        self.logs(price)
        self.logs(short_desc)
        self.logs(desc)
        self.logs(address)
        self.logs(phone)

        # self.logs(name + " " + price + " " + short_desc + " " + desc + " " + address + " " + phone + " ")

        if not (name and image1 and image2 and price and short_desc and desc and phone and city_id and user_id):
            return None

        return Good(name, image1, image2, image3, status, price, short_desc, desc, address, phone, view_times,
                    create_time, last_modify_time, city_id, user_id)

    def get_user_info(self):
        id = self.get_argument("user_id", None)
        user = User(id)
        return user


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
