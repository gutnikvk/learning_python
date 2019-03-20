from tkinter import *


def openFile():
    fileName = entry.get()
    file = open(fileName, 'r')
    textArea.insert(1.0, file.read())
    file.close()


def saveFile():
    fileName = entry.get()
    file = open(fileName, 'w')
    file.write(textArea.get(1.0, END))
    file.close()


# declarations
index = Tk()
entry = Entry(
    index
)
openButton = Button(
    index,
    width=8,
    text='Open',
    command=openFile
)
saveButton = Button(
    index,
    width=8,
    text='Save',
    command=saveFile
)
textArea = Text(
    index
)
scrollbar = Scrollbar(textArea, command=textArea.yview)
entry.grid(row=0, column=0, sticky=E + W + S + N)
openButton.grid(row=0, column=1)
saveButton.grid(row=0, column=2)
textArea.grid(row=1, columnspan=3, sticky=E + W + S + N)
textArea.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
index.grid_columnconfigure(0, weight=1)
index.grid_rowconfigure(1, weight=1)
index.mainloop()
