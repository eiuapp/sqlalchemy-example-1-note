# -*- coding: utf-8 -*-

from mysql_models import Log
from mysql_dao import MysqlDao
from datetime import datetime

if __name__ == "__main__":

    log1 = Log(name="aa", insert_time=datetime.now(), update_time=datetime.now(), path='aa-path', log_number=10)
    log2 = Log(name="bb", insert_time=datetime.now(), update_time=datetime.now(), path='bb-path', log_number=22)
    element_list = [log1, log2]

    mysql_dao = MysqlDao()
    mysql_dao.initDB()      # 测试initDB方法,初始化数据库

    mysql_dao.insertLogtBulk(element_list, 20, "Log")
    # print mysql_dao.insertBatch(element_list)   # 测试插入方法
