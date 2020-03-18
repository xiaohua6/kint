from sqlalchemy import Column, String, Index,Integer,Float,DateTime,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    __table_args__={
        'mysql_engine':'innoDB',
        'mysql_charset':'utf8'
    }

class Book(Base):
    __tablename__='book'
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False)

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://mysql:mysql@localhost:3306/student1')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)