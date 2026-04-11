import mysql.connector as sql

con=sql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="chetan1821",
    database="22dec_python"
)
cursor=con.cursor()
# qry = "create table student_db (id int primary key, name varchar(20),email varchar(20))"
def add_data():
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    email=input("Enter email : ")
    qry = "INSERT INTO student_db (id, name, email) VALUES (%s, %s, %s)"
    
    values = (id, name, email)

    cursor.execute(qry, values)
    con.commit()   # 🔥 must for saving data

    print("✅ Data inserted successfully")

add_data()

cursor.close()
con.close()



