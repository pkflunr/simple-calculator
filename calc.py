import tkinter as tk

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
buttons.append(tk.Button(window, text = "C"))

num_label.grid(row = 0, column = 0, columnspan = 2, sticky = "NEWS")

counter = 3

for b in buttons:
    b.grid(column = (counter % 3), row = int(counter / 3), sticky = "NEWS")
    counter += 1

window.mainloop()