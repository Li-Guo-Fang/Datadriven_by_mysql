import pymysql
from MysqlDataDriven.DatabaseInit import DataBaseInit


class MyMySQL(object):
    def __init__(self, host, port, dbName, username, password, charset):
        # 进行数据库初始化
        dbInit = DataBaseInit(host, port, dbName, username, password, charset)
        dbInit.create()
        dbInit.insertDatas()
        self.conn = pymysql.connect(
            host = host,
            port = port,
            db = dbName,
            user = username,
            passwd = password,
            charset = charset
        )
        self.cur = self.conn.cursor()

    def getDataFromDataBases(self):

        # 从test_case表中获取需要的测试数据
        # bookname作为搜索关键词，author作为预期关键词
        self.cur.execute("select bookname, author from test_case;")

        # 从查询区域取回所有查询结果
        datasTuple = self.cur.fetchall()
        return datasTuple

    def closeDatabase(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    db = MyMySQL(
        host="localhost",
        port=3306,
        dbName="test",
        username="root",
        password="123456",
        charset="utf8"
    )
    print (db.getDataFromDataBases())