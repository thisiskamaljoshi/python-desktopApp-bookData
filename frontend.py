from tkinter import *
import backend


def clearEntries():
    titleEntry.delete(0, END)
    yearEntry.delete(0, END)
    authorEntry.delete(0, END)
    ISBNEntry.delete(0, END)


def view_command():
    bookList.delete(0, END)
    for row in backend.view():
        bookList.insert(END, row)  # means insert row at end


def search_command():
    bookList.delete(0, END)
    for row in backend.search(text_title.get(), text_Author.get(), text_year.get(), text_ISBN.get()):
        bookList.insert(END, row)  # means insert row at end


def add_command():
    backend.insert(text_title.get(), text_Author.get(),
                   text_year.get(), text_ISBN.get())
    bookList.delete(0, END)
    bookList.insert(END, (text_title.get(), text_Author.get(),
                          text_year.get(), text_ISBN.get()))
    view_command()


def get_selected_row(event):
    index = bookList.curselection()[0]
    global selected_tuple  # global variable
    selected_tuple = bookList.get(index)
    clearEntries()
    titleEntry.insert(END, selected_tuple[1])
    yearEntry.insert(END, selected_tuple[2])
    authorEntry.insert(END, selected_tuple[3])
    ISBNEntry.insert(END, selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    clearEntries()


def update_command():
    backend.update(selected_tuple[0], text_title.get(), text_Author.get(),
                   text_year.get(), text_ISBN.get())
    clearEntries()


# creating a window for our content
window = Tk()

# creating a label
labelTitle = Label(window, text="Title")
# positioning a label
labelTitle.grid(row=0, column=0)

labelYear = Label(window, text="Year")
labelYear.grid(row=0, column=2)

labelAuthor = Label(window, text="Author")
labelAuthor.grid(row=1, column=0)

labelISBN = Label(window, text="ISBN")
labelISBN.grid(row=1, column=2)

text_title = StringVar()
# StringVar() creates a spatial variable
titleEntry = Entry(window, textvariable=text_title)
# textvariable expects a spatial variable
titleEntry.grid(row=0, column=1)

text_year = StringVar()
yearEntry = Entry(window, textvariable=text_year)
yearEntry.grid(row=0, column=3)

text_Author = StringVar()
authorEntry = Entry(window, textvariable=text_Author)
authorEntry.grid(row=1, column=1)

text_ISBN = StringVar()
ISBNEntry = Entry(window, textvariable=text_ISBN)
ISBNEntry.grid(row=1, column=3)

# adding a ListBox
bookList = Listbox(window, height=6, width=35)
# positioning the scollbar
bookList.grid(row=2, column=0, rowspan=6, columnspan=2)

bookList.bind('<<ListboxSelect>>', get_selected_row)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)  # positioning the scollbar


# Attaching Vertical Scrollbar and Book listbox together

# The vertical scrollbar along the y-axis will be set to "scrollbar"
bookList.configure(yscrollcommand=scrollbar.set)

# When you scroll the scrollbar "yview" i.e vertical view of bookList will change
scrollbar.configure(command=bookList.yview)

# Creating Buttons

viewAllBtn = Button(window, text="View All", width=12, command=view_command)
viewAllBtn.grid(row=2, column=3)

searchEntryBtn = Button(window, text="View Entry",
                        width=12, command=search_command)
searchEntryBtn.grid(row=3, column=3)

addEntryBtn = Button(window, text="Add Entry", width=12, command=add_command)
addEntryBtn.grid(row=4, column=3)

updateBtn = Button(window, text="Update", width=12)
updateBtn.grid(row=5, column=3)

deleteBtn = Button(window, text="Delete", width=12, command=delete_command)
deleteBtn.grid(row=6, column=3)

closeBtn = Button(window, text="Close", width=12, command=window.destroy)
closeBtn.grid(row=7, column=3)

window.wm_title("Bookstore")

window.mainloop()
