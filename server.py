# coding:utf8

import tornado.ioloop
import os
from config import options
from tornado.httpserver import HTTPServer
from api.good.good_add import GoodSubmit
from api.good.good_list import GoodGetList
from api.good.good_get import GoodGet
from api.need.need_add import NeedSubmit
from api.openid import GetOpenidHandler
from api.upload import UploadHandler
from api.test import Test
from api.author.author_register import AuthorRegister
from api.author.author_login import AuthorLogin


app = tornado.web.Application([
    (r'/fps/getopenid', GetOpenidHandler),
    (r'/upload', UploadHandler),
    (r'/fps/good/submit', GoodSubmit),
    (r'/fps/good/getlist', GoodGetList),
    (r'/fps/good/get', GoodGet),

    (r'/fps/need/submit', NeedSubmit),
    (r'/fps/test', Test),

    (r'/fps/author/register', AuthorRegister),
    (r'/fps/author/login', AuthorLogin),

])

if __name__ == "__main__":
    server = HTTPServer(app)

    server.listen(options.get('port'))  # 只在单进程中这样使用

    tornado.ioloop.IOLoop.current().start()
