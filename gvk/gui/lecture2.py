from tkinter import *

# declarations
root = Tk()
button = Button(
    text='Change',
    width=15,
    height=3
)


def changeAppearance():
    button.config(
        text='Changed',
        bg='#000000',
        activebackground='#555555',
        fg='#ffffff',
        activeforeground='#ffffff'
    )


button.config(command=changeAppearance)
button.pack()
root.mainloop()
