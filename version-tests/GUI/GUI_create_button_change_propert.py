# Ref: Burkhard A. Meier - Python GUI Programming Cookbook 2nd ed.
# Preventing the GUI from being resized
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Novelscraper")

# Disable resizing the GUI by passing in False/False
# win.resizable(False, False)

# Enable resizing x-dimension, disable y-dimension
# win.resizable(True, False)

# Adding a Label that will get modified
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Button Click Event Function
def click_me():
	action.configure(text="** I have been Clicked! **")
	a_label.configure(foreground="red")
	a_label.configure(text="A Red Label")

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=0)

# Start our GUI
win.mainloop()