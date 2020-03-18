# -*- coding: utf-8 -*-
import json      # item['b_category_url']=res['']
        # item['b_category_name']=res['']
        # # 中标签名字和url
        # item['m_category_name']
        # item['m_category_url']
        # # 小标签名字和url
        # item['s_category_name']
        # item['s_category_url']
import re
from jsonpath import jsonpath
import scrapy
from mall_spiders.items import CategoryItem

class JdCategorySpider(scrapy.Spider):
    name = 'jd_category'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):

        res=json.loads(response.body.decode('GBK'))

        item=CategoryItem()

        category_info=res['data']
        for res in category_info:
            b_category_info=res['s'][0]['n']
            b_category_info=b_category_info.split('|')
            item['b_category_name'] = b_category_info[1]
            item['b_category_url'] = 'https://'+b_category_info[0]

            # print('大标签信息',b_category_info)

            m_category_info_list=res['s'][0]['s']

            for m_info in m_category_info_list:
                m_category_info=m_info['n']

                m_category_info=m_category_info.split('|')
                item['m_category_name'] = m_category_info[1]
                item['m_category_url'] = 'https://' + m_category_info[0]
                # print('中分类',m_category_info)
                s_category_list=m_info['s']
                # print(s_category_list)

                for s_info in s_category_list:
                    s_category_info=s_info['n']
                    s_category_info=s_category_info.split('|')
                    item['s_category_name'] = s_category_info[1]
                    if s_category_info[0].count('jd.com')==1:
                        # print('小分类', s_category_info)
                        print(item)
                        yield item
                        item['s_category_url'] = 'https://' + s_category_info[0]
                    elif s_category_info[0].count('-')==1:
                        item['s_category_url'] = 'https://channel.jd.com/{}.html'.format(s_category_info[0])
                        # print('小分类', s_category_info)
                        print(item)
                        yield item
                    elif s_category_info[0].count('-')==2:
                        c=re.sub('-',',',s_category_info[0])
                        item['s_category_url'] = 'https://list.jd.com/list.html?cat={}'.format(c)
                        # print('小分类',s_category_info)
                        print(item)
                        yield item





