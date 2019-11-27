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


class UploadHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-type', 'text/html')

    def get(self):
        print('UploadHandler get')
        self._handle_request()

    def post(self):
        print('UploadHandler post')
        self._handle_request()

    def _handle_request(self):

        print("_handle_request")
        # str = "good man"

        # self.request
        file_name = self.get_argument('file_name', 'null')
        file_md5 = self.get_argument('file_md5', True)
        file_path = self.get_argument('file_path', True)
        file_content_type = self.get_argument('file_content_type', True)
        file_size = self.get_argument('file_size', True)
        image1 = self.get_argument('image1', True)
        image2 = self.get_argument('image2', True)

        my_name = self.get_argument('myname', True)

        os.rename(file_path, file_path + ".jpg")

        (path, filename) = os.path.split(file_path + ".jpg")

        content = json.dumps({
            'name': file_name + ".jpg",
            'content_type': file_content_type,
            'md5': file_md5,
            'path': file_path,
            'size': file_size,
            'filename' : filename,
            # 'desc': str(self.request),
            # 'args': str(self.request.arguments),
            # 'query_arguments': str(self.request.query_arguments),
            # 'body_arguments': str(self.request.body_arguments),
            # 'files': str(self.request.files),
        })

        print("_handle_request", "path-:", path)
        print("_handle_request", "filename", filename)

        print("_handle_request", "my_name", my_name)
        print("_handle_request", "image1", image1)
        print("_handle_request", "image2", image2)

        print("%%%%%%%%%%%%%%%%%%%%%haha, upload done: ", json.dumps(content))

        self.write(content)
        self.finish()
