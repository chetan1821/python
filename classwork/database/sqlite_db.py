import sqlite3
con = sqlite3.connect("data.db")

# qry = """
# create table employee (
# emp_id int,
# emp_name varchar(20),
# emp_email varchar(20),
# emp_address varchar(20)
# )
# """
qry = """
insert into employee (emp_id,emp_name,emp_email,emp_address) values 
(2,"chetan","cp12@gmail.com","surat")
"""
con.execute(qry)
con.commit
print("one row inserted...")