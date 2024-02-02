import csv
from classes import Workout
from tkinter import *

def create_window():
    window = Tk()
    window.title("Fitness Tracker")
    window.geometry("500x500")
    window.resizable(True, True)
    return window

def enter_workout_name(window):
    name_entry = Entry(window)
    name_entry.place(x=300, y=100)
    return name_entry

def save_workout(name_entry):
    name = name_entry.get()
    with open("workouts.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name])

def convert(name_entry, window):
    convert_button = Button(window, text="Save", command=lambda: save_workout(name_entry))
    convert_button.place(x=300, y=300)
    return convert_button

def startup(window):
    name_entry = enter_workout_name(window)
    convert(name_entry, window)

def main():
    window = create_window()
    startup(window)
    window.mainloop()

if __name__ == "__main__":
    main()