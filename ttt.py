from tkinter import *
import tkinter.messagebox
from random import *
import random


def main():
    root = Tk()
    
    root.geometry('400x500')
    root.title("Tic Tac Toe ")
    global bclick, flag, player2_name, player1_name, playerb, pa
    pa = StringVar()
    playerb = StringVar()
    p1 = StringVar()
    p2 = StringVar()

    player1_name = Entry(root, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)
    player2_name = Entry(root, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)
    
            

     
    bclick=True
    flag = 0

    def disableButton():
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
    def normalButton():
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        
    def TF():
        if len(player1_name.get()) == 0 and len(player2_name.get())==0:
            return False
        else:
            return True
        
    



    def btnClick(buttons):
        
        global bclick, flag, player2_name, player1_name, playerb, pa
        #print(p1.get())
        #print(p2.get())
        if(TF()):
            if buttons["text"] == " " and  bclick == True:
                buttons["text"] = "X"
                bclick = False
                playerb = player2_name.get() + " Wins!"
                pa =  player1_name.get() + " Wins!"
                checkForWin()
                flag += 1


            elif buttons["text"] == " " and bclick == False:
                buttons["text"] = "O"
                bclick = True
                checkForWin()
                flag += 1
            else:
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
        else:
            #disableButton()
            #root.destroy()
            tkinter.messagebox.showinfo("Tic-Tac-Toe","please fill player name before starting the Game")
            #normalButton()

    def checkForWin():
        if (button1['text'] == 'X' and button2['text'] == 'X' and
        button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and
        button6['text'] == 'X' or
            button7['text'] =='X' and button8['text'] == 'X' and
        button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and
        button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and
        button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and
        button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and
        button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and
        button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and
        button9['text'] == 'X'):
            disableButton()
            #root.destroy()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

        elif(flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
            #root.destroy()

        elif (button1['text'] == 'O' and button2['text'] == 'O' and
        button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and
        button6['text'] == 'O' or
                button7['text'] == 'O' and button8['text'] == 'O' and
        button9['text'] == 'O' or
                button1['text'] == 'O' and button5['text'] == 'O' and
        button9['text'] == 'O' or
                button3['text'] == 'O' and button5['text'] == 'O' and
        button7['text'] == 'O' or
                button1['text'] == 'O' and button2['text'] == 'O' and
        button3['text'] == 'O' or
                button1['text'] == 'O' and button4['text'] == 'O' and
        button7['text'] == 'O' or
                button2['text'] == 'O' and button5['text'] == 'O' and
        button8['text'] == 'O' or
                button7['text'] == 'O' and button6['text'] == 'O' and
        button9['text'] == 'O'):
            disableButton()
            #root.destroy()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


    buttons = StringVar()

    label = Label( root, text="Player 1:", font='Times 20 bold', bg='white',
    fg='black', height=1, width=8)
    label.grid(row=1, column=0)


    label = Label( root, text="Player 2:", font='Times 20 bold', bg='white',
    fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    button1 = Button(root, text=" ", font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(root, text=' ',font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(root, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)

    
    root.mainloop()
    
if __name__ == "__main__":    
    main()    
    