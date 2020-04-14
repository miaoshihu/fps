# coding:utf8

"""
@ Author Jue
@ Date 2019-11-17 10:58:27

"""

import json


def json_error(code, error_text):
    content = json.dumps({
        'code': code,
        'desc': error_text,
    })

    return content


def json_success(text):
    content = json.dumps({
        'code': 0,
        'desc': text,
    })

    return content


def json_success_data(text, data):
    content = json.dumps({
        'code': 0,
        'desc': text,
        'data': data,
    })

    return content
