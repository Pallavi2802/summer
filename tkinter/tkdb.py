from tkinter import *
from tkinter import messagebox
import pymysql as sql
root = Tk()

f1 = Frame(root)
f1.pack()

l1 = Label(f1,text="Enter your username",fg="#2E86C1")
l1.config(font=(None,20,'italic'))
l1.grid(row=0,column=0)
e1 = Entry(f1)
e1.grid(row=0,column=1)
l2 = Label(f1,text="Enter your password",fg="#2E86C1")
l2.config(font=(None,20,"italic"))
l2.grid(row=1,column=0)
e2 = Entry(f1,show="*")
e2.grid(row=1,column=1)
def submit():
    #print(e1.get())
    #print(e2.get())
    user = e1.get()
    password = e2.get()
    db = sql.connect(host="localhost",port=3306,user="root",password="",database="internbatch2")
    c = db.cursor()
    cmd = "select * from user where username = '{}'".format(user)
    c.execute(cmd)
    data = c.fetchone()
    if data:
        if password == data[1]:
            messagebox.showinfo("INFO","WELCOME")
        else:
            messagebox.showerror("ERROR","PASSWORD DOES NOT MATCH")
    else:
        messagebox.showerror("Error","USER DOES NOT EXIST")
    text = "Welcome user " + e1.get()
    l3.configure(text=text)
b1 = Button(f1,text="SUBMIT",fg="red",bg="black",height=2,width=5,command=submit)
b1.grid(row=2,column=0,columnspan=3)
l3 = Label(f1,text='Welcome user',fg="red")
l3.config(font=(None,30,"bold"))
l3.grid(row=3,column=0)


root.mainloop()