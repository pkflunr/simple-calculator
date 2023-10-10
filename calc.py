import tkinter as tk

### constants
ROW_COUNT = 3

window = tk.Tk()

num_label = tk.Label(window, text = "12345679")

buttons = []

for i in range(10):
    buttons.append(tk.Button(window, text = str(i)))

buttons.append(tk.Button(window, text = "+"))
buttons.append(tk.Button(window, text = "-"))
buttons.append(tk.Button(window, text = "*"))
buttons.append(tk.Button(window, text = "/"))
buttons.append(tk.Button(window, text = "."))
buttons.append(tk.Button(window, text = "="))
buttons.append(tk.Button(window, text = "C"))

num_label.grid(row = 0, column = 0, columnspan = 2, sticky = "NEWS")

counter = ROW_COUNT

for b in buttons:
    b.grid(column = (counter % ROW_COUNT), row = int(counter / ROW_COUNT), sticky = "NEWS")
    counter += 1

window.mainloop()