import pymysql as sql
db=sql.connect(host="localhost",port=3306,database="internshipbatch",user="pallavi",password='password')
c=db.cursor()
while True:
    name=input("enter your name : ")
    address=input("enter your address : ")
    course=input("enter your course : ")
    Dob=input("enter your date of birth :")
    phoneno=int(input("enter your phone no : "))
    cmd="insert into student(name,address,course,Dob,phoneno)values('{}','{}','{}','{}',{})".format(name,address,course,Dob,phoneno)
    c.execute(cmd)
    print("data inserted")
    db.commit()
    ch=input("do you want to continue").lower().strip()
    if ch == "no":
        break
