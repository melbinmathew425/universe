import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="demo",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
sql="create table student(rollno int,name varchar(20),mark int);"
cursor.execute(sql)
db.close()