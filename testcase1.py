#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

from ddt import ddt, data, unpack
import unittest
from papi.httprequest import SendHttpRequest
from papi.dataprase import jsonprase
from pyapilog import pyapixml


@ddt
class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.url = 'http://120.197.58.120:9090/Sourcepool/httpservice/index.html?method=getPubcat'


    def test_GetPubcat(self):
        #value = {'cid': cid, 'token': token}
        value = dict(cid='402881ed5431bc0e015431bcb5ce0001',token='weixin123')
        #data = SendHttpRequest(self.url).get(value)
        data = SendHttpRequest(self.url).post_json(value)
        json_data = jsonprase(data)
        '''
        with open('test_GetpUBCAT.xml','w',encoding='utf-8') as f:
            f.write(json_data.json_to_xml)
        '''
        pyapixml(json_data.json_to_xml)
        print(json_data.json_to_xml)



if __name__ == "__main__":
    unittest.main()
