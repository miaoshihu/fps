# coding:utf8

"""
@ Author Jue
@ Date 2019-11-22 12:51:26

"""


# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
import redis

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class Test(tornado.web.RequestHandler):


    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('Test *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        print("Test _handle_request")

        # print("------------------------%s"%result2)
        # content = json.dumps({
        #     'desc': desc,
        # })

        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set("name", "zhangsan")
        #
        self.write(r.get("name"))
        # self.write("good man")
        self.finish()

