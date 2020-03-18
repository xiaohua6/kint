# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from mall_spiders.spiders.jd_category import JdCategorySpider
from mall_spiders.spiders.jd_product import JdProductSpider
class MallSpidersPipeline(object):
    def process_item(self, item, spider):
        return item

class CategoryPipeline(object):
    def open_spider(self,spider):
        if isinstance(spider,JdCategorySpider):
            self.client=MongoClient()
            self.collection=self.client['jd']['category']

    def process_item(self,item,spider):
        if isinstance(spider,JdCategorySpider):
            self.collection.insert_one(dict(item))

        return item
    def close_spider(self,spider):
        if isinstance(spider,JdCategorySpider):
            self.client.close()
        pass


class ProductPipeline(object):
    def open_spider(self,spider):
        if isinstance(spider,JdProductSpider):
            self.client=MongoClient()
            self.collection=self.client['jd']['product']

    def process_item(self,item,spider):
        if item!=None:
            if isinstance(spider,JdProductSpider):
                print(item)
                self.collection.insert_one(dict(item))
        else:
            print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
                  ''
                  ''
                  ''
                  '')
            return None

        return item
    def close_spider(self,spider):
        if isinstance(spider,JdProductSpider):
            self.client.close()



