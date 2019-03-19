from tkinter import *


def strToSortedList(event):
    string = entry.get()
    list = string.split()
    list.sort()
    label['text'] = ' '.join(list)


# declarations
root = Tk()
entry = Entry(root, width=20)
button = Button(root, text='Transform')
label = Label(root, bg='black', fg='white', width=20)

# bindings
button.bind('<Button-1>', strToSortedList)

# packing to window
entry.pack()
button.pack()
label.pack()

# starting
root.mainloop()
