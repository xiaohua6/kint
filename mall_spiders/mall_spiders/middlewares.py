# # -*- coding: utf-8 -*-
#
# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#
# from scrapy import signals
#
#
# class MallSpidersSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class MallSpidersDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
import base64
import json
import random
import time

import requests
from .settings import USER_AGENTS_LIST

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
        self.api_url = "http://dps.kdlapi.com/api/getdps/?orderid=988346264125524&num=10&pt=1&sep=1&signature=atvb6a4981d03pvpqalolea9e0k2pmi6&protocol=1&method=2&an_an=1&an_ha=1&quality=2&format=json&sep=1"
        self.PROXY_LIST = json.loads(requests.get(self.api_url).text)['data']['proxy_list']

    def process_request(self, request, spider):
        now_2=time.time()



        if (now_2-self.now_1)>360:
            print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
            self.now_1=now_2

            # API接口，返回格式为json
            api_url = "http://dps.kdlapi.com/api/getdps/?orderid=988346264125524&num=10&pt=1&sep=1&signature=atvb6a4981d03pvpqalolea9e0k2pmi6&protocol=1&method=2&an_an=1&an_ha=1&quality=2&format=json&sep=1"  # API接口

            # API接口返回的ip
            self.PROXY_LIST = json.loads(requests.get(self.api_url).text)['data']['proxy_list']


        #     # 用户名和密码(私密代理/独享代理)
        up = "749684756:hhjvexkj"

        proxyAuth = "Basic " + base64.b64encode(up.encode()).decode()

        IP = random.choice(self.PROXY_LIST)
        # 设置代理
        request.meta["proxy"] = IP
        # # 设置认证
        request.headers["Proxy-Authorization"] = proxyAuth