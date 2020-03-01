# coding:utf8
"""
@ Author Jue
@ Date 2020-03-01 11:48:24

"""
import hashlib
from config import settings


def getSig(time_stamp):
    text = str(time_stamp) + "&" + settings.get('url_secret')
    md5hash = hashlib.md5(text.encode('utf-8'))
    md5 = md5hash.hexdigest()
    return md5