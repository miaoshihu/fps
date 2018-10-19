# coding:utf8
import tornado.web

from index import WechatLoginHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/fps/wechat_login', WechatLoginHandler),
        ]
        super(Application, self).__init__(handlers)

