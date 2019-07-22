from tkinter import *
root=Tk()
def display(t):
    global s1
    s1=s.get()+t
    s.set(s1)
def display1():
    global s1
    s1=''
    s.set(s1)
def Result():
    global s1
    s1=s.get()
    s1=str(eval(s1))
    s.set(s1)
s1=''
s=StringVar()
root.title("Calculator")
f0=Frame(root,bg='white')
f1=Frame(root,bg='white')
f2=Frame(root,bg='white')
f3=Frame(root,bg='white')
f4=Frame(root,bg='white')
f5=Frame(root,bg='white')
e1=Entry(f0,textvariable=s,bg='lightyellow',fg='black',bd=5,justify='right',font=('arial',20,'bold'),relief=RAISED)
e1.pack(fill=BOTH,expand=YES,padx=5,pady=5)
for i in 'C':
    b=Button(f1,text=i,bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=display1)
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '/':
    b=Button(f1,text=i,bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '789*':
    b=Button(f2,text=i,bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '456-':
    b=Button(f3,text=i,bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '123+':
    b=Button(f4,text=i,bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '%0.':
    b=Button(f5,text=i,bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

b=Button(f5,text='=',bg='lightyellow',fg='black',bd=5,font=('arial',20,'bold'),relief=RAISED,command=Result)
b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
f0.pack(fill=BOTH,expand=YES)
f1.pack(fill=BOTH,expand=YES)
f2.pack(fill=BOTH,expand=YES)
f3.pack(fill=BOTH,expand=YES)
f4.pack(fill=BOTH,expand=YES)
f5.pack(fill=BOTH,expand=YES)
root.mainloop()