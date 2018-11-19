# coding:utf8
import tornado.web

from index import WechatLoginHandler, IndexHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/fps/wechat_login', WechatLoginHandler),
            (r'/fps/index', IndexHandler),
        ]
        super(Application, self).__init__(handlers)

