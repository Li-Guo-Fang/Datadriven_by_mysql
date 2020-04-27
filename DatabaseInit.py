import pymysql
from MysqlDataDriven.Sql import *

class DataBaseInit(object):

    def __init__(self, host, port, dbName, username, password, charset):
        self.host = host
        self.port = port
        self.db = dbName
        self.user = username
        self.passwd = password
        self.charset = charset

    def create(self):
        try:

            conn = pymysql.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )

            cur = conn.cursor()


            cur.execute(create_database)

            conn.select_db("test")


            cur.execute(drop_table_if_exist_sql)
            cur.execute(create_table)
        except pymysql.Error as e:
            raise e
        else:

            cur.close()
            conn.commit()
            conn.close()
            print (u"创建数据库及表成功")

    #插入数据
    def insertDatas(self):
        try:
            conn = pymysql.connect(
                host = self.host,
                port = self.port,
                db = self.db,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )
            cur = conn.cursor()
            #插入数据语句
            sql = "insert into test_case(bookname, author) values(%s, %s);"
            res = cur.executemany(sql, [('Selenium WebDriver实战宝典', '吴晓华'),
                                  ('HTTP权威指南', '古尔利'),
                                  ('探索式软件测试', '惠特克'),
                                  ('暗时间', '刘未鹏')])
        except pymysql.Error as e:
            raise e
        else:
            conn.commit()
            print (u"初始数据插入成功")
            cur.execute("select * from test_case;")
            for i in cur.fetchall():
                print (i[1], i[2])
            cur.close()
            conn.close()


if __name__ == '__main__':
    db = DataBaseInit(
        host="localhost",
        port=3306,
        dbName="test",
        username="root",
        password="123456",
        charset="utf8"
    )
    db.create()
    db.insertDatas()
    print (u"数据库初始化结束")