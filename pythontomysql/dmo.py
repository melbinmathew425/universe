import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminar",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
f=open("df","r")
for line in f:
    data=line.rstrip("\n").split(",")
    sql="insert into person(name,place,mob) values(%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()