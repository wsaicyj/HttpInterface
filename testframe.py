#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

import requests
import unittest
import json

class CallApi():

    def apicall(selfs,url,payload):


        r = requests.post(url, payload)

        jsdata = json.loads(r.text)

        return jsdata



    '''
    def apicall(self,method,url,getparams,postparams):

        result = ''

        if method == 'GET':
            if getparams != '':
                result = requests.get(url,getparams)
            else:
                result = requests.get(url)
        if method == 'POST':
            if postparams != '':
                result = requests.post(url,postparams)

        jsdata = json.loads(result.text)

        return jsdata
    '''
class APIGetAdList(unittest.TestCase):

    def test_call(self):
        api = CallApi()
        method = 'post'
        url = 'http://120.197.58.120:9090/Sourcepool/httpservice/index.html?method=getPubcat'
        #getparams = ''
        payload = dict(cid='402881ed5431bc0e015431bcb5ce0001',token='weixin123')

        data = api.apicall(url, payload)
        print(data)

        if(data['msg'] == None):
                self.assertEqual(6, data['count'])
                print("接口 index/getadlist------------OK！")
        else:
                print("接口 index/getadlist------------Failure！")
                self.assertEqual(0, data['errno'])

if __name__ == "__main__":
    unittest.main()