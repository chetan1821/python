from tkinter import *
from tkinter import ttk
import mysql.connector as sql

# ================= DB CONNECTION =================
con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="chetan1821",
    database="22dec_python"
)

Cursor = con.cursor()

# ================= WINDOW =================
root = Tk()
root.geometry("950x700")
root.title("Registration System")


# ================= FUNCTIONS =================

# -------- INSERT --------
def add():
    Cursor.execute(
        "INSERT INTO regtriation(uname,uemail,uphone,upwd,uaddress) VALUES(%s,%s,%s,%s,%s)",
        (t1.get(), t2.get(), t3.get(), t4.get(), t5.get())
    )
    con.commit()
    show_data()
    clear()


# -------- SHOW DATA --------
def show_data():
    Cursor.execute("SELECT * FROM regtriation")
    rows = Cursor.fetchall()

    for i in table.get_children():
        table.delete(i)

    for row in rows:
        table.insert("", END, values=row)


# -------- SELECT ROW --------
def select_row(event):
    selected = table.focus()
    values = table.item(selected, "values")

    if values:
        clear()
        t1.insert(0, values[1])
        t2.insert(0, values[2])
        t3.insert(0, values[3])
        t4.insert(0, values[4])
        t5.insert(0, values[5])


# -------- UPDATE --------
def update_data():
    selected = table.focus()
    values = table.item(selected, "values")

    if values:
        uid = values[0]
        Cursor.execute("""
        UPDATE regtriation 
        SET uname=%s,uemail=%s,uphone=%s,upwd=%s,uaddress=%s
        WHERE uid=%s
        """,(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),uid))

        con.commit()
        show_data()
        clear()


# -------- DELETE --------
def delete_data():
    selected = table.focus()
    values = table.item(selected, "values")

    if values:
        uid = values[0]
        Cursor.execute("DELETE FROM regtriation WHERE uid=%s",(uid,))
        con.commit()
        show_data()
        clear()


# -------- SEARCH --------
def search_data():
    Cursor.execute("SELECT * FROM regtriation WHERE uname LIKE %s",("%"+t1.get()+"%",))
    rows = Cursor.fetchall()

    for i in table.get_children():
        table.delete(i)

    for row in rows:
        table.insert("", END, values=row)


# -------- CLEAR --------
def clear():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)


# ================= LABELS =================
Label(root,text="User name").place(x=100,y=50)
Label(root,text="Email").place(x=100,y=100)
Label(root,text="Phone").place(x=100,y=150)
Label(root,text="Password").place(x=100,y=200)
Label(root,text="Address").place(x=100,y=250)

# ================= ENTRIES =================
t1=Entry(root); t1.place(x=200,y=50)
t2=Entry(root); t2.place(x=200,y=100)
t3=Entry(root); t3.place(x=200,y=150)
t4=Entry(root); t4.place(x=200,y=200)
t5=Entry(root); t5.place(x=200,y=250)

# ================= BUTTONS =================
Button(root,text="Submit",width=12,command=add).place(x=200,y=300)
Button(root,text="Update",width=12,command=update_data).place(x=300,y=300)
Button(root,text="Delete",width=12,command=delete_data).place(x=400,y=300)
Button(root,text="Search",width=12,command=search_data).place(x=500,y=300)
Button(root,text="Show All",width=12,command=show_data).place(x=600,y=300)

# ================= TABLE =================
table = ttk.Treeview(root)

table["columns"]=("id","name","email","phone","pwd","address")

table.column("#0",width=0,stretch=NO)
table.column("id",width=50)
table.column("name",width=120)
table.column("email",width=180)
table.column("phone",width=120)
table.column("pwd",width=120)
table.column("address",width=180)

table.heading("id",text="ID")
table.heading("name",text="Name")
table.heading("email",text="Email")
table.heading("phone",text="Phone")
table.heading("pwd",text="Password")
table.heading("address",text="Address")

table.place(x=50,y=380)

table.bind("<ButtonRelease-1>",select_row)

root.mainloop()