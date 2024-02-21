import csv
from classes import Workout
from tkinter import *

def create_window():
    window = Tk() # Create a window
    window.title("Fitness Tracker") # Set the title of the window
    window.geometry("600x400") # Set the size of the window
    window.resizable(True, True) # Set the window to be resizable
    return window # Return the window

def enter_workout_name(window): # Create a label and entry for the workout name
    name_label = Label(window, text="Workout Name:") # Create a label
    name_label.pack() # Add the label to the window
    name_label.place(x=50, y=20) # Set the position of the label
    name_entry = Entry(window) # Create an entry
    name_entry.pack() # Add the entry to the window
    name_entry.place(x=150, y=20) # Set the position of the entry
    return name_entry

def save_workout(window, workout_entry, workout_data):
    name = workout_entry.get() # Get the name of the workout
    workout_entry.delete(0, END) # Clear the entry
    if name == "": # If the name is empty, return
        return
    with open("workouts.csv", "a", newline="", encoding="utf-8") as csvfile: # Open the workouts.csv file
        writer = csv.writer(csvfile) # Create a writer object
        writer.writerow([name, 0, 0, 0])  # Assume initial 0s are placeholders for weight, sets, reps
    workouts_list = summon_workouts() # Get the list of workouts
    create_checkboxes(window, workouts_list, workout_data, 100, workout_entry) # Create the checkboxes

def summon_workouts():
    workouts_list = [] # Create an empty list
    with open("workouts.csv", encoding="utf-8") as csvfile: # Open the workouts.csv file
        reader = csv.reader(csvfile) # Create a reader object
        next(reader)  # Skip the header row
        for row in reader: # Iterate through the rows
            workout = Workout(row[0], (row[1]), (row[2]), (row[3]))  # Adjusted for new Workout structure
            workouts_list.append(workout) # Add the workout to the list
    return workouts_list # Return the list of workouts

def create_checkboxes(window, workouts_list, workout_data, y_placement, workout_entry): # Create checkboxes for the workouts
    for workout in workouts_list: # Iterate through the workouts
        var = IntVar() # Create an IntVar
        cb = Checkbutton(window, text=workout.name, variable=var) # Create a Checkbutton
        cb.var = var # Set the var attribute of the Checkbutton
        cb.pack() # Add the Checkbutton to the window
        cb.place(x=50, y=y_placement) # Set the position of the Checkbutton

        # Entry fields for weight, sets, and reps
        weight_entry = Entry(window) # Create an entry for the weight
        sets_entry = Entry(window) # Create an entry for the sets
        reps_entry = Entry(window) # Create an entry for the reps

        weight_entry.place(x=200, y=y_placement) # Set the position of the weight entry
        sets_entry.place(x=300, y=y_placement) # Set the position of the sets entry
        reps_entry.place(x=400, y=y_placement) # Set the position of the reps entry

        weight_entry.insert(0, "Weight") # Insert "Weight" into the weight entry
        sets_entry.insert(0, "Sets") # Insert "Sets" into the sets entry
        reps_entry.insert(0, "Reps") # Insert "Reps" into the reps entry

        weight_entry.config(state="disabled") # Set the weight entry to be disabled
        sets_entry.config(state="disabled") # Set the sets entry to be disabled
        reps_entry.config(state="disabled") # Set the reps entry to be disabled

        cb.config(command=lambda cb=cb, we=weight_entry, se=sets_entry, re=reps_entry: toggle_entries(cb, we, se, re)) # Set the command of the Checkbutton to toggle_entries function with the Checkbutton and entries as arguments

        y_placement += 30

def toggle_entries(checkbutton, weight_entry, sets_entry, reps_entry): # Toggle the state of the entries
    if checkbutton.var.get() == 1: # If the Checkbutton is checked
        weight_entry.config(state="normal") # Set the weight entry to be normal
        sets_entry.config(state="normal") # Set the sets entry to be normal
        reps_entry.config(state="normal") # Set the reps entry to be normal
    else:
        weight_entry.config(state="disabled") # Set the weight entry to be disabled
        sets_entry.config(state="disabled") # Set the sets entry to be disabled
        reps_entry.config(state="disabled") # Set the reps entry to be disabled

def convert(workout_entry, window, workout_data): # Convert the workout data to a csv file
    convert_button = Button(window, text="Save", command=lambda: save_workout(window, workout_entry, workout_data)) # Create a button to save the workout
    convert_button.pack() # Add the button to the window
    convert_button.place(x=150, y=60) # Set the position of the button

def startup(window): # Start the program
    workout_data = {} # Create an empty dictionary
    workouts_list = summon_workouts() # Get the list of workouts
    workout_entry = enter_workout_name(window) # Create the entry for the workout name
    create_checkboxes(window, workouts_list, workout_data, 100, workout_entry) # Create the checkboxes
    convert(workout_entry, window, workout_data) # Convert the workout data to a csv file

def main():
    window = create_window() # Create the window
    startup(window) # Start the program
    window.mainloop() # Run the window

if __name__ == "__main__":
    main()
