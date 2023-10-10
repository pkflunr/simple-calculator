import tkinter as tk
from tkinter import ttk

### constants
ROW_COUNT = 3

window = tk.Tk()

num_label = ttk.Label(window, text = "12345679", background = "white")

buttons = []

for i in range(10):
    buttons.append(ttk.Button(window, text = str(i)))

buttons.append(ttk.Button(window, text = "."))
buttons.append(ttk.Button(window, text = "+"))
buttons.append(ttk.Button(window, text = "-"))
buttons.append(ttk.Button(window, text = "*"))
buttons.append(ttk.Button(window, text = "/"))
buttons.append(ttk.Button(window, text = "="))
buttons.append(ttk.Button(window, text = "C"))

num_label.grid(row = 0, column = 0, columnspan = ROW_COUNT, sticky = "NEWS")

counter = ROW_COUNT

for b in buttons:
    b.grid(column = (counter % ROW_COUNT), row = int(counter / ROW_COUNT), sticky = "NEWS")
    counter += 1

window.mainloop()