import csv
from tkinter import *

# Create the main application window
def create_window():
    """Initialize the main application window."""
    window = Tk()
    window.title("Fitness Tracker")
    window.geometry("600x400")
    window.resizable(False, False)
    return window

# Define the Workout class to hold workout data
class Workout:
    """A class to represent a workout with name, weight, reps, and sets."""
    def __init__(self, name, weight="", reps="", sets=""):
        self.name = name
        self.weight = weight
        self.reps = reps
        self.sets = sets

# Function to load workouts from a CSV file
def summon_workouts():
    """Read workout data from 'workouts.csv' and return a list of Workout objects."""
    workouts_list = []
    with open("workouts.csv", mode="r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            workouts_list.append(Workout(row['name'], row['weight'], row['reps'], row['sets']))
    return workouts_list

# Function to save a new workout to the CSV file
def save_new_workout(workout_entry, workout_data):
    """Save a new workout to 'workouts.csv' and update the UI."""
    name = workout_entry.get().strip()
    if name:  # Check if name is not empty
        with open("workouts.csv", mode="a", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, "", "", ""])
        update_ui()
    workout_entry.delete(0, END)

# Function to save updates to the workout data back to the CSV
def save_updates(workout_data):
    """Write updated workout data back to 'workouts.csv'."""
    with open("workouts.csv", mode="w", encoding="utf-8", newline="") as csvfile:
        fieldnames = ['name', 'weight', 'reps', 'sets']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for workout, entries in workout_data.items():
            writer.writerow({
                'name': workout,
                'weight': entries['weight'].get(),
                'reps': entries['reps'].get(),
                'sets': entries['sets'].get()
            })
    update_ui()

# Function to update the application's UI
def update_ui():
    """Clear and rebuild the UI with updated data."""
    global window, workout_data
    for widget in window.winfo_children():
        widget.destroy()
    startup()

# Function to control the entry widget states based on checkbox
def toggle_entry_state(*args, workout_data, name):
    """Enable or disable entry widgets based on the state of their corresponding checkbox."""
    if workout_data[name]["var"].get():
        workout_data[name]["weight"].config(state=NORMAL)
        workout_data[name]["reps"].config(state=NORMAL)
        workout_data[name]["sets"].config(state=NORMAL)
    else:
        workout_data[name]["weight"].config(state=DISABLED)
        workout_data[name]["reps"].config(state=DISABLED)
        workout_data[name]["sets"].config(state=DISABLED)

# Validation function for entry widget input
def only_numeric_input(P):
    """Allow only numeric input in entry widgets."""
    return P.isdigit() or P == ""

# Function to set up the application's UI
def startup():
    """Initialize the application's UI with widgets."""
    global window, workout_data
    workout_data = {}
    workout_entry = enter_workout_name(window)
    units_label(window)
    workouts_list = summon_workouts()
    y_placement = 100
    for workout in workouts_list:
        create_workout_row(window, workout, workout_data, y_placement)
        y_placement += 30
    Button(window, text="Add Workout", command=lambda: save_new_workout(workout_entry, workout_data)).place(x=450, y=20)
    Button(window, text="Save Changes", command=lambda: save_updates(workout_data)).place(x=250, y=350)

# Helper function to create each workout row in the UI
def create_workout_row(window, workout, workout_data, y_placement):
    """Create a row in the UI for each workout."""
    validation = window.register(only_numeric_input)
    var = IntVar()
    cb = Checkbutton(window, text=workout.name, variable=var)
    cb.place(x=50, y=y_placement)
    cb.config(command=lambda name=workout.name: toggle_entry_state(workout_data=workout_data, name=name))

    # Create entry widgets for weight, reps, and sets
    weight_entry = Entry(window, validate="key", validatecommand=(validation, '%P'))
    weight_entry.place(x=200, y=y_placement)
    weight_entry.insert(0, workout.weight)
    weight_entry.config(state=DISABLED)

    reps_entry = Entry(window, validate="key", validatecommand=(validation, '%P'))
    reps_entry.place(x=300, y=y_placement)
    reps_entry.insert(0, workout.reps)
    reps_entry.config(state=DISABLED)

    sets_entry = Entry(window, validate="key", validatecommand=(validation, '%P'))
    sets_entry.place(x=400, y=y_placement)
    sets_entry.insert(0, workout.sets)
    sets_entry.config(state=DISABLED)

    # Display recommended weight, if applicable
    try:
        recommended_weight = float(workout.weight) * 1.025 if workout.weight else ""
    except ValueError:
        recommended_weight = ""
    rec_label = Label(window, text=f"Rec: {recommended_weight:.2f}" if recommended_weight else "")
    rec_label.place(x=470, y=y_placement)

    workout_data[workout.name] = {
        "weight": weight_entry, 
        "reps": reps_entry, 
        "sets": sets_entry, 
        "var": var
    }

# Helper functions to add labels to the UI
def units_label(window):
    """Label for the units (weight, reps, sets)."""
    Label(window, text="Weight                    Reps                         Sets").place(x=200, y=70)

def enter_workout_name(window):
    """Entry widget for adding a new workout name."""
    Label(window, text="Workout Name:").place(x=50, y=20)
    workout_entry = Entry(window)
    workout_entry.place(x=150, y=20)
    return workout_entry

# Initialize and run the application
window = create_window()
startup()

if __name__ == "__main__":
    mainloop()
