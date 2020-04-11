from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0
color = 'black'
tool = 'pencil'
oval = None

def change_tool(t):
    global tool
    tool = t
    if tool == 'pencil':
        canvas.bind("<ButtonPress-1>", dummy_func)
        canvas.bind("<ButtonRelease-1>", dummy_func)
        canvas.bind("<Button-1>", xy)
        canvas.bind("<B1-Motion>", addLine)
    elif tool == 'oval':
        canvas.bind("<Button-1>", dummy_func)
        canvas.bind("<B1-Motion>", show_oval)
        canvas.bind("<ButtonPress-1>", xy)
        canvas.bind("<ButtonRelease-1>", draw_oval)

def dummy_func(event):
    pass

def change_color(c):
    global color
    color = c

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    lastx, lasty = event.x, event.y

def draw_oval(event):
    global oval
    if oval:
        canvas.delete(oval)
    oval = None
    canvas.create_oval((lastx, lasty, event.x, event.y), fill=color)

def show_oval(event):
    global lastx, lasty, oval
    if oval:
        canvas.delete(oval)
    oval = canvas.create_oval((lastx, lasty, event.x, event.y), fill=color)



root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

red_btn = Button(root, text="Red", fg="red", command=lambda: change_color('red'))
blue_btn = Button(root, text="Blue", fg="blue", command=lambda: change_color('blue'))
oval_btn = Button(root, text="Oval tool", command=lambda: change_tool('oval'))
draw_btn = Button(root, text="Pencil tool", command=lambda: change_tool('pencil'))
red_btn.grid(column=0, row=1)
blue_btn.grid(column=0, row=2)
draw_btn.grid(column=0, row=3)
oval_btn.grid(column=0, row=4)
root.mainloop()