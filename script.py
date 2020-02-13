from tkinter import *
from backend import Database

database = Database("books.db")

def view_command():
    box.delete(0, END)
    for row in database.view():
        box.insert(END, row)
    
def search_command():
    box.delete(0, END)
    for row in database.search(titleEntry.get(), authorEntry.get(), yearEntry.get(), ISBNEntry.get()):
        box.insert(END, row)

def add_command():
    database.insert(titleEntry.get(), authorEntry.get(), yearEntry.get(), ISBNEntry.get())
    view_command()

def get_selected_row(event):
    try:
        global selected_tuple
        index = box.curselection()[0]
        selected_tuple = box.get(index)
        title.delete(0, END)
        title.insert(END, selected_tuple[1])
        year.delete(0, END)
        year.insert(END, selected_tuple[2])
        author.delete(0, END)
        author.insert(END, selected_tuple[3])
        ISBN.delete(0, END)
        ISBN.insert(END, selected_tuple[4])
    except IndexError:
        pass


def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], titleEntry.get(), authorEntry.get(), yearEntry.get(), ISBNEntry.get())
    view_command()

interface = Tk()

interface.wm_title("BookCity")

titleLab = Label(interface, text = "Title")
titleLab.grid(row = 0, column = 0)

titleEntry = StringVar()
title = Entry(interface, textvariable = titleEntry, width = 15)
title.grid(row = 0, column = 1)

yearLab = Label(interface, text = "Year")
yearLab.grid(row = 1, column = 0)

yearEntry = StringVar()
year = Entry(interface, textvariable = yearEntry, width = 15)
year.grid(row = 1, column = 1)

authorLab = Label(interface, text = "Author")
authorLab.grid(row = 0, column = 2)

authorEntry = StringVar()
author = Entry(interface, textvariable = authorEntry, width = 15)
author.grid(row = 0, column = 3)

ISBNLab = Label(interface, text = "ISBN")
ISBNLab.grid(row = 1, column = 2)

ISBNEntry = StringVar()
ISBN = Entry(interface, textvariable = ISBNEntry, width = 15)
ISBN.grid(row = 1, column = 3)

viewBut = Button(interface, text = "View All", height = 1, width = 10, command = view_command)
viewBut.grid(row = 2, column = 3)

searchBut = Button(interface, text = "Search Entry", height = 1, width = 10, command = search_command)
searchBut.grid(row = 3, column = 3)

AddBut = Button(interface, text = "Add Entry", height = 1, width = 10, command = add_command)
AddBut.grid(row = 4, column = 3)

updateBut = Button(interface, text = "Update", height = 1, width = 10, command = update_command)
updateBut.grid(row = 5, column = 3)

deleteBut = Button(interface, text = "Delete", height = 1, width = 10, command = delete_command)
deleteBut.grid(row = 6, column = 3)

closeBut = Button(interface, text = "Close", height = 1, width = 10, command = interface.destroy)
closeBut.grid(row = 7, column = 3)

box = Listbox(interface, height = 6, width = 35)
box.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scr = Scrollbar(interface)
scr.grid(row = 2, column = 2, rowspan = 6)

box.configure(yscrollcommand = scr.set)
scr.configure(command = box.yview)

box.bind('<<ListboxSelect>>', get_selected_row)

interface.mainloop()

