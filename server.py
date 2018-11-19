# coding:utf8

import tornado.ioloop
import os
from application import Application
from config import options
from tornado.httpserver import HTTPServer
from index import WechatLoginHandler, IndexHandler, UploadHandler

app = tornado.web.Application([
    (r'/fps/wechat_login', WechatLoginHandler),
    (r'/fps/index', IndexHandler),
    (r'/upload', UploadHandler),
])

if __name__ == "__main__":
    # app = Application()
    # app = Application()
    server = HTTPServer(app)

    server.listen(options.get('port'))  # 只在单进程中这样使用

    tornado.ioloop.IOLoop.current().start()
