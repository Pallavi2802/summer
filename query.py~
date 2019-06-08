import sqlite3 as sql
db=sql.connect("student.db")
c=db.cursor()
cmd="select * from student"
d=c.execute(cmd)
data=c.fetchall()
print(data)
for var in data:
    print("name ",var[0])
    print("address",var[1])
    print("course ",var[2])
    print("phoneno",var[3])

