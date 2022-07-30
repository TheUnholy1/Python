from tkinter import *

root = Tk()
root.title("Basic Arithmetic Calculator")
root.geometry("500x300")
fs = "Verdana 15"
n1, n2, ans = StringVar(), StringVar(), StringVar()


def Add():
    a = int(n1.get())
    b = int(n2.get())
    c = a + b
    ans.set(c)

def Minus():
    a = int(n1.get())
    b = int(n2.get())
    c = a - b
    ans.set(c)


def Multiply():
    a = int(n1.get())
    b = int(n2.get())
    c = a * b
    ans.set(c)


def Divide():
    a = int(n1.get())
    b = int(n2.get())
    c = a / b
    ans.set(c)


def Clear():
    n1.set("")
    n2.set("")
    ans.set("")


l1 = Label(root, text="Enter a number:", font=fs)
l1.grid(row=0, column=0)
t1 = Entry(root, justify=RIGHT, font=fs, textvariable=n1)
t1.grid(row=0, column=1, columnspan=4)
l2 = Label(root, text="Enter a number:", font=fs)
l2.grid(row=1, column=0)
t2 = Entry(root, justify=RIGHT, font=fs, textvariable=n2)
t2.grid(row=1, column=1, columnspan=4)
b1 = Button(root, justify=RIGHT, font=fs, text="+", width=5, command=Add)
b1.grid(row=2, column=1)
b2 = Button(root, justify=RIGHT, font=fs, text="-", width=5,command = Minus)
b2.grid(row=2, column=2)
b3 = Button(root, justify=RIGHT, font=fs, text="x", width=5, command=Multiply)
b3.grid(row=2, column=3)
b4 = Button(root, justify=RIGHT, font=fs, text="/", width=5, command=Divide)
b4.grid(row=2, column=4)
l3 = Label(root, text="The answer is", font=fs)
l3.grid(row=3, column=0)
t3 = Entry(root, justify=RIGHT, font=fs, state=DISABLED, textvariable=ans)
t3.grid(row=3, column=1, columnspan=4)
b5 = Button(root, justify=RIGHT, font=fs, text="CLEAR", width=20, command=Clear)
b5.grid(row=4, column=1, columnspan=4)
root.mainloop()
