# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker
import mysql_config as mc

# 数据库连接
conn_url = URL(
    drivername='mysql',
    username=mc.get_config('MYSQL', 'username'),
    password=mc.get_config('MYSQL', 'password'),
    host=mc.get_config('MYSQL', 'host'),
    port=mc.get_config('MYSQL', 'port'),
    database=mc.get_config('MYSQL', 'database'),
    query={'charset': 'utf8'}
)

#返回一个数据库引擎,echo参数为true时,会显示每条执行的sql语句,生产环境下可关闭
engine = create_engine(conn_url, encoding='utf-8', echo=False)
"""
sessionmaker会生成一个数据库会话类,实例可当成一个数据库链接,同时记录了一些查询的数据,
并决定什么时候执行sql.scoped_session保证每个线程获得的session对象是唯一的.
"""
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
