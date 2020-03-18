# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the item_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DouBan.models import Big_tag,Small_tag,Book_Details,BookToTag


class DoubanPipeline(object):

    def process_item(self, item, spider):
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/dbbook?charset=utf8')
        # 创建DBSession类型:
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        try:
            print(item)
            bigtag=item.pop('big_name')
            smltaglist = item.pop('smal_name_list')
    
            if not session.query(Big_tag).filter_by(big_tag=bigtag).first():
    
                Bigtag=Big_tag(big_tag=bigtag)
    
                session.add(Bigtag)
                # 把数据提交给数据库
                session.commit()
                print(Bigtag.id)
                for sml_tag in smltaglist:
                    Smalltag=Small_tag(sml_tag=sml_tag,btag_id=Bigtag.id)
                    session.add(Smalltag)
                session.commit()
    
    
            offset=item.pop('offset')
            sml_tag=item.pop('sml_tag')
            smltag=session.query(Small_tag).filter_by(sml_tag=sml_tag).first()
            session.add(Book_Details(**item))
            session.commit()
            session.add(BookToTag(smltag_id=smltag.id,book_isbn=item['ISBN']))
    
    
            session.commit()
        except Exception:
            print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',Exception)

        finally:
            session.close()
        return item




