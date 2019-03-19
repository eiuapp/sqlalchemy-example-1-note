# sqlalchemy-example-1-note

https://blog.csdn.net/xsdxs/article/details/53150287 笔记


## 代码说明

```
mysql_config: 记录mysql配置的文件，运行前必须配置。 
mysql_conn: 连接模块，负责python和mysql之间的连接 
mysql_models: 模型模块，在此可以添加多个模型，用于和数据库中多张表进行“对象关系映射”。一个类对应一张表。 
mysql_dao: Python和mysql进行操作的模块，把增删改查操作都写到这个模块下，目前本文写了批量插入的两种实现方式。 
mysql_test: 测试模块，最顶层的操作都放在这里即可。
```

模块之间的关系依赖如下图所示： 

![img](https://img-blog.csdn.net/20161113174038613)
