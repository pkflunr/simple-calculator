import tkinter as tk
from tkinter import ttk
from decimal import *

### constants
ROW_COUNT = 3
## enum basically im lazy shut up
ADD = 0
SUBTRACT = 1
MULTIPLY = 2
DIVIDE = 3

window = tk.Tk()

num_label = ttk.Label(window, text = "", background = "white", anchor=tk.E)

buttons = []

first_string = ""
second_string = ""

has_decimal = False
first_string_selected = True # true if first number is being inputted, false if second is
operation_selected = False
result_displayed = False

def input_number(x):
    global first_string, second_string, first_string_selected
    if first_string_selected:
        first_string += str(x)
        num_label.config(text = first_string)
    else:
        second_string += str(x)
        num_label.config(text = second_string)

def input_decimal():
    global has_decimal
    if not has_decimal:
        input_number(".")
        has_decimal = True


for i in range(10):
    buttons.append(ttk.Button(window, text = str(i), command = lambda j=i:input_number(j)))

buttons.append(ttk.Button(window, text = ".", command = input_decimal))
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