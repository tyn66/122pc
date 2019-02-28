import pymysql
'''
操作mysql第一步：创建连接，返回连接对象和游标
'''
# host = "192.168.50.95"#本地的ip地址
host = "127.0.0.1"#本地的ip地址
port = 3306#端口号
user = "root"#数据库的用户名
# passwd = "19970210cqm"#数据库的密码
passwd="123456"
# db = '远程专用库'#你要连接的数据库名称
db='feixiaohao'
#-----------------------------------------
def getConnection():
    try:
        #连接数据库
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, charset="utf8", db=db)
        #设置游标
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print(e)
        return None
#-----------------------------------------
#TODO 第二步：创建增删改的方法，此方式用于insert、update、delete,create,alter
#-----------------------------------------
def execute(sql):
    # 获取连接
    conn, cur = getConnection()
    try:
        #开启事物
        conn.begin()
        # 游标执行sql语句
        cur.execute(sql)
        # 连接进行事务提交
        conn.commit()
        # 如果程序执行无误，返回True
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cur.close()
        conn.close()

def execute2(sql):
    conn,cur=getConnection()
    try:
        #开启事物
        conn.begin()
        # 游标执行sql语句
        for item in sql:
            cur.execute(item)
        # 连接进行事务提交
        conn.commit()
        # 如果程序执行无误，返回True
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cur.close()
        conn.close()
def executeMany(sql, values):
    # 获取连接
    conn, cur = getConnection()
    try:
        # 游标执行sql语句
        cur.executemany(sql, values)
        # 连接进行事务提交
        conn.commit()
        # 如果程序执行无误，返回True
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cur.close()
        conn.close()

'''
第三步：创建返回第一条数据方法，此方式用于select one
'''
def first(sql):
    # 获取连接
    conn, cur = getConnection()
    try:
        # 游标执行sql语句
        cur.execute(sql)
        # fetchone
        rs = cur.fetchone()
        # 连接进行事务提交
        conn.commit()
        # 如果程序执行无误，返回True
        return rs
    except Exception as e:
        print(e)
        return False
    finally:
        cur.close()
        conn.close()


'''
第四步：创建返回所有数据方法
'''


def fetchall(sql):
    # 获取连接
    conn, cur = getConnection()
    try:
        # 游标执行sql语句
        cur.execute(sql)
        # fetchone
        rs = cur.fetchall()
        # 连接进行事务提交
        conn.commit()
        # 如果程序执行无误，返回True
        return rs
    except Exception as e:
        print(e)
        return False
    finally:
        cur.close()
        conn.close()

