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
            result = json_error(Code.ERROR_GODD_INSERT, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

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
              "user_id,user_nickname, name,status,price,short_desc,descs,address,phone,city_id,create_time,image1,image2,time_stamp) values " \
              "('{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{})".\
            format(info.user_id, info.user_nickname,info.name, 0, info.price, info.short_desc, info.descs, info.address, info.phone, "hebei.xianghe", datetime.datetime.now(), info.image1, info.image2, time_stamp)
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
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        city_id = self.get_argument('city_id', None)
        user_id = self.get_argument('user_id', None)
        user_nickname = self.get_argument('user_nickname', None)
        image1 = self.get_argument('image1', None)
        image2 = self.get_argument('image2', None)

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

        # self.logs(name + " " + price + " " + short_desc + " " + desc + " " + address + " " + phone + " ")

        # if not (name and image1 and image2 and price and short_desc and desc and phone and city_id and user_id):
        #     return None

        return Good(name, image1, image2, image3, status, price, short_desc, descs, address, phone,
                    create_time, city_id, user_id, user_nickname)


class GoodGetList(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('GoodGetList *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        page = int(self.get_argument('page', "1")) - 1
        print("GoodGetList ", page)
        # step = 3
        # startIndex = page * step
        # dbHelper = MysqlHelper()
        # mysql = "select * from msapp_good limit " + str(startIndex) + "," + str(step)
        # print(mysql)
        # result = dbHelper.get_all(mysql)
        # print(result)
        result = json_success("success good get list")
        # self.write(result)
        listkey = "cgl_hb.xianghe"

        data = []

        # [b'id', b'user_id', b'user_nickname', b'city', b'name', b'image1', b'image2', b'status', b'price', b'short_desc', b'descs', b'address', b'phone', b'create_time']

        r = redis.Redis(host='localhost', port=6379, db=0)
        length = r.llen(listkey)

        step = 6
        start = page * step
        end = (page + 1) * step - 1
        total = (length + step - 1) / step

        if start >= length:
            result = {
                'code': -1,
                'desc': "reach max",
                'data': [],
                'page': page,
                'total': total,
            }

            self.write(result)
            self.finish()
            return

        if end >= length:
            end = length - 1

        # r.flushdb()
        print("start = ", start, " , end = ", end, " , curpage = ", page, " total = ", total)
        print(r.lrange(listkey, start, end))
        cglist = r.lrange(listkey, start, end)
        for gid in cglist:
            # print(gid)
            good = r.hgetall(gid)
            item = {
                'id': good.get(b'id').decode(),
                'name': good.get(b'name').decode(),
                'user_nickname': good.get(b'user_nickname').decode(),
                'city': good.get(b'city').decode(),
                'image1': good.get(b'image1').decode(),
                'image2': good.get(b'image2').decode(),
                'price': good.get(b'price').decode(),
                'short_desc': good.get(b'short_desc').decode(),
                'address': good.get(b'address').decode(),
                'create_time': good.get(b'create_time').decode(),
                'phone': good.get(b'phone').decode(),
                'time_stamp': good.get(b'time_stamp').decode(),
            }
            data.append(item)
            # print(good.keys())
            # name = good.get(b'name')
            # desc = good.get

        result = {
            'code': 0,
            'desc': "success",
            'data': data,
            'page': page,
            'total': total,
        }

        self.write(result)
        self.finish()


class GoodGet(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('GoodGet *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        id = int(self.get_argument('id', "1"))
        print("GoodGet ", id)

        r = redis.Redis(host='localhost', port=6379, db=0)

        mykey = "cg_hb.xianghe_" + str(id)

        print(r.hgetall(mykey))

        good = r.hgetall(mykey)
        data = {
            'id': good.get(b'id').decode(),
            'name': good.get(b'name').decode(),
            'user_nickname': good.get(b'user_nickname').decode(),
            'city': good.get(b'city').decode(),
            'image1': good.get(b'image1').decode(),
            'image2': good.get(b'image2').decode(),
            'price': good.get(b'price').decode(),
            'short_desc': good.get(b'short_desc').decode(),
            'descs': good.get(b'descs').decode(),
            'address': good.get(b'address').decode(),
            'create_time': good.get(b'create_time').decode(),
            'phone': good.get(b'phone').decode(),
            'time_stamp': good.get(b'time_stamp').decode(),
        }

        result = {
            'code': 0,
            'desc': "success",
            'data': data,
        }

        self.write(result)
        self.finish()
