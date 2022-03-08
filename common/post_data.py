import json,re,time
from common.aes import AesCrypt
from common.request_update import Update_all
class Postdata:
    def __init__(self,data,associate_id,get_param,set_param,sheet_name):
        self.data = data
        self.associate_id = associate_id
        self.get_param = get_param
        self.set_param = set_param
        self.sheet_name = sheet_name
    def handle_data(self):
        if self.associate_id != "" :#判断是否需要修改入参
            id_list = self.associate_id.split(',')
            get_param_list = self.get_param.split(',')
            set_param_list = self.set_param.split(',')
            #print('data111:',self.data)
            for id, get_param, set_param in zip(id_list, get_param_list, set_param_list):
                if set_param in self.data:
                    self.data = json.loads(self.data)
                    self.data = Update_all().update_all(self.sheet_name, id, self.data, get_param, set_param)
                    self.data = json.dumps(self.data)
                    self.data = AesCrypt().encrypt(self.data).decode('utf-8')
                    self.data = {"jsonParas": self.data}
        else:
            self.data = AesCrypt().encrypt(self.data).decode('utf-8')
            self.data = {"jsonParas": self.data}
        return self.data
if __name__ == '__main__':
    pass
    #content ={'handleDto': {}, 'responseCommonDto': {'resvNo': None, 'errorLevel': '0', 'invokerEndTime': 4938829387425979, 'lans': None, 'message': '000000', 'resultCode': '0', 'sessionKey': None, 'token': '6af80826-eba3-4e45-bb32-78b40541fef4', 'tracerId': None, 'userUid': None}, 'resultData': [{'acctNo': ['F0010160'], 'arrDt': None, 'breakFlg': None, 'dptDt': None, 'errorFlg': '0', 'errorRoomNums': None, 'noShareRoomNums': None, 'resvNo': 'R0010134', 'shareAcctNos': None, 'shareFlg': None, 'shareRoomNums': None, 'shareSeq': 'S0010160'}]}
    #print(content.__contains__('acctNo'))