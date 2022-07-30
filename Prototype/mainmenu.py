from tkinter import *
import time
from tkinter.font import BOLD
#eto yung edited na practice.py


def onenter(b):
    b.widget['background'] = 'white'
    b.widget['foreground'] = 'green' 
    
def onleave(b):
     b.widget['background'] = 'white'
     b.widget['foreground'] = 'black'   



def main():
    global root
    root = Tk()
    root.title("Game Box")
    root.geometry("300x400")
    root.resizable(width=False,height=False)
    root.configure(bg='black')
    #root.iconbitmap('games.ico')
    fs = "Arial 8 bold"
    
    global current_time 
    current_time=time.strftime('%A %B %d %Y %I:%M:%S %p')
    

    my_label =Label(root, text=current_time, font="Helvetica 12 bold",fg='white',bg='black' )
    my_label.grid(row=0, column=0,sticky="N", columnspan=2)
    

    card = Button(root, text="Card Game",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white", background="white")
    card.grid(row=1, column=0, padx=7)
    card.bind("<Enter>", onenter)
    card.bind("<Leave>", onleave)

    games = Button(root, text="Tic Tac Toe",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white")
    games.grid(row=1, column=1)
    games.bind("<Enter>", onenter)
    games.bind("<Leave>", onleave)

    snake = Button(root, text="Snake",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white")
    snake.grid(row=2, column=0)
    snake.bind("<Enter>", onenter)
    snake.bind("<Leave>", onleave)

    tile = Button(root, text="Tile Match",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white")
    tile.grid(row=2, column=1)
    tile.bind("<Enter>", onenter)
    tile.bind("<Leave>", onleave)

    exit = Button(root, text="Exit",width=18, height=3, font=fs, relief=RAISED,
    activebackground="white",background="white", command=root.quit)
    exit.place(relx=0.5, rely=0.5, anchor='center')
    #exit.grid(row=3, column=1, pady=5)
    exit.bind("<Enter>", onenter)
    exit.bind("<Leave>", onleave)
    root.mainloop()
    
    
if __name__ == '__main__':
    main()


  
#def clock():
#    global root1
#    root1 = Toplevel(root)
   
#    formated_clock = time.strftime("%A %B %d %Y %I:%M:%S %p")
#   my_label.config(formated_clock)
#   my_label = Label(root, text="", font=("Helvetica", 12, BOLD), fg="white", bg="black")
#    my_label.grid(row=0, column=0, sticky="N", columnspan=2)
    
#clock()
