import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="demo",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
sql="insert into student(rollno,name,mark) values(1001,'anu',198)"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()

