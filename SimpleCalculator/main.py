from tkinter import *
import ast

root = Tk()
root.title("CalculatorApp")
root.configure(bg="black")

i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    display.delete(0, END)

def calculate():
    ent_string = display.get()
    try:
        node = ast.parse(ent_string, mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')

def remove_last():
    ent_string = display.get()
    if len(ent_string):
        new_str = ent_string[:-1]
        clear_all()
        display.insert(0, new_str)
    else:
        clear_all()
        display.insert(0, '')


display = Entry(root, bg='dark gray', width=35, font=('Arial', 14))
display.grid(row=1, columnspan=6, padx=5, pady=5)

numbers = [7,8,9,4,5,6,1,2,3]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, 
                        text=button_text, 
                        width=2, 
                        height=2, 
                        background='dark gray',
                        command=lambda text=button_text: get_number(text))
        button.grid(row=x+2, column=y, padx=5, pady=5)
        counter += 1

button = Button(root, 
                text="0", 
                width=2, 
                height=2, 
                background='dark gray', 
                command=lambda : get_number(0))
button.grid(row=5, column=1, padx=5, pady=5)

count = 0
operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, 
                            text=operations[count], 
                            width=2, 
                            height=2, 
                            background='dark gray', 
                            command=lambda text=operations[count]: get_operation(text))
            button.grid(row=x+2, column=y+3, padx=5, pady=5)
            count += 1

Button(root, 
       text='AC', 
       width=2, 
       height=2, 
       background='red', 
       command=clear_all).grid(row=5, column=0, padx=5, pady=5)
Button(root, 
       text='=', 
       width=2, height=2, 
       background='green', 
       command=calculate).grid(row=5, column=2, padx=5, pady=5)
Button(root, 
       text='<=', 
       width=9, 
       height=2, 
       background='yellow', 
       command=remove_last).grid(row=5, column=4, columnspan=2, padx=5, pady=5)

root.mainloop()