from tkinter import *
import time
from datetime import datetime
import erosclock
import Stopwatch

def open_stopwatch():
    c.destroy()
    Stopwatch.main()

def bwclock():
    c.destroy()
    erosclock.main()
def on_enters(e):
    
    e.widget['foreground'] = 'green'
def on_leaves(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def time_clock():
    displaytime=time.strftime("%I:%M:%S:%p")
    digiclock=Label(c,font=("arial",70))
    digiclock.place(x=30,y=100)
    digiclock.configure(bg="#282828", fg="white")
    digiclock.pack
    digiclock.config(text=displaytime)
    digiclock.after(1000,time_clock)

def main():
    global c
    c = Tk()
    c.title("Clock")
    c.geometry("600x600")
    c.resizable(width=False,height=False)
    c.configure(bg="#282828")
    alarm = Button(c, text="Alarm", bg="white", width="15", height="2", font=("arial", 10, "bold"))
    alarm.place(x=20, y=550)
    worldclock = Button(c, text="World clock", bg="white", width="15", height="2", font=("arial", 10, "bold"),command=bwclock)
    worldclock.place(x=160, y=550)
    stopwatch = Button(c, text="Stopwatch", bg="white", width="15", height="2", font=("arial", 10, "bold"), command=open_stopwatch)
    stopwatch.place(x=310, y=550)
    timer = Button(c, text="Timer", bg="white", width="15", height="2", font=("arial", 10, "bold"))
    timer.place(x=450, y=550)
    alarm.bind("<Enter>", on_enters)
    alarm.bind("<Leave>", on_leaves)
    worldclock.bind("<Enter>", on_enters)
    worldclock.bind("<Leave>", on_leaves)
    stopwatch.bind("<Enter>", on_enters)
    stopwatch.bind("<Leave>", on_leaves)
    timer.bind("<Enter>", on_enters)
    timer.bind("<Leave>", on_leaves)
    time_clock()

    c.mainloop()

if __name__ == "__main__":
    main()
    
