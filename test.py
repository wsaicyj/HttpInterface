#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'


import requests
import json


def callapi(url,payload):
    r = requests.post(url, data=payload)
    print(r)
    jsdata = json.loads(r.text)
    print(jsdata)

url = 'http://120.197.58.120:9090/Sourcepool/httpservice/index.html?method=getPubcat'
payload = dict(cid='402881ed5431bc0e015431bcb5ce0001',token='weixin123')
callapi(url,payload)