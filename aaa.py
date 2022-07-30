from tkinter import *

#unfinished search engine project

def button_clicks():
    
    s1 = e1.get()
    s1= Label(root,font="Arial 20")
    s1.place(x=50,y=400)



def main():
    global root
    root=Tk()
    root.title("Get Variable")
    root.config(bg="#282828")
    #root.resizable(False, False)
    #Center the App
    n1= StringVar()
    
    window_width = 400
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    
    #Create Label
    l1=Label(root,text="Internet",font="Arial 20 bold",fg="White",bg="#282828")
    l1.pack(pady=20)
    #create entry box
    global e1
    e1=Entry(root,font="Arial 20",textvariable=n1)
    e1.pack()
    #create button
    b1=Button(root,text="Search",font="Arial 15 bold",command=lambda : button_clicks())
    b1.place(x=155,y=340)
    #create listbox
    global my_list
    my_list = Listbox(root, width=50)
    my_list.pack(pady=40)
    
    #tfield = Text(root, width=46, height=10)
    #tfield.pack()
    
     
    
    
    
    
    
    root.mainloop()
    
if __name__ == "__main__":
    main()