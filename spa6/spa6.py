#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# @File    ：spa6.py
# @IDE     ：PyCharm 
# @Author  ：SuperYong
# @Date    ：2021/11/16 15:37 
# @Summary : this is the summary
import requests
from time import time
from hashlib import sha1
from base64 import b64encode


def get_token():
    now = str(int(time()))
    api_path = '/api/movie'
    plain_text = f'{api_path},{now}'

    plain_text_sha1 = sha1(plain_text.encode('utf-8')).hexdigest()
    b64_plain_text = f'{plain_text_sha1},{now}'

    token = b64encode(b64_plain_text.encode('utf-8')).decode('utf-8')
    return token


def req():

    token = get_token()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }

    for page in range(0, 100, 10):
        params = (
            ('limit', '10'),
            ('offset', str(page)),
            ('token', token),
        )

        response = requests.get('https://spa6.scrape.center/api/movie/', headers=headers, params=params)
        print(response.text)


if __name__ == '__main__':
    req()
