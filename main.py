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


def save_workout(window, name_entry): # save the workout to the workouts.csv file
    name = name_entry.get() # get the name from the entry
    name_entry.delete(0, END) # delete the entry
    if name == "": # if the name is empty
        return # return
    with open("workouts.csv", "a", newline="", encoding="utf-8") as csvfile: # open the workouts.csv file
        writer = csv.writer(csvfile) # create a writer
        writer.writerow([name,0,0,0]) # write the name to the file
    workouts_list = summon_workouts() # get the workouts from the file
    print(workouts_list) # print the workouts
    create_checkboxes(window, workouts_list, 200) # create the checkboxes
    return workouts_list # return the workouts

#create a square where name is displayed
def convert(name_entry, window): # create a button that saves the workout
    convert_button = Button(window, text="Save", command=lambda: save_workout(window, name_entry)) # create a button
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

def create_checkboxes(window, workouts_list, y_placement): # create a checkbox for each workout
    for workout in workouts_list: # for each workout in the list
        var = IntVar() # create a variable
        c = Checkbutton(window, text=workout.name, onvalue=1, offvalue=0, variable=var) # create a checkbox
        c.pack() # pack the checkbox
        c.place(x=100, y=y_placement) # place the checkbox
        y_placement += 20 # increase the y placement

def startup(window): # create the window and the checkboxes
    workouts_list = summon_workouts() # get the workouts from the file
    y_placement = create_checkboxes(window, workouts_list, 200) # create the checkboxes


def main(): # create the window and the checkboxes
    window = create_window() # create the window
    startup(window) # create the checkboxes
    name_label = enter_workout_name(window) # create the input
    convert(name_label, window) # create the button
    window.mainloop() # run the window

if __name__ == "__main__":
    main()
    