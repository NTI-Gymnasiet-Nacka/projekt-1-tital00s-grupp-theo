import csv, tkinter
import classes




def create_window():
    window = tkinter.Tk()
    window.title("Fitness Tracker")
    window.geometry("500x500")
    window.resizable(True, True)    
    return window


def enter_name(window):
#create a input in the window that takes in a string
    name = tkinter.Entry()    
    name.pack()
    name.place(x=300, y=100)
    return name


def main():
    window = create_window()
    print(enter_name(window))
    
    window.mainloop()

if __name__ == "__main__":
    main()