import re

from pandas import json
from common.aes import AesCrypt

class Responsedata():
    def __init__(self,response,post_data,logger,case_id):
        self.response = response
        self.post_data = post_data
        print(type(post_data), post_data)
        self.logger = logger
        self.case_id = case_id
    def handle_data(self):
        post_data = self.post_data['jsonParas']
        post_data = AesCrypt().decrypt(post_data)
        response_data = re.findall('.*org/">(.*)</string>.*', self.response.text)
        response_data = AesCrypt().decrypt(''.join(response_data))
        #print('response_data111:',response_data)
        response_data = json.loads(response_data)

        # 日志
        self.logger.info("case_id" + str(self.case_id) + '请求时间为' + str(self.response.elapsed.microseconds))
        self.logger.info("case_id" + str(self.case_id) + "入参" + post_data)
        self.logger.info("case_id" + str(self.case_id) + "出参" + json.dumps(response_data))
        return response_data


