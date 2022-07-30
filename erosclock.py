from datetime import datetime
from math import factorial
import pytz
from tkinter import *
import time


def times():
    home = pytz.timezone("Hongkong")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock.config(text=current_time)
    name.config(text="Hongkong")
    clock.after(200,times)

    home = pytz.timezone("Asia/Kolkata")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock1.config(text=current_time)
    name1.config(text="India")

    home = pytz.timezone("Europe/Athens")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock2.config(text=current_time)
    name2.config(text="Europe")

    home = pytz.timezone("Canada/Pacific")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock3.config(text=current_time)
    name3.config(text="Canada")

    home = pytz.timezone("Brazil/Acre")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock4.config(text=current_time)
    name4.config(text="Brazil")

    home = pytz.timezone("Australia/ACT")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock5.config(text=current_time)
    name5.config(text="Australia")

    home = pytz.timezone("Asia/Tokyo")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock6.config(text=current_time)
    name6.config(text="Tokyo")

    home = pytz.timezone("Asia/Singapore")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock7.config(text=current_time)
    name7.config(text="Singapore")

    home = pytz.timezone("Asia/Qatar")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock1.config(text=current_time)
    name1.config(text="Qatar")

    home = pytz.timezone("Asia/Brunei")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock1.config(text=current_time)
    name1.config(text="Brunei")
    
    
    
def main():
    global root
    root = Tk()
    root.geometry("600x600")
    global name
    name = Label(root, font=("times", 20, "bold"))
    name.place(x=50, y=30)
    global clock
    clock = Label(root, font=("times", 25, "bold"))
    clock.place(x=350, y=30)
    global name1
    name1 = Label(root, font=("times", 20, "bold"))
    name1.place(x=50, y=90)
    global clock1
    clock1 = Label(root, font=("times", 25, "bold"))
    clock1.place(x=350, y=90)
    global name2
    name2 = Label(root, font=("times", 20, "bold"))
    name2.place(x=50, y=150)
    global clock2
    clock2 = Label(root, font=("times", 25, "bold"))
    clock2.place(x=350, y=150)
    global name3
    name3 = Label(root, font=("times", 20, "bold"))
    name3.place(x=50, y=210)
    global clock3
    clock3 = Label(root, font=("times", 25, "bold"))
    clock3.place(x=350, y=210)
    global name4
    name4 = Label(root, font=("times", 20, "bold"))
    name4.place(x=50, y=270)
    global clock4
    clock4 = Label(root, font=("times", 25, "bold"))
    clock4.place(x=350, y=270)
    global name5
    name5 = Label(root, font=("times", 20, "bold"))
    name5.place(x=50, y=330)
    global clock5
    clock5 = Label(root, font=("times", 25, "bold"))
    clock5.place(x=350, y=330)
    global name6
    name6 = Label(root, font=("times", 20, "bold"))
    name6.place(x=50, y=390)
    global clock6
    clock6 = Label(root, font=("times", 25, "bold"))
    clock6.place(x=350, y=390)
    global name7
    name7 = Label(root, font=("times", 20, "bold"))
    name7.place(x=50, y=450)
    global clock7
    clock7 = Label(root, font=("times", 25, "bold"))
    clock7.place(x=350, y=450)

    times()
    root.mainloop()
if __name__ == "__main__":
    main()