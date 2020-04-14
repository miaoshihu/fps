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
        city = self.get_argument('city', None)
        print("GoodGet ", id)

        r = redis.Redis(host='localhost', port=6379, db=0)

        mykey = "cg_" + city + "_" + str(id)

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
