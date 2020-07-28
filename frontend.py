"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add an entry
Update entry
Delete
Close
"""
from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=books.curselection()[0]
    selected_tuple = books.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    ISBN_entry.delete(0, END)
    ISBN_entry.insert(END, selected_tuple[4])
    

def view_command():
    books.delete(0, END)
    for row in backend.view():
        books.insert(END, row)
        
def search_command():
    books.delete(0, END)
    for row in backend.search(title_strVar.get(), author_strVar.get(), year_strVar.get(), ISBN_strVar.get()):
        books.insert(END, row)
        
def insert_command():
    backend.insert(title_strVar.get(), author_strVar.get(), year_strVar.get(), ISBN_strVar.get())
    books.delete(0, END)
    books.insert(END, (title_strVar.get(), author_strVar.get(), year_strVar.get(), ISBN_strVar.get()))
    
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    
def update_command():
    backend.update(selected_tuple[0], title_strVar.get(), author_strVar.get(), year_strVar.get(), ISBN_strVar.get())
    view_command()


root = Tk()

root.title("BookStore")

title_label = Label(root, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(root, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(root, text="Year")
year_label.grid(row=1, column=0)

ISBN_label = Label(root, text="ISBN")
ISBN_label.grid(row=1, column=2)

title_strVar = StringVar()
title_entry = Entry(root, textvariable=title_strVar)
title_entry.grid(row=0, column = 1)

author_strVar = StringVar()
author_entry = Entry(root, textvariable=author_strVar)
author_entry.grid(row=0, column=3)

year_strVar = StringVar()
year_entry = Entry(root, textvariable=year_strVar)
year_entry.grid(row=1, column=1)

ISBN_strVar = StringVar()
ISBN_entry = Entry(root, textvariable=ISBN_strVar)
ISBN_entry.grid(row=1, column=3)

books = Listbox(root, height=8, width=50)
books.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1 = Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)

books.configure(yscrollcommand=sb1.set)
sb1.configure(command=books.yview)

books.bind('<<ListboxSelect>>', get_selected_row)

viewAll = Button(root, text="View all", width=12, command=view_command)
viewAll.grid(row=2, column=3)

searchEntry = Button(root, text="Search entry", width=12, command=search_command)
searchEntry.grid(row=3, column=3)

addEntry = Button(root, text="Add entry", width=12, command=insert_command)
addEntry.grid(row=4, column=3)

update = Button(root, text="Update", width=12, command=update_command)
update.grid(row=5, column=3)

delete = Button(root, text="Delete", width=12, command=delete_command)
delete.grid(row=6, column=3)

close = Button(root, text="Close", width=12, command=root.destroy)
close.grid(row=7, column=3)

root.mainloop()