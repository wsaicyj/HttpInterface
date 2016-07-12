#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import unittest
from setting import url

class SetYuYueTest(unittest.TestCase):

    def setUp(self):
        self.url = url + '/httpservice/index.html?method=setYuyue'

    def test_setYuYue(self):
        value = dict(cid='',token='',uid='',dep_id='',phone='',card='',card_type='',truename='',sex='',birth='',detlid='')



if __name__ == '__main__':
    unittest.main()
