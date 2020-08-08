# import pymysql
#
# class DBase():
#
#     def serch_data(self,SQL):
#
#
#         config = {#组装一个数据库连接的字典
#             'host': '192.168.1.178',
#             'port': 3306,
#             'user': 'root',
#             'password': '',
#             'db': 'test',
#             'charset': 'utf8mb4',
#             'cursorclass': pymysql.cursors.DictCursor
#         }
#         db = pymysql.connect(**config)
#         cur = db.cursor()#创建一个游标对象
#         sql = SQL
#         cur.execute(sql)
#         return cur.fetchall()

