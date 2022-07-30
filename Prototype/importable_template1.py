from tkinter import *
import random
from tkinter.font import BOLD

#tictactoe game

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

#def onenter1(b):
#    b.widget['background'] = 'white'
#    b.widget['foreground'] = 'red' 
            
#def onenter(b):
#    b.widget['background'] = 'white'
#    b.widget['foreground'] = 'green' 
    
#def onleave(b):
#     b.widget['background'] = 'white'
#    b.widget['foreground'] = 'black' 

def main():
    
    window = Tk()
    window.title("Tic-Tac-Toe")
    window.resizable(width=False,height=False)
    global players
    players = ["x","o"]
    global player
    player = random.choice(players)
    global buttons
    buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    global label
    label = Label(window,text=player + " Turn", font=('consolas',40, BOLD))
    label.grid(column=4, row=0, columnspan= 8)

#    reset_button = Button(window,text="Restart", font=('consolas',20, BOLD)
#                          ,background="white", relief=GROOVE, command=new_game)
#    reset_button.grid(column=1,row=3)
 #   reset_button.bind("<Enter>", onenter)
#   reset_button.bind("<Leave>", onleave)

 #   exit_button = Button(window,text="Exit", font=('consolas',20, BOLD)
#                         ,background="white", command=window.destroy, relief="groove")
#    exit_button.grid(column=2, row=6)
#    exit_button.bind("<Enter>", onenter1)
#    exit_button.bind("<Leave>", onleave)

    frame = Frame(window)
    frame.grid(column=4,row=6)
    
    #create a menu
    my_menu = Menu(window)
    window.config(menu=my_menu)
    #create options for dropdown menu
    
    option_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Reset Game", command=new_game)
    option_menu.add_separator()
    option_menu.add_command(label="Exit Game", command=window.destroy) 
    

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,relief="groove"
                                      ,command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row,column=column)

    window.mainloop()

if __name__ == "__main__":
    main()