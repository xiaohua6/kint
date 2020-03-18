# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CategoryItem(scrapy.Item):

    b_category_name=scrapy.Field()  #大标签名字
    b_category_url=scrapy.Field()   #大标签的url
    m_category_url=scrapy.Field()   #中标签的url
    m_category_name=scrapy.Field()   #中标签的名字
    s_category_name=scrapy.Field()   #小标签的名字
    s_category_url=scrapy.Field()   #小标签的url

class ProductItem(scrapy.Item):
    product_category=scrapy.Field()  #商品类别
    product_category_id=scrapy.Field()  #商品类别id
    product_sku_id=scrapy.Field()  #商品id
    product_name=scrapy.Field()  #商品名称
    product_img_url=scrapy.Field()  #商品图片连接
    product_book_info=scrapy.Field()  #商品t图书信息，作者出版社
    product_option=scrapy.Field()  #商品选项
    product_shop=scrapy.Field()   #商品店铺
    product_comments=scrapy.Field()   #商品评论
    product_ad=scrapy.Field()   #商品促销
    product_price=scrapy.Field()   #商品价格



