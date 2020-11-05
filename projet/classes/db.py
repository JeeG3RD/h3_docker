import mysql.connector

class DB:
    def __init__(self, user, pwd, host):
        self.user = user
        self.pwd = pwd
        self.host = host

    def connect(self):
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.pwd
        )

        self.cursor = self.con.cursor()

    def connect_db(self, db):
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.pwd,
            database=db
        )

        self.cursor = self.con.cursor()

    def createDB(self):
        sql = open("sql/db_create.sql", mode='r', encoding='utf-8-sig').read()
        self.cursor.execute(sql)

        self.connect_db("nasa")

    def importData(self):
        sql = open("sql/db_insert_data.sql", mode='r', encoding='utf-8-sig').read()
        self.cursor.execute(sql)

    def execQuery(self, query):
        self.cursor.execute(query)
        self.con.commit()

    def exportData(self, table):
        self.cursor.execute("Select * from " + table)
        return self.cursor.fetchall()

    def getColumns(self, table):
        field_names = [i[0] for i in self.cursor.description]
        
        return field_names


    
    