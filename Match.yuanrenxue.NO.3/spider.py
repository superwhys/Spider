#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# @File    ：spider.py
# @IDE     ：PyCharm 
# @Author  ：SuperYong
# @Date    ：2021/11/19 14:38 
# @Summary : this is the summary

import requests
from collections import Counter

session = requests.session()

headers = {
    'Host': 'match.yuanrenxue.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.10 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://match.yuanrenxue.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://match.yuanrenxue.com/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

session.headers = headers
cookies = {'Cookie': 'sessionid=;'}


res_lst = []
for i in range(1, 6):
    session.post('https://match.yuanrenxue.com/jssm', cookies=cookies)

    headers['user-agent'] = 'yuanrenxue.project'

    res = session.get(f"http://match.yuanrenxue.com/api/match/3?page={i}").json()
    for data in res.get('data'):
        res_lst.append(data.get('value'))


print(Counter(res_lst).most_common(1)[0][0])
