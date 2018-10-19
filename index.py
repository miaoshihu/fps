# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class WechatLoginHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self._future = None
        print('WechatLoginHandler *******************get****')
        self._handle_request()

    def post(self):
        self._future = None
        self._handle_request()

    @gen.coroutine
    def _handle_request(self):
        code = self.get_query_argument('code', True)
        app_id = self.get_query_argument('app_id', True)
        app_secret = self.get_query_argument('app_secret', True)

        print('WechatLoginHandler _handle_request code = ', code, app_id, app_secret)

        requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
            APPID=app_id, SECRET=app_secret, JSCODE=code)

        print('request url ', requestString)
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(requestString, method='GET')
        print("respose ", response.body)
        raise gen.Return(str(response))

    def _parse_response(self, response):
        return response.body

    def _parse_response_wrapper(self, response):
        try:
            result = self._parse_response(response)
            self._future.set_result(result)
        except Exception as exc:
            self._future.set_exception(exc)
