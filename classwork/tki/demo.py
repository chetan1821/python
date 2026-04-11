from tkinter import *
import mysql.connector as sql
con=sql.connect(
    host="localhost",
    port ="3306",
    user="root",
    password = "chetan1821",
    database="22dec_python"
)
cursor = con.cursor()

root = Tk()

root.geometry("400x400")
root.title("MyApp")

# b1=Button(root,text="Right").pack(side=RIGHT)
# b1=Button(root,text="Left").pack(side=LEFT)
# b1=Button(root,text="Top").pack(side=TOP)
# b1=Button(root,text="Bottom").pack(side=BOTTOM)

# Using Grid....

# l1=Label(root,text="User name : ").grid(row=0,column=0)
# l1=Label(root,text="Email : ").grid(row=1,column=0)
# l1=Label(root,text="phone : ").grid(row=2,column=0)

# t1=Entry(root).grid(row=0,column=1)
# t1=Entry(root).grid(row=1,column=1)
# t1=Entry(root).grid(row=2,column=1)

# b1 = Button(root,text="Submit").grid(row=3,column=1)
# ===============
# using place

def add():
    uname = t1.get()
    email = t2.get()
    phone = t3.get()
    cursor.execute(f"insert into reg(uname,email,phone) values('{uname}','{email}','{phone}')")

    con.commit()
    print("Data inserted")
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)

    

l1=Label(root,text="User name : ").place(x=100,y=100)
l2=Label(root,text="Email : ").place(x=100,y=150)
l3=Label(root,text="phone : ").place(x=100,y=200)

t1=Entry(root)
t1.place(x=200,y=100)
t2=Entry(root)
t2.place(x=200,y=150)
t3=Entry(root) 
t3.place(x=200,y=200)



b1 = Button(root,text="Submit",width=15,command=add).place(x=200,y=250)
    
root.mainloop()