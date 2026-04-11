import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="chetan1821",
    database="22dec_python"
)
cursor=con.cursor()
# cursor.execute("create database 22dec_python")
# qry = "create table student (id int primary key, name varchar(20),email varchar(20))"
qry = "insert into student values (2,'jagdish','JP78@gmail.com')"
cursor.execute(qry)
con.commit()
cursor.close()
con.close()


