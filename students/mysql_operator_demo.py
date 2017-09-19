#coding=utf8
import pandas as pd
from sqlalchemy import create_engine

######### 读操作 #############
# 初始化引擎，数据库为远程数据库mysql+pymysql://用户名：密码@IP：端口/数据库名称?字符集
engine = create_engine('mysql+pymysql://xx:xx*@xxxx:xx/wendy?charset=utf8')
# 数据库读操作
df = pd.read_sql('L网基站级工参', engine)
# 保存到本地
df.to_csv('my_table.csv', index=None)

######### 写操作 #############
# 初始化引擎，数据库为本地数据库，用户名、密码和数据库名称参照自己的设定
engine_local = create_engine('mysql+pymysql://root:1@localhost/test?charset=utf8')
# 本地文件读操作
# 取“经度”和“纬度”两个字段
# 如果取包含中文字段，下面的to_sql会报错，可先创建表，设定表字符集后便可
# alter table <表名> character set utf8;
# alter table <表名> change <字段名> <字段名> <类型> character set utf8;
df = pd.read_csv('my_table.csv', encoding='utf-8')[['经度','纬度']]
# 本地数据库写操作
df.to_sql('myTable', engine_local, index=False, if_exists='append')