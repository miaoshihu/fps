# coding:utf8

import tornado.ioloop
from application import Application
from config import options

if __name__ == "__main__":
    app = Application()
    app.listen(options.get('port'))  # 只在单进程中这样使用

    tornado.ioloop.IOLoop.current().start()
