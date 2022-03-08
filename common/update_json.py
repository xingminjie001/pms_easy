import json

#更新一个json

def update_target_value(key, dic, target_value):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys() and dic[key]!=None:
        if isinstance(dic[key], list) and not isinstance(target_value, list):
            dic[key] = [target_value]
        elif not isinstance(dic[key], list) and isinstance(target_value,list):
            dic[key] = target_value[0]
        else:
            dic[key] = target_value  # 更新数据
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                update_target_value(key, value, target_value)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, target_value)  # 传入数据的value值是列表或者元组，则调用_get_value
    print(target_value)
    return target_value


def _get_value(key, val, target_value):
    for val_ in val:
        if isinstance(val_, dict):
            update_target_value(key, val_, target_value)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, target_value)   # 传入数据的value值是列表或者元组，则调用自身


if __name__ == "__main__":
    content = '{"RQModel_CheckInfo":[{"Identity":"18611625312","ArrDate":"2020-02-26","DptDate":"2020-03-04","Status":"1","SearchFlg":"3","SearchMainAcct":"False","SearchLockFlag":"False"}],"grpcd":"lc","htlcd":"lc01","staffcd":"9897","token":"52138214DD7DC7A80073B3C2CF3D2AD5F0841C16","staffpassword":"sunwood","isformal":"True","mac":"6C-0B-84-08-06-78"}'
    content = json.loads(content)
    # del_data(key,content)
    # data = json.loads(content)
    #update_target_value('token',content,'1111111111111111111111')
