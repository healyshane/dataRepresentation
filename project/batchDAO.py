import mysql.connector

class BatchDAO:
    db=""

    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass",
        database="datarepresentation"
    )

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into batch (batch, yield, time) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from batch"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDict(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from batch where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
 
    def update(self, values):
        cursor = self.db.cursor()
        sql="update batch set batch= %s, yield=%s, time=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from batch where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDict(self,result):
        colnames=['id','batch','yield','time']
        item ={}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item

    

batchDAO = BatchDAO()