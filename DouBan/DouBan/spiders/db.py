# -*- coding: utf-8 -*-
from datetime import datetime
import scrapy
import re
import time
import copy


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']

    def parse(self, response):
        time.sleep(0.3)
        bb = response.xpath('//*[@id="content"]/div/div[1]/div[2]/div')

        item={}
        for i in bb:
            big_name = i.xpath('./a/h2/text()').extract_first()

            smal_name_list=i.xpath('./table/tbody/tr/td/a/text()').extract()
            item['big_name']=big_name
            item['smal_name_list']=smal_name_list
            item['offset']=0

            for sml_tag in smal_name_list:
                item['sml_tag'] = sml_tag

                url = "https://book.douban.com/tag/{0}?start={1}&type=T".format(item['sml_tag'],item['offset'] )

                yield scrapy.Request(url=url, callback=self.get_all_page, meta={'item': copy.deepcopy(item)})

    def get_all_page(self, response):
        time.sleep(0.3)
        item=response.meta['item']

        book_url_list = response.xpath('//div[@class="info"]/h2/a/@href').extract()

        next_ = response.xpath('//span[@class="next"]/a/@href').extract_first()

        for url in book_url_list:
            yield scrapy.Request(url=url,callback=self.get_book_detail,meta={'item':copy.deepcopy(item)})
        if next_ and item['offset']<980:

            item['offset']=int(item['offset'])+20
            url = "https://book.douban.com/tag/{0}?start={1}&type=T".format(item['sml_tag'], item['offset'])

            yield scrapy.Request(url=url,callback=self.get_all_page,meta={'item':copy.deepcopy(item)})




    def get_book_detail(self, response):
        time.sleep(0.3)

        book_info_details = ['作者', '副标题', '出版社', '出品方', '原作名', '译者', '出版年', '页数', '定价', '装帧', '丛书', 'ISBN',
                             '统一书号']



        details = response.xpath('//div[@id="info"]//text()').extract()
        details = re.sub('\s', '', "".join(details))

        field_info_set = [('作者', 'author'), ('副标题', 'subtitle'), ('出版社', 'publish'), ('出品方', 'Producer'
                                                                                      ), ('原作名', "Org_title"),
                          ('译者', "translator"""), ('出版年', "publish_date"), ('页数', "pages"), ('定价', "price"),
                          ('装帧', 'framing'), ('丛书', 'books'), ('ISBN', 'ISBN'), ('统一书号', 'ISBN')]
        value_dict = response.meta['item']

        value_dict['score'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract_first()
        value_dict['title'] = response.xpath('//div[@id="wrapper"]/h1/span/text()').extract_first()
        value_dict['book_summary'] = re.sub('\s', '',''.join(response.xpath('//*[@id="link-report"]/div[1]/div//text()').extract()))
        value_dict['author_summary'] = re.sub('\s', '',''.join(response.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div//text()').extract()))

        for field, field_name in field_info_set:

            _ = re.search('%s:(.*?):' % field, details + ":")
            if _:
                dres = _.group(1)
                value = re.sub("作者|副标题|出版社|出品方|原作名|译者|出版年|页数|定价|装帧|丛书|ISBN|统一书号", '', dres)
                value_dict[field_name] = value
            else:
                if field == "统一书号":
                    if value_dict['ISBN']:
                        continue

                value_dict[field_name] = None

        value_dict = self.data_cleaaning(value_dict)



        yield value_dict

    def data_cleaaning(self,value_dict):

        try:
            value_dict['price']=float(re.search('\d\.*\d*',value_dict['price']).group())
        except:
            value_dict['price'] = 0

        try:
            value_dict['score']=float(value_dict['score'])
        except:
            value_dict['score'] = 0
        try:
            value_dict['pages']=int(value_dict['pages'])
        except:
            value_dict['pages'] = 0





        publish_date=value_dict['publish_date']
        if publish_date:
            date_list=publish_date.split('-')
            if len(date_list)==1:
                publish_date=datetime(int(date_list[0]),1,1)
            elif len(date_list)==2:
                publish_date=datetime(int(date_list[0]),int(date_list[1]),1)
            elif len(date_list) == 3:
                publish_date=datetime(int(date_list[0]),int(date_list[1]),int(date_list[2]))

        try:
            value_dict['publish_date']=publish_date.strftime('%Y-%m-%d')
        except:
            value_dict['publish_date']=publish_date



        return value_dict

