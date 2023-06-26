from tkinter import *

def btn_click(text):
    if text == "=":
        try:
            result = eval(display.get())
            display.delete(0, END)
            display.insert(END, str(result))
        except:
            display.delete(0, END)
            display.insert(END, "Error")
    elif text == "C":
        display.delete(0, END)
    else:
        display.insert(END, text)

root = Tk()
root.geometry("350x400")
root.title("Calculator")

display = Entry(root, font="Helvetica 20", justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0

for label in button_labels:
    button = Button(root, text=label, padx=10, pady=10, font="Helvetica 15 bold")
    button.grid(row=row, column=col, padx=2, pady=2)

    button.configure(command=lambda label=label: btn_click(label))

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
