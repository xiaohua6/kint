# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy_splash import SplashRequest
from Aqi.items import CityItem

class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/monthdata.php?city=%E6%B7%AE%E5%AE%89']
    #
    # def parse(self, response):
    #     data=response.xpath('//div/li')
    #     # print(data)
    #
    #
    #     for i in data:
    #         item=CityItem()
    #
    #         item['name']=i.xpath('./a/text()').extract_first()
    #
    #         item['link']=response.urljoin(i.xpath('./a/@href').extract_first())
    #         # time.sleep(2)
    #
    #
    #
    #         yield  scrapy.Request(url=item['link'],callback=self.get_month,meta={'name':item['name']})
    #
    # def get_month(self,response):
    #
    #     data=response.xpath('//div/ul[@class="unstyled1"]/li')
    #
    #     name=response.meta['name']
    #
    #
    #     for i in data:
    #
    #         item = dict()
    #
    #         item[name] = i.xpath('./a/text()').extract_first()
    #
    #         item['link'] = response.urljoin(i.xpath('./a/@href').extract_first())
    #         # time.sleep(2)
    #
    #         # print(item['link'])
    #
    #         yield scrapy.Request(url=item['link'], callback=self.get_date_data,meta={'name':name})
    #
    #
    # def get_date_data(self,response):
    #     name=response.meta['name']
    #     # time.sleep(2)
    #
    #     print(response.url)
    #
    #     pass


    def start_requests(self):
        yield SplashRequest(self.start_urls[0],
                            callback=self.parse_splash,
                            args={'wait': 10}, # 最大超时时间，单位：秒
                            endpoint='render.html') # 使用splash服务的固定参数

    def parse_splash(self, response):
        with open('with_splash.html', 'w') as f:
            f.write(response.body.decode())
