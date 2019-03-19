# -*- coding: utf-8 -*-
class Conf(object):
    MYSQL = {
        'host': '127.0.0.1',  # 换成你自己的ip地址
        'port': 3306,         # 换成你自己的端口号，以下也一样
        'username': 'bigdata',
        'password': 'bigdata',
        'database': 'logdb'
    }

def get_config(section, option):
    try:
        config = Conf()
        return getattr(config, section)[option]
    except AttributeError:
        print 'section {0} is not available!'.format(section)
    except KeyError:
        print 'option {0} is not available!'.format(option)
