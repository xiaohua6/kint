from sqlalchemy import Column, String, Index,Integer,Float,DateTime,create_engine,ForeignKey,UniqueConstraint
from sqlalchemy import Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20))
    __table_args__={
        'mysql_engine':'innoDB',
        'mysql_charset':'utf8'
    }
class Big_tag(Base):
    __tablename__='bigtag'
    id=Column(Integer,primary_key=True,autoincrement=True)
    big_tag=Column(String(20))
    __table_args__ = {
        'mysql_engine': 'innoDB',
        'mysql_charset': 'utf8'
    }




class Small_tag(Base):
    __tablename__ = 'smltag'
    id=Column(Integer,primary_key=True,autoincrement=True)
    sml_tag=Column(String(30))

    btag_id=Column(Integer,ForeignKey("bigtag.id"))
    __table_args__ = {
        'mysql_engine': 'innoDB',
        'mysql_charset': 'utf8'
    }




class Book_Details(Base):
    field_info_set = [('作者', 'author'), ('副标题', 'subtitle'), ('出版社', 'publish'), ('出品方', 'Producer'
                                                                                  ), ('原作名', "Org_title"),
                      ('译者', "translator"), ('出版年', "publish_date"), ('页数', "pages"), ('定价', "price"),
                      ('装帧', 'framing'), ('丛书', 'books'), ('ISBN', 'ISBN'), ('统一书号', 'ISBN')]

    __tablename__ = 'book'

    author=Column(String(30))
    publish=Column(String(30))
    Producer=Column(String(30))
    translator=Column(String(30))
    pages=Column(String(30))
    ISBN=Column(String(30),primary_key=True)
    subtitle=Column(String(30))
    book_summary=Column(Text)
    framing=Column(String(30))
    books=Column(String(30))
    price=Column(Float)
    score=Column(Float)
    author_summary=Column(Text)
    title=Column(String(30),nullable=False)
    Org_title=Column(String(30))
    publish_date=Column(DateTime)


__table_args__ = (
    # 创建联合约束title和author不能同时相同
    UniqueConstraint('title','author',name='uix_title_author'),
    Index('title','author'),
    # 存在多个key_value形式的约束时候要把他们组成一个字典放在最后
    {'mysql_engine': 'innoDB','mysql_charset': 'utf8'})

class BookToTag(Base):
    __tablename__ = 'booktotag'
    id=Column(Integer,primary_key=True,autoincrement=True)
    smltag_id=Column(Integer,ForeignKey('smltag.id'))
    book_isbn=Column(String(30),ForeignKey('book.ISBN'))


    __table_args__ = {
        'mysql_engine': 'innoDB',
        'mysql_charset': 'utf8'
    }

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/dbbook?charset=utf8')
# 创建DBSession类型:
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# 创建表的方法
def create_table(engine):
    Base.metadata.create_all(engine)

# 删除表的方法
def drop_table(engine):
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    drop_table(engine)
    create_table(engine)

    # session.add_all([User(name='cc'),User(name='dd'),User(name='ee')])
    #
    # user=session.query(User).filter_by(name='dd').first()
    # session.commit()
    #
    # print(user)
    #
    # item={'big_name': '文学 · · · · · · ', 'smal_name_list': ['小说', '外国文学', '文学', '经典', '中国文学', '随笔', '日本文学', '散文', '村上春树', '诗歌', '童话', '名著', '儿童文学', '古典文学', '余华', '王小波', '杂文', '当代文学', '张爱玲', '外国名著', '钱钟书', '鲁迅', '诗词', '茨威格', '米兰·昆德拉', '杜拉斯', '港台'], 'offset': 100, 'sml_tag': '小说', 'score': 8.8, 'title': '灿烂千阳', 'book_summary': '', 'author_summary': '', 'author': '[美]卡勒德·胡赛尼', 'subtitle': None, 'publish': '上海人民', 'Producer': '世纪文景', 'Org_title': 'AThousandSplendidSuns', 'translator': '李继宏', 'publish_date': '2007-09-01', 'pages': 428, 'price': 28.0, 'framing': '平装', 'books': '卡勒德·胡赛尼作品', 'ISBN': '9787208072107'}
    #
    # bigtag = item.pop('big_name')
    # smltaglist = item.pop('smal_name_list')
    #
    # if not session.query(Big_tag).filter_by(big_tag=bigtag).first():
    #
    #     Bigtag = Big_tag(big_tag=bigtag)
    #     session.add(Bigtag)
    #     # Bigtag=session.query(Big_tag).filter_by(big_tag=bigtag).first()
    #     session.commit()
    #     for sml_tag in smltaglist:
    #         Smalltag = Small_tag(sml_tag=sml_tag, btag_id=Bigtag.id)
    #         session.add(Smalltag)
    #
    # offset = item.pop('offset')
    # sml_tag = item.pop('sml_tag')
    # print(item)
    # smltag = session.query(Small_tag).filter_by(sml_tag=sml_tag).first()
    # session.add(Book_Details(**item))
    # session.commit()
    # print(item['ISBN'])
    # session.add(BookToTag(smltag_id=smltag.id, book_isbn=item['ISBN']))
    #
    # session.commit()

