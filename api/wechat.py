# coding:utf8
import tornado.web
import tornado.gen
import logging
import json
from tornado import gen
import os
import time
from mysql_helper import MysqlHelper
import datetime

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class IndexHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'text/html')

    def get(self):
        print('IndexHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        code = self.get_query_argument('code', True)

        patha = os.path.join(os.path.abspath("."), "1_shuxiaosheng.top_bundle.crt")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ path = %s" % patha)

        self.write(patha)
        self.finish()


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


class UploadHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'text/html')

    def get(self):
        print('IndexHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        code = self.get_query_argument('code', True)

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ upload 2")
        # str = "good man"

        # self.request
        file_name = self.get_body_argument('file_name', 'null')
        file_md5 = self.get_body_argument('file_md5', True)
        file_path = self.get_body_argument('file_path', True)
        file_content_type = self.get_body_argument('file_content_type', True)
        file_size = self.get_body_argument('file_size', True)

        content = json.dumps({
            'name': file_name,
            'content_type': file_content_type,
            'md5': file_md5,
            'path': file_path,
            'size': file_size,
            # 'desc': str(self.request),
            # 'args': str(self.request.arguments),
            # 'query_arguments': str(self.request.query_arguments),
            # 'body_arguments': str(self.request.body_arguments),
            # 'files': str(self.request.files),
        })

        self.write(content)
        self.finish()


class GoodSubmitHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('IndexHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ SubmitGoodHandler 1")
        # str = "good man"
        dbHelper = MysqlHelper()
        result = dbHelper.get_all("select * from msapp_good")
        print(result)

        # self.request
        userid = self.get_query_argument('userid', 'null')
        name = self.get_query_argument('name', True)
        image1 = self.get_query_argument('image1', True)
        image2 = self.get_query_argument('image2', True)
        image3 = self.get_query_argument('image3', True)
        type = self.get_query_argument('type', 0)

        userid = 1
        name = '苹果手机'
        image1 = 'www.baidu.com1'
        image2 = 'www.sina.com1'
        image3 = 'www.163.com1'
        type = 0

        status = 1  # 待审核
        price = self.get_query_argument('price', 0)

        short_desc = self.get_query_argument('short_desc', '')
        desc = self.get_query_argument('short_desc', '')
        view_times = self.get_query_argument('view_times', 0) + 1

        price = 10
        short_desc = '苹果货就是牛逼'
        desc = '好奇，好骑'
        view_times = 11

        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        create_time = datetime.datetime.now()
        last_modify_time = datetime.datetime.now()


        sql = "insert into msapp_good(user_id,name,status,type,price,view_times, create_time, last_modify_time) values ({},'{}',{},{},{},{}, '{}', '{}')".format(userid, name, status, type, price, view_times, str(create_time), str(last_modify_time))

        result2 = dbHelper.insert(sql)

        print(sql)
        print("------------------------%s"%result2)
        content = json.dumps({
            'userid': userid,
            'name': name,
            'image1': image1,
            'image2': image2,
            'image3': image3,
            'status': status,
            'price': price,
            'short_desc': short_desc,
            'desc': desc,
            'view_times': view_times,
        })

        self.write(content)
        self.finish()


class GoodGetListHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self):
        print('GoodGetListHandler *******************get****')
        self._handle_request()

    def post(self):
        self._handle_request()

    def _handle_request(self):
        # str = "good man"
        dbHelper = MysqlHelper()
        result = dbHelper.get_all("select * from msapp_good")
        print(result)

        # self.request
        userid = self.get_query_argument('userid', 'null')
        name = self.get_query_argument('name', True)
        image1 = self.get_query_argument('image1', True)
        image2 = self.get_query_argument('image2', True)
        image3 = self.get_query_argument('image3', True)
        type = self.get_query_argument('type', 0)

        userid = 1
        name = '苹果手机'
        image1 = 'www.baidu.com1'
        image2 = 'www.sina.com1'
        image3 = 'www.163.com1'
        type = 0

        status = 1  # 待审核
        price = self.get_query_argument('price', 0)

        short_desc = self.get_query_argument('short_desc', '')
        desc = self.get_query_argument('short_desc', '')
        view_times = self.get_query_argument('view_times', 0) + 1

        price = 10
        short_desc = '苹果货就是牛逼'
        desc = '好奇，好骑'
        view_times = 11

        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        last_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        create_time = datetime.datetime.now()
        last_modify_time = datetime.datetime.now()


        sql = "insert into msapp_good(user_id,name,status,type,price,view_times, create_time, last_modify_time) values ({},'{}',{},{},{},{}, '{}', '{}')".format(userid, name, status, type, price, view_times, str(create_time), str(last_modify_time))

        result2 = dbHelper.insert(sql)

        print(sql)
        print("------------------------%s"%result2)
        content = json.dumps({
            'userid': userid,
            'name': name,
            'image1': image1,
            'image2': image2,
            'image3': image3,
            'status': status,
            'price': price,
            'short_desc': short_desc,
            'desc': desc,
            'view_times': view_times,
        })

        self.write(content)
        self.finish()