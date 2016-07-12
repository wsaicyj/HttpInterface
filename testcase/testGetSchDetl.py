#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

#from ddt import ddt, data, unpack
import unittest
from papi.httprequest import SendHttpRequest
from papi.dataprase import jsonprase
from pyapilog import pyapixml



class GetSschDetlTest(unittest.TestCase):
    '''
    号源资料
    select * from base_channel bc;
    select * from base_hospital_info bhi;
    select * from base_subsourcepool_info bsi;
    '''

    def setUp(self):
        self.url = 'http://120.197.58.120:9090/Sourcepool/httpservice/index.html?method=getSchDetl'

    def test_GetSchDetl(self):
        value = dict(cid='402881ed5431bc0e015431bcb5ce0001',token='weixin123',uid='2494AE0905EA483F8CDC6C3F94F4927E',schid='402881ec55013b260155013b74b90e73')
        data = SendHttpRequest(self.url).post_json(value)
        json_data = jsonprase(data)
        pyapixml(json_data.json_to_xml)
        #print(data)
        print(json_data.json_to_xml)


if __name__ == '__main__':
    unittest.main()
