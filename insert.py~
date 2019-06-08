import sqlite3 as sql
db=sql.connect("Student.db")
c=db.cursor()
#cmd="create table student(name varchar(20),address varchar(30),course varchar(40),phoneno varchar(20))"
#c.execute(cmd)
while True:
    name=input("enter your name : ")
    address=input("Enter your address : ")
    course=input("Enter your course : ")
    phoneno=input("Enter your no : ")
    cmd = " insert into student values('{}','{}','{}','{}') ".format(name,address,course,phoneno)
    c.execute(cmd)
    db.commit()
    choice=input("Do you want to continue (yes/no) : ")
    if choice.strip().lower() == "no" :
        break
