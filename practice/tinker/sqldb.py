
import sqlite3

con = sqlite3.connect("data.db")
# qry = "create table student(id int primary key, name varchar(10),email varchar(20))"
# qry = "insert into student values(3,'chetan','cp78@gmail.com'),(2,'jagdish','jp78@gmail.com')"
# qry= "update student set email='Ashish@gmail.com' where id=3"
# qry = "delete from student where id =2"
# con.execute(qry)
# con.commit()

data = con.execute("select * from student")
# print(data.fetchall())

for i in data.fetchall():
    print(i)
