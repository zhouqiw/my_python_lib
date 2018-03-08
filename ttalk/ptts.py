# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: ptts.py
@time: 2018/1/16 下午10:15
"""

# -*- coding: UTF-8 -*-
#
# import sys
# import pyttsx
# # reload(sys)
# # sys.setdefaultencoding("utf-8")
# text = u'你好，中文测试'
# engine = pyttsx.init()


from aip import AipSpeech
""" 你的百度 APPID AK SK
https://console.bce.baidu.com/ai/#/ai/speech/app/list       应用列表
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top         API
"""
APP_ID = '10703745'
API_KEY = 'ZDNGbZ6sn55DA2B59TsWl9M9'
SECRET_KEY = 'lXHd9bkfg1bOSQzSTu3EzCO76vgRavMU'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
text111 = "招行研发中心数据中心3楼机房温湿度5报警"
result  = client.synthesis(text111, 'zh', 1, {
    'vol': 5,'spd':1,'per': 3,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('/Users/zhouqi/Desktop/python/p_4/ttalk/do.mp3', 'wb') as f:
        f.write(result)