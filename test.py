import csv
from classes import Workout
from tkinter import *

def create_window():
    window = Tk()
    window.title("Fitness Tracker")
    window.geometry("500x700")
    window.resizable(True, True)
    return window

def enter_workout_name(window):
    name_label = Label(window, text="Workout Name:")
    name_label.pack()
    name_label.place(x=50, y=20)
    name_entry = Entry(window)
    name_entry.pack()
    name_entry.place(x=150, y=20)
    return name_entry

def save_workout(window, workout_entry, workout_data):
    name = workout_entry.get()
    workout_entry.delete(0, END)
    if name == "":
        return
    with open("workouts.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, 0, 0, 0])  # Assume initial 0s are placeholders for weight, sets, reps
    workouts_list = summon_workouts()
    create_checkboxes(window, workouts_list, workout_data, 100, workout_entry)

def summon_workouts():
    workouts_list = []
    with open("workouts.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            workout = Workout(row[0], (row[1]), (row[2]), (row[3]))  # Adjusted for new Workout structure
            workouts_list.append(workout)
    return workouts_list

def create_checkboxes(window, workouts_list, workout_data, y_placement, workout_entry):
    for workout in workouts_list:
        var = IntVar()
        cb = Checkbutton(window, text=workout.name, variable=var)
        cb.var = var
        cb.pack()
        cb.place(x=50, y=y_placement)

        # Entry fields for weight, sets, and reps
        weight_entry = Entry(window)
        sets_entry = Entry(window)
        reps_entry = Entry(window)

        weight_entry.place(x=200, y=y_placement)
        sets_entry.place(x=300, y=y_placement)
        reps_entry.place(x=400, y=y_placement)

        weight_entry.insert(0, "Weight")
        sets_entry.insert(0, "Sets")
        reps_entry.insert(0, "Reps")

        weight_entry.config(state="disabled")
        sets_entry.config(state="disabled")
        reps_entry.config(state="disabled")

        cb.config(command=lambda cb=cb, we=weight_entry, se=sets_entry, re=reps_entry: toggle_entries(cb, we, se, re))

        y_placement += 30

def toggle_entries(checkbutton, weight_entry, sets_entry, reps_entry):
    if checkbutton.var.get() == 1:
        weight_entry.config(state="normal")
        sets_entry.config(state="normal")
        reps_entry.config(state="normal")
    else:
        weight_entry.config(state="disabled")
        sets_entry.config(state="disabled")
        reps_entry.config(state="disabled")

def convert(workout_entry, window, workout_data):
    convert_button = Button(window, text="Save", command=lambda: save_workout(window, workout_entry, workout_data))
    convert_button.pack()
    convert_button.place(x=150, y=60)

def startup(window):
    workout_data = {}
    workouts_list = summon_workouts()
    workout_entry = enter_workout_name(window)
    create_checkboxes(window, workouts_list, workout_data, 100, workout_entry)
    convert(workout_entry, window, workout_data)

def main():
    window = create_window()
    startup(window)
    window.mainloop()

if __name__ == "__main__":
    main()
