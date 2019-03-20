from tkinter import *


def selectColor(event):
    label.config(text=event.widget['bg'])
    for color in colors:
        if colors[color] == event.widget['bg']:
            entry.delete(0, END)
            entry.insert(0, color)
            break


# declarations
root = Tk()
label = Label(
    root,
    width=50,
    justify=CENTER
)
entry = Entry(
    root,
    width=59,
    justify=CENTER
)
colors = {
    'red': '#ff0000',
    'orange': '#ff7d00',
    'yellow': '#ffff00',
    'green': '#00ff00',
    'light blue': '#007dff',
    'blue': '#0000ff',
    'violet': '#7d00ff'
}
buttons = {}
for color in colors:
    buttons[color] = Button(
        bg=colors[color],
        width=50
    )
    buttons[color].bind('<Button-1>', selectColor)
label.pack()
entry.pack()
for buttonKey in buttons:
    buttons[buttonKey].pack()
root.mainloop()
