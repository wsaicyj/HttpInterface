#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

from ddt import ddt, data, unpack
import unittest
from papi.httprequest import SendHttpRequest
from papi.dataprase import jsonprase


@ddt
class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.url = 'http://120.197.58.120:9090/Sourcepool/httpservice/index.html?method=getPubcat'

    @unpack
    @data(('402881ed5431bc0e015431bcb5ce0001','weixin123'))
    def test_GetPubcat(self,cid,token):
        value = {'cid': cid, 'token': token}
        #data = SendHttpRequest(self.url).get(value)
        data = SendHttpRequest(self.url).post_json(value)
        json_data = jsonprase(data)
        print(json_data)
        '''
        point_lat = json_data.find_json_node_by_xpath("/Point/Lat")
        point_lng = json_data.find_json_node_by_xpath("/Point/Lng")
        is_exists_map = json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/IsExistsMap")
        size = json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/Size")
        # 断言
        assert float(point_lat) != 0 and float(point_lng) != 0
        # 断言
        assert json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/DownUrl") is not None
        if is_exists_map == True:
            assert size != ""
        '''


'''

@ddt
class TestSingleRequest(unittest.TestCase):
    def setUp(self):
        self.url = "http://xxxxxxxxxxxxxxxxxxx/api/xxxxxx"
    @data(
        (32351, 6),
        (9, 4)
    )
    @unpack
    def test_Single_right(self, sid, count):
        value = {"sid": sid, "count": count}
        data = SendHttpRequest(self.url).get(value)
        json_data = jsonprase(data)
        point_lat = json_data.find_json_node_by_xpath("/Point/Lat")
        point_lng = json_data.find_json_node_by_xpath("/Point/Lng")
        is_exists_map = json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/IsExistsMap")
        size = json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/Size")
        # 断言
        assert float(point_lat) != 0 and float(point_lng) != 0
        # 断言
        assert json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/DownUrl") is not None
        if is_exists_map == True:
            assert size != ""

    # 导常请求SingleRequest接口
    @data(
        ("abceeffffg", 6),
        (9, "")
    )
    @unpack
    def test_Single_error(self, sid, count):
        value = {"sid": sid, "count": count}
        data = SendHttpRequest(self.url).get(value)
        self.assertEqual(data, u'{"Message":"请求无效。"}')

@ddt
class TourMaps(unittest.TestCase):
    def setUp(self):
        self.url = "http://xxxxxx/api/TourMap"

    @data(32351, 9)
    def test_requests_online_xml(self, tourId):
        xml_url = self.url + "/%s" % tourId
        data = SendHttpRequest(xml_url).get()
        json_st = xmlprase(data).xml_to_json
        json_data = jsonprase(json_st)
        lng = json_data.find_json_node_by_xpath("/root/data/@lng")
        lat = json_data.find_json_node_by_xpath("/root/data/@lat")
        assert lng != "" and lat != ""
        son_tour = json_data.find_json_node_by_xpath("/root/data/data")
        assert len(son_tour) > 0

class TourData(unittest.TestCase):
    def setUp(self):
        self.url = "http://xxxxxx/api/xxx"

    @data(
        (),
        (),
        (),
    )
    @unpack
    def test_tourList_Location_in_open(self):
        pass

    def test_tourList_Location_not_open(self):
        pass

    def test_tour_open_city(self):
        pass
'''


if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestDepartment)
    # unittest.TextTestRunner(verbosity=2).run(suite)