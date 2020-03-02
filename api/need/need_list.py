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


class NeedGetList(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('NeedGetList *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        page = int(self.get_argument('page', "1")) - 1
        step = 3
        startIndex = page * step
        dbHelper = MysqlHelper()
        mysql = "select * from msapp_need limit " + str(startIndex) + "," + str(step)
        print(mysql)
        result = dbHelper.get_all(mysql)
        print(result)
        result = json_success("success need get list")
        self.write(result)
        self.finish()
