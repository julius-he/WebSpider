import pymssql

class SQLManager:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    # 连接数据库
    def connect(self):
        # 获取数据库连接对象
        connection = pymssql.connect(
            host = self.host,
            user = self.user,
            password = self.pwd,
            database = self.db,
            charset = "utf8"
        )
        # 作为SQLManager对象的属性使用，在该对像断开连接前都能使用
        self.connection = connection

    # 查询
    def query(self, sqlCommand):
        # 通过连接对象获取游标
        cursor = self.connection.cursor()
        # 执行sql命令
        cursor.execute(sqlCommand)
        # 获取所有查询结果
        dataList = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 返回查询结果
        return dataList

    # 操作
    def operate(self, sqlCommand):
        # 通过连接对象获取游标
        cursor = self.connection.cursor()
        # 执行sql命令
        cursor.execute(sqlCommand)
        # 提交事务
        self.connection.commit()
        # 关闭游标
        cursor.close()

    # 关闭连接
    def closeConnet(self):
        # 调用连接对象的close方法，断开连接
        self.connection.close()
        # 将SQLManager对象的connection属性置空
        self.connection = None