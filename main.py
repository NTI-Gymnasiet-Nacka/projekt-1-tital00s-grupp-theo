import csv
from classes import Workout
from tkinter import *




def create_window():
    window = Tk()
    window.title("Fitness Tracker")
    window.geometry("500x500")
    window.resizable(True, True)    
    return window

def summon_workouts(window):
    
    

def enter_name(window):
#create a input in the window that takes in a string
    name = Entry()   
    name.pack()
    name.place(x=300, y=100)
    return name

#create a square where name is displayed
def display_name(window, name):
    name_display = Label(window, text=name)
    name_display.pack()
    name_display.place(x=300, y=100)
    return name_display


def main():
    
    window = create_window()
    (enter_name(window))
    
    window.mainloop()

if __name__ == "__main__":
    main()