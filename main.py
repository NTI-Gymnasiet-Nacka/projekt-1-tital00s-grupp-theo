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
    pass
    

def enter_workout_name(window):
#create a input in the window that takes in a string and puts it in the workouts.csv file
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
    workouts_list = []
    with open("workouts.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            workout = Workout(row[0], row[1], row[2], row[3])
            workouts_list.append(workout)
    window = create_window()
    (enter_name(window))
    
    window.mainloop()

if __name__ == "__main__":
    main()