# coding:utf8
import tornado.web
import tornado.gen
import logging
from tornado import gen

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class WechatLoginHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        self._future = None
        print('WechatLoginHandler *******************get*0***')
        # self._handle_request()
        self.write(u"yes")
        print('WechatLoginHandler *******************get*1***')
        self.finish()

    def post(self):
        self._future = None
        self._handle_request()

    @gen.coroutine
    def _handle_request(self):
        print("11111111")
        code = self.get_query_argument('code', True)
        print("22222222")
        app_id = self.get_query_argument('app_id', True)
        print("33333333")
        app_secret = self.get_query_argument('app_secret', True)

        print('WechatLoginHandler _handle_request code = ', code, app_id, app_secret)

        # requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
        #     APPID=app_id, SECRET=app_secret, JSCODE=code)
        #
        # print('request url ', requestString)
        # http_client = AsyncHTTPClient()
        # response = yield http_client.fetch(requestString, method='GET')
        # print("respose ", response.body)
        # raise gen.Return(str(response))

        self.write("jiayou")
        self.finish()

    def _parse_response(self, response):
        return response.body

    def _parse_response_wrapper(self, response):
        try:
            result = self._parse_response(response)
            self._future.set_result(result)
        except Exception as exc:
            self._future.set_exception(exc)
