# -*- coding: utf-8 -*-

from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from mysql_conn import session

# Model基类,创建了一个BaseModel类,这个类的子类可以自动与一个表关联
Base = declarative_base()
# 这样设置以后直接可以通过model类进行query查询,否则必须通过session进行查询。
Base.query = session.query_property()

class Log(Base):
    '''
    对应数据库中的表
    '''
    __tablename__ = 'log'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    insert_time = Column(DateTime, nullable=False, default=datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.now())
    path = Column(String(128), nullable=False)
    log_number = Column(Integer, nullable=False)

    def getSelf(self):
        return '['+str(self.id) + '-' + self.name + '-' + str(self.insert_time) + '-' + str(self.update_time) + '-' + self.path + '-' + str(self.log_number)+']'
