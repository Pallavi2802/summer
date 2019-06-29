from tkinter import *
from tkinter import messagebox
root = Tk()

class Buttons:
    def __init__(self,master):
        self.master = master
        f1 = Frame(master)
        f1.pack()

        self.b1 = Button(f1,text="Button1",command=self.show)
        self.b1.pack()
        self.l1 = Label(f1,text="This is label1",fg="red")
        self.l1.config(font=(None,30,'bold'))
        self.l1.pack()
        self.b2 = Button(f1,text="Exit",height=3,width=7,command=master.destroy)
        self.b2.pack()
    def show(self):
        messagebox.showinfo("INFO","GOOD YOU ARE WELCOME")

b1 = Buttons(root)
root.mainloop()