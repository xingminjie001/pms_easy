from urllib import parse

import requests
from common.readconfig import ReadConfig
from common.logger import Logger
import json
# logger = Logger(logger_name='ConfigHttp').getlog()

class ConfigHttp:
    def __init__(self,name):
        self.logger = Logger(logger_name=name).getlog()
        global url,timeout,header
        header={}
        config = ReadConfig()

        url = config.get_config_value('apiDomain','domain')
        timeout = config.get_config_value('apiDomain','timeout')
        self.headers = config.get_config_section_dict('HEADERS')
        self.data = None
        self.url = None
        self.files = {}

    def set_url(self, para_api):   #拼接ip方法
        self.url = url+para_api
        return self.url


    def set_url2(self, para_api):
        self.url = para_api
        return self.url

    def set_headers(self):
        return self.headers

    def set_cookies(self,cookie):
        pass
        #self.headers['cookie'] = 'ASP.NET_SessionId='+ cookie


    def set_data(self,data):
        #self.data = parse.urlencode(self.data)
        self.data = data

    def set_files(self,file):
        self.files = file

    def get(self):
        try:
            response = requests.get(self.url,headers = self.headers,params = None,timeout = float(timeout))
            return response
        except TimeoutError:
            # pass
            self.logger.error('TIME OUT %s .'%self.url)

    def post(self):
        try:
            response = requests.post(self.url,headers = self.headers,data = self.data,timeout = float(timeout))
            return response
        except TimeoutError:
            # pass
            self.logger.error('TIME OUT %s .'%self.url)


if __name__ == '__main__':
    print(ConfigHttp('p').set_headers())
    print(ConfigHttp('').set_url('/test'))
