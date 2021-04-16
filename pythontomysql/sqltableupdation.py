import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminar",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
sql="update employee set salary=10000 where eid=1000"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()