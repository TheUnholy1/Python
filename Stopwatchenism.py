from tkinter import *
from datetime import datetime
import time
import ULTIMATE


def counter_label(label):
    def count():
        if running:
            global counter
            tt = datetime.fromtimestamp(counter)
            if(counter > 600):
                date_object = tt.strftime('%H:%M:%S')
            elif(counter > 60):
                date_object = tt.strftime('%M:%S.%f')[:-4]
            else:
                date_object = tt.strftime('%S.%f')[:-4]
            display=date_object
   
            label['text']=display
   
            label.after(4, count) 
            counter += 0.01
    count()
    
def clocktime(label):
    
    def count():
        if main1 == True:
            label['text']=time.strftime('%I:%M:%S')
            label.after(500, count) 
    count()
    

def Start(label):
    global running,main1
    running=True
    main1 = False
    counter_label(label)
    
    start['state']='disabled'
    start['highlightbackground']='black'
    
    stop['state']='normal'
    stop['highlightbackground']='red'
    
    reset['state']='disabled'
    reset['highlightbackground']='dark grey'
   

def Stop():
    global running,main1
    start['state']='normal'
    start['highlightbackground']='green'
    start['text'] = 'Resume'
    
    stop['state']='disabled'
    stop['highlightbackground']='black'
    
    reset['state']='normal'
    reset['highlightbackground']='dark grey'
    
    running = False
  

def Reset(label):
    global counter,main1
    counter=00000
    if running==False:      
        reset['state']='disabled'
        reset['highlightbackground']='black'
        
        start['text']='Start'
        
        main1 = True
        clocktime(label)


def exit_watch():
    root.destroy()
    ULTIMATE.main()
    
   
def main():
    global main1
    
    global start,reset,stop,root,counter,running
    root = Tk()
    root.title("Stopwatch")
    counter = 0
    running = False
    main1 = True


    root.minsize(width=100, height=150)
    root.resizable(False,False)

   
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
   
   
   
    label = Label(root, text=datetime.utcnow().strftime('%I:%M:%S'), fg="white", font="Geneva 45 bold",bg="#282828")
    label.pack()
    root.attributes("-alpha", 0.90)
    
    
    

    f = Frame(root)
    root.config(bg="#282828")
    f.configure(background="black")

    start = Button(f, text='Start', width=7,height=3, command=lambda:Start(label),font="Geneva 15 bold",highlightbackground="green",activeforeground='black',fg='green')
    reset = Button(f, text='Reset',width=7,height=3, state='disabled', command=lambda:Reset(label),font="Geneva 15 bold",highlightbackground="black",activeforeground='black',fg='black')
    stop = Button(f, text='Stop',width=7,height=3,state='disabled',command=Stop,font="Geneva 15 bold",highlightbackground="black",activeforeground='black',fg='red')

    exitbutton =Button(f, text='Exit',width=23,height=1,command=exit_watch,font="Geneva 15 bold",highlightbackground="black",activeforeground='black',fg='red',bd=0) 
    exitbutton.pack(side="bottom")
    
    f.pack(anchor = 'center',pady=5)
    start.pack(side="left")
    reset.pack(side="left")
    stop.pack(side ="left")
    
    clocktime(label)
    root.mainloop()
if __name__ == "__main__":
    main()
    