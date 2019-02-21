import pymysql
from readConfig import ReadConfig
from balance import Balance
import traceback
mysql = ReadConfig()


#db = MySQLdb.connect(host,user,passwd,database,charset="utf8")

class MysqlTool:
    def __init__(self):
        self.host = mysql.Database("host")
        self.user = mysql.Database("user")
        self.passwd = mysql.Database("passwd")
        self.database = mysql.Database("database")
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.database,charset="utf8")

    def user_id(self):
        cursor = self.db.cursor()
        sql = mysql.Mysql("user_id")
        cursor.execute(sql)                    #db.commit()提交到数据库执行
        data = cursor.fetchone()               #cursor
        return data

    def check_balance(self, balance_id, stock_symbol, created_at):
        cursor = self.db.cursor()
        sql = "select count(id ) from history where (rebalancing_id = %s) or (stock_symbol = %s and created_at = %s)"
        cursor.execute(sql, (balance_id, stock_symbol, created_at))
        data = cursor.fetchone()
        return data[0]

    def save_balance(self, balance):
        cursor = self.db.cursor()
        sql = "insert into history(account_id, created_at, net_value, prev_net_value, prev_price, prev_target_volume, prev_target_weight, prev_volume, prev_weight, prev_weight_adjusted, price, proactive, rebalancing_id, stock_id, stock_name, stock_symbol, target_volume, target_weight, volume, weight) " \
              " values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (balance.account_id, balance.created_at, balance.net_value, balance.prev_net_value, balance.prev_price, balance.prev_target_volume, balance.prev_target_weight, balance.prev_volume, balance.prev_weight, balance.prev_weight_adjusted, balance.price, balance.proactive, balance.rebalancing_id, balance.stock_id, balance.stock_name, balance.stock_symbol, balance.target_volume, balance.target_weight, balance.volume, balance.weight))
            self.db.commit()
        except Exception as e:
            print(traceback.print_exc())
            self.db.rollback()

    def query_accounts(self):
        cursor = self.db.cursor()
        sql = "select * from account"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def query_latest_history(self, account_id):
        cursor = self.db.cursor()
        print(account_id)
        sql = "select created_at from history where account_id = %s order by created_at desc limit 0, 1"
        cursor.execute(sql, account_id)
        data = cursor.fetchone()
        return data