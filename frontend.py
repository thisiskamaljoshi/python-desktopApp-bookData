from tkinter import *

window = Tk()

labelTitle = Label(window, text="Title")
labelTitle.grid(row=0, column=0)

labelYear = Label(window, text="Year")
labelYear.grid(row=0, column=2)

labelAuthor = Label(window, text="Author")
labelAuthor.grid(row=1, column=0)

labelISBN = Label(window, text="ISBN")
labelISBN.grid(row=1, column=2)

text_title = StringVar()
titleEntry = Entry(window, textvariable=text_title)
titleEntry.grid(row=0, column=1)

text_year = StringVar()
yearEntry = Entry(window, textvariable=text_year)
yearEntry.grid(row=0, column=3)

text_Author = StringVar()
AuthorEntry = Entry(window, textvariable=text_Author)
AuthorEntry.grid(row=1, column=1)

text_ISBN = StringVar()
ISBNEntry = Entry(window, textvariable=text_ISBN)
ISBNEntry.grid(row=1, column=3)

bookList = Listbox(window, height=6, width=35)
bookList.grid(row=2, column=0, rowspan=6, columnspan=2)

window.mainloop()
