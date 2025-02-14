# Ref: Burkhard A. Meier - Python GUI Programming Cookbook 2nd ed.
# Preventing the GUI from being resized
import tkinter as tk

# Create instance
win = tk.Tk()

# Add a title
win.title("Novelscraper")

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)

# Enable resizing x-dimension, disable y-dimension
# win.resizable(True, False)

# Start our GUI
win.mainloop()