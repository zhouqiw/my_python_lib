# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo.py
@time: 2018/4/27 下午10:06
"""

import json

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print(test_dict)
print(type(test_dict))
#dumps 将数据转换成字符串
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))

with open("./record.json","w") as f:
     json.dump(new_dict,f)
     print("加载入文件完成...")



with open("../config/record.json",'r') as load_f:
     load_dict = json.load(load_f)
     print(load_dict)
load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
5 print(load_dict)
6
7 with open("../config/record.json","w") as dump_f:
8     json.dump(load_dict,dump_f)