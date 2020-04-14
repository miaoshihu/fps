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
from api.utils.utils import check_args
from utils.status_code import Code
logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class GoodGetList(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        page = int(self.get_argument('page', "1")) - 1
        city = self.get_argument('city', None)

        paraCheck = check_args(self)

        if not paraCheck:
            print("GoodGetList para check failed!")
            result = {
                'code': Code.ERROR_PARA,
                'desc': "error para",
                'data': [],
                'page': 0,
                'total': 0,
            }

            self.write(result)
            self.finish()
            return

        print("GoodGetList ", page)

        listkey = "cgl_" + city

        data = []

        # [b'id', b'user_id', b'user_nickname', b'city', b'name', b'image1', b'image2', b'status', b'price', b'short_desc', b'descs', b'address', b'phone', b'create_time']

        r = redis.Redis(host='localhost', port=6379, db=0)
        length = r.llen(listkey)

        step = 6
        start = page * step
        end = (page + 1) * step - 1
        total = (length + step - 1) / step

        if start >= length:
            print("GoodGetList ", "start = ", start, " end = ", end, "total = ", total, "length = ", length)
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
            print("&&&&&&&&&&&", good, gid)
            item = {
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

