from tkinter import *

def create_window():
    window = Tk()
    window.title("Fitness Tracker")
    window.geometry("500x500")
    window.resizable(True, True)    
    return window

def print_selection():
    if (var1.get() == 1):
        print("Crunches")

window = create_window()
var1 = IntVar()
c1 = Checkbutton(window, text="Crunches",variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
window.mainloop()