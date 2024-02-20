import csv # import the csv module
from classes import Workout # import the Workout class
from tkinter import * # import the tkinter module

def create_window(): # create a window with a title and size
    window = Tk() # create a window
    window.title("Fitness Tracker") # set the title of the window
    window.geometry("500x500") # set the size of the window
    window.resizable(True, True) # make the window resizable
    return window # return the window
    
def enter_workout_name(window): # create a input in the window that takes in a string and puts it in the workouts.csv file
    name_label = Label(window, text="Workout Name:") # create a label
    name_label.pack() # pack the label
    name_label.place(x=300, y=180) # place the label
    name_entry = Entry(window) # create an entry
    name_entry.pack() # pack the entry
    name_entry.place(x=300, y=200) # place the entry
    return name_entry # return the label


def save_workout(window, workout_entry): # save the workout to the workouts.csv file
    name = workout_entry.get() # get the name from the entry
    workout_entry.delete(0, END) # delete the entry
    if name == "": # if the name is empty
        return # return
    with open("workouts.csv", "a", newline="", encoding="utf-8") as csvfile: # open the workouts.csv file
        writer = csv.writer(csvfile) # create a writer
        writer.writerow([name,0,0,0]) # write the name to the file
    workouts_list = summon_workouts() # get the workouts from the file  
    create_checkboxes(window, workouts_list, 200, workout_entry) # create the checkboxes
    return workouts_list # return the workouts

#create a square where name is displayed
def convert(workout_entry, window): # create a button that saves the workout
    convert_button = Button(window, text="Save", command=lambda: save_workout(window, workout_entry)) # create a button
    convert_button.pack() # pack the button
    convert_button.place(x=300, y=300) # place the button

def summon_workouts(): # get the workouts from the workouts.csv file
    workouts_list = [] # create a list
    with open("workouts.csv", encoding="utf-8") as csvfile: # open the workouts.csv file
        reader = csv.reader(csvfile) # create a reader
        next(reader) # skip the first row
        for row in reader: # for each row in the file
            workout = Workout(row[0], row[1], row[2], row[3]) # create a workout
            workouts_list.append(workout) # append the workout to the list
    return workouts_list # return the list

def disable_entries(workout_entry): # create a label
    if workout_entry['state'] == "normal":
        workout_entry.config(state= "disabled")
    else:
        workout_entry.config(state= "normal")
    return workout_entry
    

def create_checkboxes(window, workouts_list, y_placement, workout_entry): # create a checkbox for each workout
    checkbutton_list = [] # create a list
    for workout in workouts_list: # for each workout in the list
        var = IntVar() # create a variable
        workout_check = Checkbutton(window, text=workout.name, onvalue=1, offvalue=0, command=lambda: disable_entries(workout_entry)) # create a checkbox
        workout_check.pack() # pack the checkbox
        workout_check.place(x=100, y=y_placement) # place the checkbox
        checkbutton_list.append(workout_check) # append the checkbox to the list
        y_placement += 20 # increase the y placement
        return checkbutton_list

def startup(window): # create the window and the checkboxes
    workouts_list = summon_workouts() # get the workouts from the file
    workout_entry = enter_workout_name(window) # create the input
    checkbutton_list = create_checkboxes(window, workouts_list, 200, workout_entry) # create the checkboxes
    return workout_entry # return the input


def main(): # create the window and the checkboxes
    window = create_window() # create the window
    workout_entry = startup(window) # create the checkboxes
    workout_entry.state = "normal"
    convert(workout_entry, window) # create the button
    window.mainloop() # run the window

if __name__ == "__main__":
    main()
    