# -*- coding: utf-8 -*-
#!usr/bin/python
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append("C:/Users/35789/AppData/Roaming/Python/Python36/site-packages")
import unittest,ddt
from common.logger import Logger
from common.confighttp import ConfigHttp
from common import base_api
from common.post_data import Postdata
from common.response_data import Responsedata


#申明类、公共参数

sheet_name='easy'
logger =Logger(logger_name=sheet_name).getlog()
api_xls = base_api.get_xls('case.xlsx',sheet_name)
LocalConfigHttp=ConfigHttp(sheet_name)
#cookie = Login(sheet_name).get_cookies()  # 获取cookie


@ddt.ddt
class TestReverse(unittest.TestCase):
    '''参数化'''

    def setParameters(self,case_id,description,interface,method,data,associate_id,get_param,set_param,ignore_key,message):
        self.case_id = str(case_id)
        self.description = str(description)
        self.interface = str(interface)
        self.method = str(method)
        self.data = str(data)
        self.associate_id = str(associate_id)
        self.get_param = str(get_param)
        self.set_param = str(set_param)
        self.ignore_key = str(ignore_key)
        self.message = str(message)

    @classmethod
    def setUpClass(self):
        pass
        #数据库还原
        #Database().huanyuan(sheet_name)
        #验证数据库是否还原
        # database.get_sql()

    @classmethod
    def tearDownClass(self):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @ddt.data(*api_xls)
    @ddt.unpack
    def testReverse(self,id,description,interface,method,data,associate_id,get_param,set_param,ignore_key,message):
        self.setParameters(id,description,interface,method,data,associate_id,get_param,set_param,ignore_key,message)
        datas = Postdata(self.data,self.associate_id,self.get_param,self.set_param,sheet_name).handle_data()#处理入参
        api_url = self.interface  #获取url
        if 'http'in api_url:#判断url格式是否需要拼接
            LocalConfigHttp.set_url2(api_url)
        else:
            LocalConfigHttp.set_url(api_url)

        LocalConfigHttp.set_headers()#设置header
        #LocalConfigHttp.set_cookies(cookie)#设置cookie
        LocalConfigHttp.set_data(datas)#设置入参

        self.response = LocalConfigHttp.post()#调接口

        #处理出参并写日志
        #self.response1 = LocalConfigHttp.post1()
        response_data = Responsedata(self.response,datas,logger,self.case_id)
        content = response_data.handle_data()
        # 断言状态码
        self.assertEqual(str(self.response.status_code), self.message.split('.')[0])


if __name__ == '__main__':
    unittest.main()
