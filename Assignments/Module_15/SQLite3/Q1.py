import sqlite3
con=sqlite3.connect("company_db.db")
# query="create table employee (emp_id INTEGER PRIMARY KEY AUTOINCREMENT,emp_name varchar(20),emp_dept varchar(20),emp_email varchar(20),salary int(11))"
# query = """
# INSERT INTO employee (emp_name, emp_dept, emp_email, salary) VALUES
# ('Nikhil Koli','Electric','Nk11@gmail.com',2000),
# ('vrujal Rana','IT','vrujal789@gmail.com',5000),
# ('Parmeshwar Patil','Markting','par123@gmail.com',15000)
# """
# con.execute(query)

data= con.execute("select * from employee")
print(data.fetchall())
for i in data:
    print(i)
con.commit()
con.close()

# print("Data inserted..")