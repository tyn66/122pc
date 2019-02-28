from peewee import MySQLDatabase, Model, CharField

# py_peewee连接的数据库名
db = MySQLDatabase('feixiaohao', host='127.0.0.1', user='root', passwd='123456', charset='utf8', port=3306)


class BaseModel(Model):
    class Meta:
        database = db  # 将实体与数据库进行绑定


class feixiaohao(BaseModel):  # 继承自BaseModel，直接关联db，并且也继承了Model。Model有提供增删查改的函数
    fullname = CharField(max_length=255)
    price = CharField(max_length=255)
    inserttime = CharField(max_length=255)#插入时间
    opentime = CharField(max_length=255)#修改时间


# TODO 创建table
try:
    feixiaohao.create_table()
except Ellipsis as e:
    print(e)

