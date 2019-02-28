import requests,json,time
from utils import dbmysql

def fxh():
    try:
        for i in range(1,26): 
            print(i)
            url = "https://dncapi.feixiaohao.com/api/coin/web-coinrank?page=%s&type=0&pagesize=100&webp=1"%i
            a = requests.get(url=url).content.decode()
            b = json.loads(a)
            c = b["data"]
            for cc in c:
                fullname = "%s-%s"%(cc["name"],cc["fullname"])
                print(fullname)
                price = cc["current_price"]
                inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                opentime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                sql = "SELECT * FROM feixiaohao where fullname ='%s'"%fullname
                a = dbmysql.first(sql)
                if a == None:
                    sql = "INSERT INTO feixiaohao(fullname,price,inserttime,opentime) VALUES ('%s','%s','%s','%s')"%(fullname,price,inserttime,opentime)
                    dbmysql.execute(sql)
                else:
                    sql = "UPDATE feixiaohao SET price = '%s',opentime = '%s' WHERE fullname =  '%s'"%(price,opentime,fullname)
                    dbmysql.execute(sql)
    except Ellipsis as e:
        print(e)


if __name__ == '__main__':
    time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(time1)
    fxh()
    time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(time2)