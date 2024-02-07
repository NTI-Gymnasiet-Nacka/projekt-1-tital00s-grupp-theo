import csv
from classes import Workout
from tkinter import *

def create_window():
    window = Tk()
    window.title("Fitness Tracker")
    window.geometry("500x500")
    window.resizable(True, True)    
    return window
    
def enter_workout_name(window): # create a input in the window that takes in a string and puts it in the workouts.csv file
    name_label = Label(window, text="Workout Name:")
    name_label.pack()
    name_label.place(x=300, y=180)
    name_entry = Entry(window)
    name_entry.pack()
    name_entry.place(x=300, y=200)
    return name_entry # return the label


def save_workout(name_entry):
    name = name_entry.get()
    with open("workouts.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name,0,0,0])
    workouts_list = summon_workouts()
    print(workouts_list)
    return workouts_list

#create a square where name is displayed
def convert(name_entry, window):
    convert_button = Button(window, text="Save", command=lambda: save_workout(name_entry))
    convert_button.pack()
    convert_button.place(x=300, y=300)
    return convert_button

def summon_workouts(y_placement):
    workouts_list = []
    with open("workouts.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            workout = Workout(row[0], row[1], row[2], row[3])
            workouts_list.append(workout)
    return workouts_list

def create_checkboxes(window, workouts_list, y_placement):
    for workout in workouts_list:
        var = IntVar()
        c = Checkbutton(window, text=workout.name, variable=var, onvalue=1, offvalue=0)
        c.pack()
        c.place(x=100, y=y_placement)
        y_placement += 20
    return y_placement

def startup(window):
    workouts_list = summon_workouts()
    y_placement = create_checkboxes(window, workouts_list, 150)
    return workouts_list, y_placement

def main():
    window = create_window()
    workouts_list, y_placement = startup(window)

    name_label = enter_workout_name(window)
    convert_button = convert(name_label, window)
    window.mainloop()

if __name__ == "__main__":
    main()
    