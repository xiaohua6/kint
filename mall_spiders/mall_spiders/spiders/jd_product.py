# -*- coding: utf-8 -*-
import json
import pickle

from jsonpath import jsonpath
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str

from mall_spiders.items import ProductItem

class JdProductSpider(RedisSpider):
    name = 'jd_product'
    # allowed_domains =
    # start_urls = ['https://jd.com/']
    redis_key = 'satrturljd'

    def __init__(self, *args, **kwargs):

        # Dynamically define the allowed domains list.
        domain = "jd.com,3.cn'"
        print(domain)
        self.allowed_domains = ['jd.com','3.cn']

        super(JdProductSpider, self).__init__(*args, **kwargs)

    def make_request_from_data(self, data):
        """Returns a Request instance from data coming from Redis.

        By default, ``data`` is an encoded URL. You can override this method to
        provide your own message decoding.

        Parameters
        ----------
        data : bytes
            Message from redis.

        """
        url_ = pickle.loads(data)
        url=url_['s_category_url']
        return scrapy.Request(url,callback=self.parse,meta={'category_name':url_['s_category_name']})


    # def start_requests(self):
    #
    #
    #     dict1={"b_category_name" : "工业品", "b_category_url" : "https://imall.jd.com/",
    #            "m_category_name" : "工控配电", "m_category_url" : "https://imall.jd.com/dianqi.html",
    #            "s_category_name" : "工业控制", "s_category_url" : "https://coll.jd.com/list.html?sub=47560" }
    #     # print(dict1['s_category_url'])
    #     yield scrapy.Request(url=dict1['s_category_url'],callback=self.parse,meta={'category_name':dict1['s_category_name']})
    #     pass

    def parse(self, response):


        sku_id_list=response.xpath("//div[contains(@class,'j-sku-item')]/@data-sku").extract()
        # print(sku_id_list)
        for sku_id in sku_id_list:
            url='https://cdnware.m.jd.com/c1/skuDetail/apple/7.3.0/{}.json'.format(sku_id)

            yield scrapy.Request(url=url,callback=self.get_content,meta=response.meta)

        next_page=response.xpath('//a[@class="pn-next"]/@href').extract_first()
        if next_page:
            next_page_url=response.urljoin(next_page)
            # print(next_page_url)
            yield scrapy.Request(url=next_page_url,callback=self.parse,meta=response.meta)

    def get_content(self,response):
        """
        Product_category=scrapy.Field()  #商品类别
        Product_category_id=scrapy.Field()  #商品类别id
        Product_sku_id=scrapy.Field()  #商品id
        Product_name=scrapy.Field()  #商品名称
        product_img_url=scrapy.Field()  #商品图片连接
        product_book_info=scrapy.Field()  #商品t图书信息，作者出版社
        product_option=scrapy.Field()  #商品选项
        product_shop=scrapy.Field()   #商品店铺
        product_comments=scrapy.Field()   #商品评论
        product_ad=scrapy.Field()   #商品促销
        product_price=scrapy.Field()   #商品价格


        :param response:
        :return:
        """
        category_name=response.meta['category_name']


        item=ProductItem()

        res_json=json.loads(response.text)
        if res_json['code']!=0:
            return
        shop=jsonpath(res_json,'$..shop')
        if shop[0]:
            item['product_shop']={'shopId':shop[0]['shopId'], 'name': shop[0]['name'], 'score': shop[0]['score'], 'url':shop[0]['url']}

        else:
            item['product_shop']={'name':'京东自营'}

        item['product_category']=category_name
        item['product_category_id']=jsonpath(res_json,'$..category')[0].replace(';',',')
        item['product_sku_id']=jsonpath(res_json,'$..wareId')[0]
        item['product_name']=jsonpath(res_json,'$..basicInfo')[0]['name']
        item['product_img_url']=jsonpath(res_json,'$..wareImage')[0][0]['small']
        item['product_book_info']=jsonpath(res_json,'$..bookInfo')[0]

        try:
            colorsize = jsonpath(res_json, '$..colorSize')[0]
            b = {}
            for cs in colorsize:
                b[cs['title']] =cs['buttons']
        except TypeError:
            b={}

        item['product_option'] =b

        yield scrapy.Request(url='https://p.3.cn/prices/mgets?skuIds=%s' % item['product_sku_id'], meta={'item': item},
                             callback=self.get_price)

    def get_price(self, response):
        price_list = json.loads(response.body)
        item = response.meta['item']

        item['product_price'] = float(price_list[0]['op'])
        url="https://cd.jd.com/promotion/v2?skuId={0}&area=12_904_50647_0&cat={1}".format(item['product_sku_id'],item['product_category_id'])
        # yield item
        yield scrapy.Request(url=url,callback=self.get_ad,meta={'item': item})

    def get_ad(self,response):
        item=response.meta['item']

        res_json=json.loads(response.text)
        item['product_ad'] =jsonpath(res_json,'$..ad')[0]

        url='https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}'.format(item['product_sku_id'])
        yield scrapy.Request(url=url,callback=self.get_comment,meta={'item':item})

    def get_comment(self,response):
        item=response.meta['item']
        res_json=json.loads(response.text)
        item['product_comments']={'CommentCount':res_json["CommentsCount"][0]['CommentCount'],
                          'GeneralCount':res_json["CommentsCount"][0]['GeneralCount'],
                          'GoodCount':res_json["CommentsCount"][0]['GoodCount'],
                          'PoorCount':res_json["CommentsCount"][0]['PoorCount'],
                          'AverageScore':res_json["CommentsCount"][0]['AverageScore'],
                          }


        yield item



