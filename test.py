# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

def disable_entry():
    if entry['state'] == "disabled":
        entry.config(state= "normal")
    else:
        entry.config(state= "disabled")

# Create an entry widget
entry=Entry(win, width= 40, font= ('Helvetica 16'))
entry.pack(pady=20)

# Create a button
button=Checkbutton(win, text="Disable Entry", font=('Arial', 12), command=disable_entry)
button.pack()

win.mainloop()