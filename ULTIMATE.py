from tkinter import *
from tkinter.font import BOLD
import weather
import time
import Stopwatchenism


def open_stopwatch():
    root.destroy()
    Stopwatchenism.main()

def enters(e):
    e.widget['foreground'] = 'red'
    e.widget['background'] = '#B7950B'
def on_enters(e):
    e.widget['background'] = '#B7950B'
    e.widget['foreground'] = 'black'
    
def on_leaves(e):
    e.widget['background'] = '#F1C40F'
    e.widget['foreground'] = 'black'

#unfinished all in one tool
def open_weather():
    root.destroy()
    weather.main()

def time_clock():
    displaytime=time.strftime("%I:%M:%S:%p")
    digiclock=Label(root,font=("arial",60))
    digiclock.place(x=25,y=30)
    digiclock.configure(bg="#282828", fg="white")
    digiclock.pack
    digiclock.config(text=displaytime)
    digiclock.after(1000,time_clock)

def main():
    global root
    root = Tk()
    root.title("ULTIMATE TOOL")
    root.config(bg="#282828")
    root.resizable(False,False)
    
    #Center the Window
    window_width = 500
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    
    time_clock()
    
    #Buttons
    b1 = Button(root,height=2, width=12,text="Check Weather",bg="#F1C40F",fg="black",
                relief=GROOVE,bd=0,font='Arial 12 bold',activebackground="#F1C40F", command=open_weather)
    b1.place(x=30,y=150)
    b1.bind("<Enter>", on_enters)
    b1.bind("<Leave>", on_leaves)
    
    b2 =Button(root,height=2, width=12,text="Stopwatch",bg="#F1C40F",fg="black",
                relief=GROOVE,bd=0,font='Arial 12 bold',activebackground="#F1C40F", command=open_stopwatch)
    b2.place(x=30,y=210)
    b2.bind("<Enter>", on_enters)
    b2.bind("<Leave>", on_leaves)
    
    exitb =Button(root,height=2, width=12,text="Exit",fg="black",bg="#F1C40F",font=("Arial 13 bold"),
                  relief=GROOVE,bd=0,activebackground="#F1C40F", command=root.destroy)
    exitb.place(x=200,y=430)
    exitb.bind("<Enter>", enters)
    exitb.bind("<Leave>", on_leaves)
    
    
    
    
    
    root.mainloop()

if __name__ == "__main__":
    main() 