import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native"
)
cursor=db.cursor()
sql="select vertion()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()

