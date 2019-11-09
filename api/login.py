# coding:utf8
import tornado.web
import tornado.gen
import logging
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPClient

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class LoginHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self._future = None
        print('LoginHandler *******************get*0***')
        self._handle_request()
        # self.write(u"yes")
        # print('LoginHandler *******************get*1***')
        # self.finish()

    def post(self):
        self._future = None
        self._handle_request()

    @gen.coroutine
    def _handle_request(self):
        print("11111111vv")
        code = self.get_argument('code')
        print("22222222a")
        app_id = self.get_argument('app_id')
        print("33333333")
        app_secret = self.get_argument('app_secret')

        print("44444444")
        print('LoginHandler _handle_request code = ', code, app_id, app_secret)

        requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
            APPID=app_id, SECRET=app_secret, JSCODE=code)

        print("5555555")
        print(requestString)
        # http_client = AsyncHTTPClient()
        http_client = HTTPClient()

        print("66666666")

        response = http_client.fetch(requestString)
        print("77777777")
        print("after fetch----------")
        self.write(str(response.body))

        print("8888888")

        # print("6666666")
        # http_client.fetch(requestString, self.on_response)


        # response = yield tornado.gen.Task(http_client.fetch, requestString)
        # print(str(response.body))
        # print("fetch end !!!!!!")

        # self.finish("it worksa")

        # response = self.request.get(requestString)
        # print("7777777")
        # print("respose ", response.body)
        #
        #
        # # raise gen.Return(str(response))
        #
        # print("88888888")
        # self.write(response.body)
        # self.finish()

    @tornado.gen.coroutine
    def on_response(self, response):
        print("on_response b code = ", str(response))
        print("--------------------------------")
        # self.write(response.body)
        # print("finish a : ", response.body)
        self.finish()

    def _parse_response(self, response):
        return response.body

    def _parse_response_wrapper(self, response):
        try:
            result = self._parse_response(response)
            self._future.set_result(result)
        except Exception as exc:
            self._future.set_exception(exc)
