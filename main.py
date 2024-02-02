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
    
def name_label(name, window):
    name_label = Label(window, text="Name:")
    name_label.pack()
    name_label.place(x=200, y=100)
    return name_label

def enter_workout_name(window):
#create a input in the window that takes in a string and puts it in the workouts.csv file
    name = Entry()   
    name.pack()
    name.place(x=300, y=100)
    return name
    
def save_workout(name):
    with open("workouts.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(enter_workout_name(name.get()))

#create a square where name is displayed
def convert(name, window):
    convert_button = Button(window, text="Save", command=lambda: save_workout(name))
    convert_button.pack()
    convert_button.place(x=300, y=300)
    return convert_button


def startup(window):
    name = enter_workout_name(window)
    convert(name, window)
    window.mainloop()

def main():
    workouts_list = []
    with open("workouts.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            workout = Workout(row[0], row[1], row[2], row[3])
            workouts_list.append(workout)
    window = create_window()
    startup(window)
    (enter_workout_name(window))
    name = enter_workout_name(window)
    convert_button = convert(name, window)
    window.mainloop()

if __name__ == "__main__":
    main()
    