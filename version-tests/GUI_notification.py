import tkinter as tk

win = tk.Tk()

notification_text = tk.StringVar()
progress = tk.Label(win, textvariable=notification_text)
progress.grid(column=0, row=0)

def update_progress():
	global current_progress
	current_progress += 1

	if current_progress <= 5:
		notification_text.set("%s/5 downloaded" % current_progress)
		win.after(1000, update_progress)

	else:
		notification_text.set("Done!")

	

current_progress = 0
notification_text.set("%s/5 downloaded" % current_progress)
win.after(1, update_progress)

win.mainloop()