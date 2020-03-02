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


class AuthorGet(tornado.web.RequestHandler):

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
        id = self.get_argument('id', "-1")
        print("AuthorGet ", id)

        r = redis.Redis(host='localhost', port=6379, db=0)

        mykey = "a_" + str(id)
        author = r.hgetall(mykey)

        if not author:
            self.logs("response_error_para error!")
            result = json_error(Code.ERROR_PARA, Code.ERROR_PARA_DESC)
            self.write(result)
            self.finish()
            return

        print("-----------1----")
        print(author)
        print("-----------2----")

        data = {
            'id': author.get(b'id').decode(),
            'nickname': author.get(b'nickname').decode(),
            'point': author.get(b'point').decode(),
            'status': author.get(b'status').decode(),
            'town': author.get(b'town').decode(),
            'address': author.get(b'address').decode(),
            'phone': author.get(b'phone').decode(),
        }

        result = {
            'code': 0,
            'desc': "success",
            'data': data,
        }

        self.write(result)
        self.finish()
