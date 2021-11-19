#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# @File    ：parseSpider.py
# @IDE     ：PyCharm 
# @Author  ：SuperYong
# @Date    ：2021/11/18 10:34 
# @Summary : this is the summary 
from time import time
import requests
import execjs

# 4df4472f5fa5ccee5c59713c5a7df196丨1637307724000

jscontext = execjs.compile(open('atob-window-b.js', encoding='utf-8').read())
a = jscontext.call('getToken')
print(a)

headers = {
    'user-agent': 'yuanrenxue.project',
    'cookie': 'sessionid=u11ufojr42dseutfyq4015b4qcmqm8d4;',
}


sum = 0
num = 0
for i in range(1, 6):
    params = (
        ('page', i),
        ('m', a),
    )

    response = requests.get('https://match.yuanrenxue.com/api/match/1', headers=headers, params=params)
    data_lst = response.json().get('data')
    print(data_lst)
    for data in data_lst:
        sum += data.get('value')
        num += 1

print(sum / num)
