# coding:utf8
import pymysql
import config


def singleton(cls, *args, **kwargs):
    """线程不安全的单例类"""
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class MysqlHelper(object):

    def __init__(self):
        self.host = config.mysql['host']
        self.user = config.mysql['user']
        self.passwd = config.mysql['passwd']
        self.dbName = config.mysql['dbName']

    def connect(self):
        # print('connect----------------')
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName)
        self.cursor = self.db.cursor()
        pass

    def close(self):
        # print('close +++++++++++++++++')
        self.cursor.close()
        self.db.close()
        pass

    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print('get_one query failed 33 !!!!!  %s' % e)
        return res

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print('__edit failed')
            self.db.rollback()
        return count

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print('get_all query failed!! %s ' % e)
        return res
