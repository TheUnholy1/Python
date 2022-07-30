from tkinter import *
from tkinter.font import BOLD

root = Tk()
root.title('Auto Select/Search')
root.geometry("500x300")
root.config(bg="#282828")
root.resizable(False,False)

# Update the listbox
def update(data):
	# Clear the listbox
	my_list.delete(0, END)

	# Add toppings to listbox
	for item in data:
		my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
	# Delete whatever is in the entry box
	my_entry.delete(0, END)

	# Add clicked list item to entry box
	my_entry.insert(0, my_list.get(ANCHOR))

# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)

	# update our listbox with selected items
	update(data)				


# Create a label
my_label = Label(root, text="Gugul.com",
	font=("Helvetica", 14, BOLD), fg="#F1C40F",bg="#282828")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Vandal", "Phantom", "Classic",
	"Operator", "Onions", "Victory", "Chonke","Sherrif","Shorty","Odin"]

# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()