from tkinter import *
import tkinter as tk
from db_operations import insert_data, search_data, search_all

root = Tk()

def add_data(name, age, address):
    insert_data(name, age, address)
    display_all()

def display_search(id):
    result = search_data(id)
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.config(background="dark gray")
    listbox.insert(END, result)
    id_search.delete(0, 'end')

def display_all():
    result = search_all()
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, column=1)

    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.grid(row=10, column=2, sticky="ns")
    listbox.config(yscrollcommand=scrollbar.set, background="dark gray")
    scrollbar.config(command=listbox.yview)

    for row in result:
        listbox.insert(END, row)


canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=.3, rely=.1, relwidth=.8, relheight=.8)

label = Label(frame, text='Add data')
label.grid(row=0, column=1)

label = Label(frame, text='Name')
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
entry_name.config(background="light gray")

label = Label(frame, text='Age')
label.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2, column=1)
entry_age.config(background="light gray")

label = Label(frame, text='Address')
label.grid(row=3, column=0)
entry_address = Entry(frame)
entry_address.grid(row=3, column=1)
entry_address.config(background="light gray")

button = Button(frame, text='Add', command=lambda:add_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

label = Label(frame, text='Search data')
label.grid(row=5, column=1)

label = Label(frame, text='Search by ID')
label.grid(row=6, column=0)
id_search = Entry(frame)
id_search.grid(row=6, column=1)
id_search.config(background="light gray")

button = Button(frame, text='Search', command=lambda:display_search(id_search.get()))
button.grid(row=6, column=2)

display_all()

root.mainloop()




