from tkinter import *
from datetime import date
today = date.today()

def onenter(a):
    a.widget ['background'] ='dodgerblue3'
def onleave(a):
    a.widget['background'] = 'steelblue'

def onenter1(b):
    b.widget ['background'] ='gray'
def onleave1(b):
    b.widget['background'] = 'lightgray'

def calculate_age():
    today=date.today()
    bdate=date(int(y.get()),int(m.get()),int(d.get()))
    age= today.year - bdate.year - ((today.month,today.day)<(bdate.month,bdate.day))
    Label(text=F"     YOUR AGE IS {age}     ",font=('Britannic Bold', 13, "bold"), borderwidth="5").place(x=146,y=316)

def exit():
    root.destroy()

def main():
    global root
    root = Tk()
    root.geometry("500x400")
    root.config(bg="lightblue")
    root.resizable(width=False, height=False)
    root.title('Age Calculator')
    l1 = Label(root, text="      WELCOME TO AGE CALCULATOR      ", font=("Britannic Bold", 20), borderwidth="20",
               fg="white", bg="skyblue4")
    l2 = Label(root, font=("Britannic Bold", 12), text="Enter your birthday using this format mm-dd-yyyy.", fg="white",
               bg="steelblue")

    l_m = Label(root, text=" MONTH:", font=('Britannic Bold', 12, "bold"), borderwidth="7", fg="white", bg="teal")
    l_d = Label(root, text=" DATE:   ", font=('Britannic Bold', 12, "bold"), borderwidth="7", fg="white", bg="teal")
    l_y = Label(root, text=" YEAR:   ", font=('Britannic Bold', 12, "bold"), borderwidth="7", fg="white", bg="teal")

    options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    global m
    m = StringVar()
    m.set(options[0])
    m1 = OptionMenu(root, m, *options)
    m1.pack()

    options2 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
                "18", "19", "20", "21",
                "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    global d
    d = StringVar()
    d.set(options2[0])
    d1 = OptionMenu(root, d, *options2)
    d1.pack()

    options3 = ["1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962",
                "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975",
                "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984",
                "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997",
                "1998", "1999",
                "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
                "2013", "2014",
                "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    global y
    y = StringVar()
    y.set(options3[50])
    y1 = OptionMenu(root, y, *options3)
    y1.pack()

    b1 = Button(root, text="    CALCULATE AGE    ", font=("Britannic Bold", 15), fg="white", bg="steelblue",
                borderwidth="10", command=calculate_age)
    b1.bind("<Enter>", onenter)
    b1.bind("<Leave>", onleave)
    b2 = Button(root, text="Exit Application", font=("Britannic Bold", 13), bg="lightgray", command=exit)
    b2.bind("<Enter>", onenter1)
    b2.bind("<Leave>", onleave1)

    l1.place(x=0, y=0)
    l2.place(x=65, y=80)
    l_m.place(x=150, y=115)
    l_d.place(x=150, y=165)
    l_y.place(x=150, y=215)
    m1.place(x=285, y=115)
    d1.place(x=285, y=165)
    y1.place(x=285, y=215)
    b1.place(x=140, y=258)
    b2.place(x=185, y=351)

    root.mainloop()

if __name__=="__main__":
  main()




