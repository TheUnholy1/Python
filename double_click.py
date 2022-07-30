from tkinter import *
def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

widget = Button(None, text='Mouse Clicks')
widget.pack()
but2 =Button(None, text='X', fg="Red")
but2.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
but2.bind('<Double-1>', quit) 
widget.mainloop()
