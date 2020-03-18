# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import json

from scrapy import signals

import requests
import random
import time


from DouBan.settings import USER_AGENTS_LIST # 注意导入路径,请忽视pycharm的错误提示
#
# class Gettime(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._time1 = time.time()
#             cls.PROXY_LIST=['223.214.205.8:19365',
# '115.211.231.1:15358',
# '144.255.149.184:21779']
#         return cls._instance
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS_LIST)
        request.headers['User-Agent'] = user_agent
        # 不写return


class ProxyMiddleware(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.now_1=time.time()
        self.PROXY_LIST=['111.176.31.251:20423']

    def process_request(self, request, spider):
        now_2=time.time()



        if (now_2-self.now_1)>360:
            print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
            self.now_1=now_2

            # API接口，返回格式为json
            api_url = "http://dps.kdlapi.com/api/getdps/?orderid=988346264125524&num=10&pt=1&sep=1&signature=atvb6a4981d03pvpqalolea9e0k2pmi6&protocol=1&method=2&an_an=1&an_ha=1&quality=2&format=json&sep=1"  # API接口

            # API接口返回的ip
            self.PROXY_LIST = json.loads(requests.get(api_url).text)['data']['proxy_list']
            print(self.PROXY_LIST)

        #     # 用户名和密码(私密代理/独享代理)
        up = "749684756:hhjvexkj"

        proxyAuth = "Basic " + base64.b64encode(up.encode()).decode()

        IP = random.choice(self.PROXY_LIST)
        # 设置代理
        request.meta["proxy"] = IP
        # # 设置认证
        request.headers["Proxy-Authorization"] = proxyAuth

