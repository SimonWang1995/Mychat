import pymysql

class Mysql(object):
    def __init__(self, host, user,  database, password=None, port=3306):
        conn = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
        self.cursor = conn.cursor()

    def runsql(self,cmd):
        try:
            self.cursor.execute(cmd)
        except Exception as e:
            print(e)

    def fechone(self):
        try:
            res = self.cursor.fetchone()
            return res
        except:
            pass

    def verify(self, user, passwd):
        return  True
