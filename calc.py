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

num_label.pack()

for b in buttons:
    b.pack()

window.mainloop()