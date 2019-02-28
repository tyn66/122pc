from utils import dbmysql
import csv
import codecs

def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f)
        sql = 'select * from feixiaohao'
        results = dbmysql.fetchall(sql=sql)
        a = ('id','fullname','price')
        write.writerow(a)
        c = 0
        for result in results:
            b = (result[0],result[1],result[2])
            c +=1
            print(b)
            write.writerow(b)
        print(c)
if __name__ == '__main__':
  ddd = "2.csv"
  read_mysql_to_csv(ddd)
  print('11111')