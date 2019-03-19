from tkinter import *


def add(event):
    summand1 = float(entry1.get())
    summand2 = float(entry2.get())
    resultLabel['text'] = summand1 + summand2


def multiply(event):
    multiplicand = float(entry1.get())
    multiplier = float(entry2.get())
    resultLabel['text'] = multiplicand * multiplier


def subtract(event):
    minuend = float(entry1.get())
    subtrahend = float(entry2.get())
    resultLabel['text'] = minuend - subtrahend


def divide(event):
    dividend = float(entry1.get())
    divisor = float(entry2.get())
    resultLabel['text'] = dividend / divisor


# declarations
root = Tk()
inputBlock = Frame(root)
resultBlock = Frame(root)
entry1 = Entry(inputBlock, width=20)
entry2 = Entry(inputBlock, width=20)
multButton = Button(inputBlock, text='*', width=5)
multButton.bind('<Button-1>', multiply)
addButton = Button(inputBlock, text='+', width=5)
addButton.bind('<Button-1>', add)
subtrButton = Button(inputBlock, text='-', width=5)
subtrButton.bind('<Button-1>', subtract)
divButton = Button(inputBlock, text='/', width=5)
divButton.bind('<Button-1>', divide)
resultLabel = Label(resultBlock, width=20)

# packing up
inputBlock.pack()
entry1.pack()
entry2.pack()
multButton.pack(side=LEFT)
addButton.pack(side=LEFT)
subtrButton.pack(side=LEFT)
divButton.pack(side=LEFT)
resultBlock.pack(side=BOTTOM)
resultLabel.pack(side=BOTTOM)

# starting
root.mainloop()
