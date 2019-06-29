from tkinter import *
from random import randint
from tkinter import messagebox
root = Tk()

class Guessnum:
    def __init__(self,master):
        self.master = master
        self.count = 0
        self.num = randint(1,100)
        self.l1 = Label(master,text="Choose a number between 1 to 100",fg="red",bg="black")
        self.l1.config(font=(None,20,'bold'))
        self.l1.pack()
        self.e1 = Entry(master)
        self.e1.pack()
        self.b1 = Button(master,text="SUBMIT",height=2,width=10,fg="red",bg="yellow",command=self.submit)
        self.b1.pack()

    def submit(self):
        var = int(self.e1.get())
        self.count += 1
        if self.count == 5:
            messagebox.showinfo("INFO","NO MORE CHANCES..")
            self.b1.configure(state=DISABLED)
        else:
            if var == self.num:
                self.l1.configure(text="You won....")
                messagebox.showinfo("INFO","YOU WON")
                self.b1.configure(state=DISABLED)
            elif var<self.num:
                self.l1.configure(text="THINK HIGH...")
            else:
                self.l1.configure(text="THINK LOW....")

guess = Guessnum(root)
root.mainloop()