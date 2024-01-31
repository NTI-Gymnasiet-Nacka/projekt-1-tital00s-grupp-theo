import csv, tkinter
import classes




def create_window():
    window = tkinter.Tk()
    window.title("Fitness Tracker")
    window.geometry("500x500")
    window.resizable(True, True)    
    return window
    
    pass

def main():
    window = create_window()
    
    window.mainloop()

if __name__ == "__main__":
    main()