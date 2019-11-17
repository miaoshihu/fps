# coding:utf8

"""
@ Author Jue
@ Date 2019-11-17 10:58:27

"""

import json


def json_error(code, error_text):
    print("json_error called")
    content = json.dumps({
        'code': code,
        'desc': error_text,
    })

    return content
