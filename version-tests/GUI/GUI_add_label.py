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

# Add a label
ttk.Label(win, text="A Label").grid(column=0, row=0)

# Start our GUI
win.mainloop()