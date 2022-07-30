from tkinter import *

calcu = Tk()
calcu.title("Calculator")
calcu.geometry("300x320")
calcu.resizable(width=False,height=False)
num = StringVar()




fs = "Arial 8 bold"

first_num = 0
second_num = 0
operation = 0
final_answer = 0

MULTIPLICATION = 1
DIVISION = 2
SUBTRACTION = 3
ADDITION = 4

def onenter(b):
    b.widget['background'] = 'steel blue'

def onleave(b):
     b.widget['background'] = 'light blue'

def onenter1(n):
    n.widget['background'] = 'light gray'

def onleave1(n):
    n.widget['background'] = 'white'

def button_click(button_value):
    current_display_value = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, current_display_value + button_value)


def operation_clicked(operator):
       global first_num
       if float(input_field.get()).is_integer():
          first_num = int(input_field.get())
       else:
           first_num = float(input_field.get())
       input_field.delete(0, END)
       global operation
       operation = operator
       
def clear():
    input_field.delete(0, END)

def clear_all():
    input_field.delete(0, END)
    global first_num,second_num,operation,final_answer
    first_num = 0
    second_num = 0
    operation = 0    
    final_answer = 0

def display_answer():
    global first_num,second_num,operation,final_answer
    second_num = input_field.get()
    if float(input_field.get()).is_integer():
       second_num = int(input_field.get())
    else:
        second_num = float(input_field.get())
    input_field.delete(0, END)
    if operation == ADDITION:
        final_answer = first_num + second_num
    elif operation == MULTIPLICATION:
        final_answer = first_num * second_num
    elif operation == SUBTRACTION:
        final_answer = first_num - second_num
    else:
        final_answer = first_num / second_num
    input_field.insert(0, final_answer)

def decimal_pressed():
    current_display_value = input_field.get()

    if current_display_value.find(".") == -1:
        input_field.delete(0, END)
        input_field.insert(0, current_display_value + ".")

def negative_clicked():
    if float(input_field.get()).is_integer():
            current_display_value = int(input_field.get())
            current_display_value = current_display_value * -1
    else:                                    
            current_display_value = float(input_field.get())
            current_display_value = current_display_value * -1
    input_field.delete(0, END)
    input_field.insert(0, current_display_value)
                        
                        
def back_space():
    length = len(input_field.get())
    input_field.delete(length-1, 'end')
    

input_field=Entry(calcu, justify=RIGHT, width=14, font="Calibri 30 bold",
textvariable=num, bg="light gray")
input_field.grid(row=0, column=0, columnspan=4)

button_CE=Button(calcu, text="CE",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=clear)
button_CE.grid(row=1, column=0)
button_CE.bind("<Enter>", onenter1)
button_CE.bind("<Leave>", onleave1)

button_clear=Button(calcu, text="C",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=clear_all)
button_clear.grid(row=1, column=1)
button_clear.bind("<Enter>", onenter1)
button_clear.bind("<Leave>", onleave1)

button_delete=Button(calcu, text="DEL",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=back_space)
button_delete.grid(row=1, column=2)
button_delete.bind("<Enter>", onenter1)
button_delete.bind("<Leave>", onleave1)

button_divide=Button(calcu, text="/",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=lambda : operation_clicked(DIVISION))
button_divide.grid(row=1, column=3)
button_divide.bind("<Enter>", onenter1)
button_divide.bind("<Leave>", onleave1)

button_7=Button(calcu, text="7",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command =lambda: button_click("7"))
button_7.grid(row=2, column=0)
button_7.bind("<Enter>", onenter1)
button_7.bind("<Leave>", onleave1)

button_8=Button(calcu, text="8",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("8"))
button_8.grid(row=2, column=1)
button_8.bind("<Enter>", onenter1)
button_8.bind("<Leave>", onleave1)

button_9=Button(calcu, text="9",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("9"))
button_9.grid(row=2, column=2)
button_9.bind("<Enter>", onenter1)
button_9.bind("<Leave>", onleave1)

button_multiplication=Button(calcu, text="X",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=lambda : operation_clicked(MULTIPLICATION))
button_multiplication.grid(row=2, column=3)
button_multiplication.bind("<Enter>", onenter1)
button_multiplication.bind("<Leave>", onleave1)

button_4=Button(calcu, text="4",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("4"))
button_4.grid(row=3, column=0)
button_4.bind("<Enter>", onenter1)
button_4.bind("<Leave>", onleave1)

button_5=Button(calcu, text="5",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("5"))
button_5.grid(row=3, column=1)
button_5.bind("<Enter>", onenter1)
button_5.bind("<Leave>", onleave1)

button_6=Button(calcu, text="6",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("6"))
button_6.grid(row=3, column=2)
button_6.bind("<Enter>", onenter1)
button_6.bind("<Leave>", onleave1)

button_minus=Button(calcu, text="-",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=lambda : operation_clicked(SUBTRACTION))
button_minus.grid(row=3, column=3)
button_minus.bind("<Enter>", onenter1)
button_minus.bind("<Leave>", onleave1)

button_1=Button(calcu, text="1",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("1"))
button_1.grid(row=4, column=0)
button_1.bind("<Enter>", onenter1)
button_1.bind("<Leave>", onleave1)

button_2=Button(calcu, text="2",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("2"))
button_2.grid(row=4, column=1)
button_2.bind("<Enter>", onenter1)
button_2.bind("<Leave>", onleave1)

button_3=Button(calcu, text="3",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("3"))
button_3.grid(row=4, column=2)
button_3.bind("<Enter>", onenter1)
button_3.bind("<Leave>", onleave1)

button_addition=Button(calcu, text="+",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command=lambda : operation_clicked(ADDITION))
button_addition.grid(row=4, column=3)
button_addition.bind("<Enter>", onenter1)
button_addition.bind("<Leave>", onleave1)

button_positiveNegative=Button(calcu, text="+/-",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command = negative_clicked)
button_positiveNegative.grid(row=5, column=0)
button_positiveNegative.bind("<Enter>", onenter1)
button_positiveNegative.bind("<Leave>", onleave1)

button_0=Button(calcu, text="0",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white",command =lambda: button_click("0"))
button_0.grid(row=5, column=1)
button_0.bind("<Enter>", onenter1)
button_0.bind("<Leave>", onleave1)

button_decimal=Button(calcu, text=".",width=9, height=3, font=fs, relief=GROOVE,
activebackground="white", command = decimal_pressed)
button_decimal.grid(row=5, column=2)
button_decimal.bind("<Enter>", onenter1)
button_decimal.bind("<Leave>", onleave1)

bequals = Button(calcu, text="=",width=9, height=3, font=fs, relief=GROOVE,bg="lightblue", activebackground="steel blue"
                 , command=display_answer)
bequals.grid(row=5, column=3)
bequals.bind("<Enter>", onenter)
bequals.bind("<Leave>", onleave)
calcu.mainloop()
