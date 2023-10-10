import tkinter as tk
from tkinter import ttk
from decimal import *

### constants
ROW_COUNT = 3
## enum basically im lazy shut up
ADD = 4
SUBTRACT = 1
MULTIPLY = 2
DIVIDE = 3

window = tk.Tk()

num_label = ttk.Label(window, text = "", background = "white", anchor=tk.E)

buttons = []

first_string = ""
second_string = ""
result = ""

has_decimal = False
first_string_selected = True # true if first number is being inputted, false if second is
current_operator = None
result_displayed = False

def input_number(x):
    print("number inputted")
    global first_string, second_string, first_string_selected, result_displayed, has_decimal
    if result_displayed:
        first_string_selected = True
        result_displayed = False
        result = ""
        has_decimal = False
    if not current_operator:
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

def input_operator(operator):
    global current_operator, first_string, second_string, first_string_selected, result, result_displayed, has_decimal
    print("operator inputted")
    # ignore this input if you hit an operator button before entering any input
    if first_string_selected and not first_string:
        print("attempted to enter an operator without entering a number first")
        return

    if first_string == "." or second_string == ".":
        print("attempted to enter just a decimal")
        return
    

    
    if second_string and current_operator:
        get_result()
    if result_displayed:
        first_string = result
        result = ""
        result_displayed = False
    if not current_operator:
        current_operator = operator
        first_string_selected = False
        has_decimal = False

        
def get_result():
    global first_string, second_string, result, current_operator, result_displayed, first_string_selected, has_decimal
    print("getting result...")
    if first_string == "." or second_string == ".":
        print("attempted to enter just a decimal")
        return
    global ADD, SUBTRACT, MULTIPLY, DIVIDE
    if first_string and second_string and current_operator:
        # damn you python. using magic numbers
        match current_operator:
            case 4:
                result = str(Decimal(first_string) + Decimal(second_string))
            case 1:
                result = str(Decimal(first_string) - Decimal(second_string))
            case 2:
                result = str(Decimal(first_string) * Decimal(second_string))
            case 3:
                result = str(Decimal(first_string) / Decimal(second_string))
        num_label.config(text = result)
        result_displayed = True
        first_string = ""
        second_string = ""
        current_operator = None
        print("result obtained:" + result)

def clear():
    global first_string, second_string, first_string_selected, result, result_displayed, has_decimal
    num_label.config(text = "")
    if result_displayed:
        result = ""
    elif first_string_selected:
        first_string = ""
        has_decimal = False
    else:
        second_string = ""
        has_decimal = False

for i in range(10):
    buttons.append(ttk.Button(window, text = str(i), command = lambda j=i:input_number(j)))

buttons.append(ttk.Button(window, text = ".", command = input_decimal))
buttons.append(ttk.Button(window, text = "+", command = lambda j=ADD:input_operator(j)))
buttons.append(ttk.Button(window, text = "-", command = lambda j=SUBTRACT:input_operator(j)))
buttons.append(ttk.Button(window, text = "*", command = lambda j=MULTIPLY:input_operator(j)))
buttons.append(ttk.Button(window, text = "/", command = lambda j=DIVIDE:input_operator(j)))
buttons.append(ttk.Button(window, text = "=", command = get_result))
buttons.append(ttk.Button(window, text = "C", command = clear))

num_label.grid(row = 0, column = 0, columnspan = ROW_COUNT, sticky = "NEWS")

counter = ROW_COUNT

for b in buttons:
    b.grid(column = (counter % ROW_COUNT), row = int(counter / ROW_COUNT), sticky = "NEWS")
    counter += 1

window.mainloop()