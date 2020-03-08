# coding:utf8
"""
@ Author Jue
@ Date 2020-03-01 11:48:24

"""
import hashlib
import time
from config import settings


def getToken(id):
    time_stamp = time.time()
    text = str(time_stamp) + "&" + str(id)
    print("getToken", text)
    md5hash = hashlib.md5(text.encode('utf-8'))
    md5 = md5hash.hexdigest()
    return md5


def getSig(time_stamp):
    text = str(time_stamp) + "&" + settings.get('url_secret')
    md5hash = hashlib.md5(text.encode('utf-8'))
    md5 = md5hash.hexdigest()
    return md5


def check_args(hander):
    time_stamp = hander.get_argument('time_stamp', "-1")
    if time_stamp == -1:
        print("check_args failed time_stamp valid!")
        return False

    sig = hander.get_argument('sig', '-1')
    if sig == '-1':
        print("check_args failed sig valid!")
        return False

    now = time.time()

    if abs(now - int(time_stamp) / 1000) > 15:
        print("check_args time offset reach max!")
        return False

    mysig = getSig(time_stamp)

    return mysig == sig
