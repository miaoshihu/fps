# coding:utf8

import tornado.ioloop
import os
from config import options
from tornado.httpserver import HTTPServer
from index import GoodGetListHandler
from api.good import GoodSubmit
from api.login import LoginHandler
from api.upload import UploadHandler

app = tornado.web.Application([
    (r'/fps/login', LoginHandler),
    (r'/upload', UploadHandler),
    (r'/fps/good/submit', GoodSubmit),
    (r'/fps/good/getlist', GoodGetListHandler),
])

if __name__ == "__main__":
    server = HTTPServer(app)

    server.listen(options.get('port'))  # 只在单进程中这样使用

    tornado.ioloop.IOLoop.current().start()
