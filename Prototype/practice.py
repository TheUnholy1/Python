#Working Main Menu DOnt Edit
from tkinter import *
import time
import importable_template
import importable_template1
import importable_template2


root = Tk()
root.title("Game Box")
root.resizable(width=False,height=False)
root.configure(bg='black')
#root.iconbitmap('games.ico')
fs = "Arial 8 bold"

app_width = 300
app_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

def open_tic():
    importable_template1.main()



def open_tiles():
    
    importable_template.main()
    
def open_snake():
    
    importable_template2.main()
    
def onenter(b):
    b.widget['background'] = 'white'
    b.widget['foreground'] = 'green' 
    
def onleave(b):
     b.widget['background'] = 'white'
     b.widget['foreground'] = 'black'   

def clock():
 
    current_time=time.strftime('%A %B %d %Y %I:%M:%S %p')
    

    my_label =Label(root, text=current_time, font="Helvetica 12 bold",fg='white',bg='black' )
    my_label.grid(row=0, column=0,sticky="N", columnspan=2)
    my_label.after(1000, clock)
    
    
clock()


card = Button(root, text="Card Game",width=18, height=3, font=fs, relief=RAISED,
activebackground="white", background="white")
card.grid(row=1, column=0, padx=7)
card.bind("<Enter>", onenter)
card.bind("<Leave>", onleave)

games = Button(root, text="Tic Tac Toe",width=18, height=3, font=fs, relief=RAISED,
activebackground="white",background="white", command=open_tic)
games.grid(row=1, column=1)
games.bind("<Enter>", onenter)
games.bind("<Leave>", onleave)

snake = Button(root, text="Snake",width=18, height=3, font=fs, relief=RAISED,
activebackground="white",background="white",command=open_snake)
snake.grid(row=2, column=0)
snake.bind("<Enter>", onenter)
snake.bind("<Leave>", onleave)

tile = Button(root, text="Tile Match",width=18, height=3, font=fs, relief=RAISED,
activebackground="white",background="white", command=open_tiles)
tile.grid(row=2, column=1)
tile.bind("<Enter>", onenter)
tile.bind("<Leave>", onleave)

exit = Button(root, text="Exit",width=18, height=3, font=fs, relief=RAISED,
activebackground="white",background="white", command=root.destroy)
exit.place(relx=0.5, rely=0.5, anchor='center')
#exit.place(x=90,y=300)
#exit.grid(row=3, column=1, pady=5)
exit.bind("<Enter>", onenter)
exit.bind("<Leave>", onleave)


root.mainloop()
