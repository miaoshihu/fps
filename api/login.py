# coding:utf8
import tornado.web
import tornado.gen
import logging
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class LoginHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    @gen.coroutine
    def post(self):
        self._future = None
        # self._handle_request()
        print("post method")

    @gen.coroutine
    def get(self):
        # self._future = None
        code = self.get_argument('code')
        app_id = self.get_argument('app_id')
        app_secret = self.get_argument('app_secret')

        requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
            APPID=app_id, SECRET=app_secret, JSCODE=code)

        print(requestString)
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(requestString)
        self.write(str(response.body))
        self.finish()
