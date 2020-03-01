# coding:utf8

import tornado.ioloop
import os
from config import options
from tornado.httpserver import HTTPServer
from api.good import GoodSubmit
from api.good import GoodGetList
from api.good import GoodGet
from api.need import NeedSubmit
from api.login import LoginHandler
from api.upload import UploadHandler
from api.test import Test
from api.author import AuthorSubmit, AuthorGet

app = tornado.web.Application([
    (r'/fps/login', LoginHandler),
    (r'/upload', UploadHandler),
    (r'/fps/good/submit', GoodSubmit),
    (r'/fps/good/getlist', GoodGetList),
    (r'/fps/good/get', GoodGet),

    (r'/fps/need/submit', NeedSubmit),
    (r'/fps/test', Test),

    (r'/fps/author/submit', AuthorSubmit),
    (r'/fps/author/get', AuthorGet),

])

if __name__ == "__main__":
    server = HTTPServer(app)

    server.listen(options.get('port'))  # 只在单进程中这样使用

    tornado.ioloop.IOLoop.current().start()
