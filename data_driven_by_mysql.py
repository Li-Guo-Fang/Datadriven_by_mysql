from selenium import webdriver
import time
import datetime
from openpyxl import *
import pymysql


def get_test_data():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="123456",
        db="test",
        charset="utf8"
    )

    # 使用cursor()方法获取数据库的操作游标
    cursor = conn.cursor()

    cursor.execute("select * from test_case;")
    resSet = cursor.fetchall()
    print(u"共%s条数据。" % len(resSet))
    print(resSet)


    cursor.close()
    conn.commit()
    conn.close()
    return resSet


def update_test_result(data, result):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="123456",
        db="test",
        charset="utf8"
    )

    cursor = conn.cursor()    #获取游标
    print('update test_case set test_result="' + result + '" where bookname="' + data + '";')
    update = cursor.execute('update test_case set test_result="' + result + '" where bookname="' + data + '";')

    print(u"修改语句受影响的行数：", update)
    cursor.close()
    conn.commit()
    conn.close()


driver = webdriver.Ie(executable_path="d:\\IEDriverServer")
test_result = []
for data in get_test_data():
    try:
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys(data[1])
        driver.find_element_by_id("su").click()
        time.sleep(3)
        assert data[2] in driver.page_source
        update_test_result(data[1], u"成功")
    except AssertionError as e:
        print(data[2] + u"断言失败")
        update_test_result(data[1], u"断言失败")
    except Exception as e:
        print(e)
        print(data[1] + u"测试执行出现异常")
        update_test_result(data[1], u"执行出现异常")

driver.quit()