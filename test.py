from tkinter import *

from main import create_window

window = create_window()

name = Entry()
name.pack()
name.place(x=300, y=100)
save_button = Button(window, text="Save", command=lambda: name.get())
save_button.pack()
save_button.place(x=300, y=150)


window.mainloop()