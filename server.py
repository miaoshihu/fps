# coding:utf8

import tornado.ioloop
import os
from application import Application
from config import options
from tornado.httpserver import HTTPServer
from index import IndexHandler, UploadHandler, GoodGetListHandler
from api.good import GoodSubmit
from api.wechat import WechatLoginHandler

app = tornado.web.Application([
    (r'/fps/wechat_login', WechatLoginHandler),
    (r'/fps/index', IndexHandler),
    (r'/upload', UploadHandler),
    (r'/fps/good/submit', GoodSubmit),
    (r'/fps/good/getlist', GoodGetListHandler),
])

if __name__ == "__main__":
    # app = Application()
    # app = Application()
    server = HTTPServer(app)

    server.listen(options.get('port'))  # 只在单进程中这样使用

    tornado.ioloop.IOLoop.current().start()
