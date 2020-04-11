from tkinter import *
from tkinter import ttk
from tkmacosx import Button
from tkinter.colorchooser import askcolor


lastx = 0
lasty = 0
color = "Black"
tool = "Pencil"
pencil_size = 2
oval = None
rectangle = None
shape_outline = 1
list_points = []
tmp_line = []


def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def clear_all():
    canvas.delete("all")

def pencil_draw(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color, width = pencil_size, capstyle = ROUND)
    lastx, lasty = event.x, event.y

def brush_draw(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color, width = pencil_size, capstyle = PROJECTING)
    lastx, lasty = event.x, event.y

def show_oval(event):
    global lastx, lasty, oval, shape_outline
    shape_outline = scale_outline.get() 
    if oval:
        canvas.delete(oval)
    oval = canvas.create_oval((lastx, lasty, event.x, event.y), fill = color, width = shape_outline)

def oval_draw(event):
    global oval, shape_outline
    shape_outline = scale_outline.get() 
    if oval:
        canvas.delete(oval)
    oval = None
    canvas.create_oval((lastx, lasty, event.x, event.y), fill = color, width = shape_outline)

def show_rectangle(event):
    global lastx, lasty, rectangle, shape_outline
    shape_outline = scale_outline.get()
    if rectangle:
        canvas.delete(rectangle)
    canvas.create_rectangle((lastx, lasty, event.x, event.y), fill = color, width = shape_outline)

def rectangle_draw(event):
    global rectangle, shape_outline
    shape_outline = scale_outline.get() 
    if rectangle:
        canvas.delete(rectangle)
    rectangle = None
    canvas.create_rectangle((lastx, lasty, event.x, event.y), fill = color, width = shape_outline)

def erase(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill="White", width = pencil_size, capstyle = ROUND, smooth = TRUE)
    lastx, lasty = event.x, event.y

def change_size(s):
    global pencil_size 
    pencil_size = s

def choose_other_color():
    global color
    color = askcolor(color = color)[1]
    btn_c_other.configure(fg = color)

def get_points(event):
    global list_points, lastx, lasty, tmp_line
    list_points.append(event.x)
    list_points.append(event.y)
    if len(list_points) > 2:
        tmp_line.append(canvas.create_line((lastx, lasty, event.x, event.y), width = 1, fill = "Cyan"))
    lastx, lasty = event.x, event.y
    
    
def draw_polygon(event):
    global list_points, tmp_line, shape_outline
    shape_outline = scale_outline.get()
    canvas.create_polygon(list_points, fill = color, width = shape_outline, outline = "Black")
    for i in tmp_line:
        canvas.delete(i)
    list_points = []
    tmp_line = []

def change_color(c):
    global color
    color = c

def do_nothing(event):
    pass

def change_tool(tool):
    if tool == 'pencil':
        canvas.bind("<Button-1>", xy)
        canvas.bind("<B1-Motion>", pencil_draw)
        canvas.bind("<ButtonPress-1>", xy)
        canvas.bind("<ButtonRelease-1>", pencil_draw)
    elif tool == 'brush':
        canvas.bind("<Button-1>", xy)
        canvas.bind("<B1-Motion>", brush_draw)
        canvas.bind("<ButtonPress-1>", xy)
        canvas.bind("<ButtonRelease-1>", brush_draw)
    elif tool == 'eraser':
        canvas.bind("<Button-1>", xy)
        canvas.bind("<B1-Motion>", erase)
        canvas.bind("<ButtonPress-1>", xy)
        canvas.bind("<ButtonRelease-1>", erase)
    elif tool == 'circle':
        canvas.bind("<Button-1>", do_nothing)
        canvas.bind("<B1-Motion>", show_oval)
        canvas.bind("<ButtonPress-1>", xy)
        canvas.bind("<ButtonRelease-1>", oval_draw)
    elif tool == 'rectangle':
        canvas.bind("<Button-1>", do_nothing)
        canvas.bind("<B1-Motion>", show_rectangle)
        canvas.bind("<ButtonPress-1>", xy)
        canvas.bind("<ButtonRelease-1>", rectangle_draw)
    elif tool == 'polygon':
        canvas.bind("<Button-1>", do_nothing)
        canvas.bind("<B1-Motion>", do_nothing)
        canvas.bind("<ButtonPress-1>", get_points)
        canvas.bind("<ButtonRelease-1>", do_nothing)
        canvas.bind('<Double-Button-1>', draw_polygon)
        

root = Tk()

root.geometry('800x600')
root.title('Pawitra Paint')
root.configure(background = '#DBDBDB')

color_paper = "White"
color_frame_left = "#DBF3F9"
color_c_button_bg = "#EBF5FB"

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame1 = Frame(root, width = 100, height = 600, background = color_frame_left)
frame1.grid(row = 0, column = 0, sticky="NSEW")

canvas = Canvas(root, width = 680, heigh = 580, background = color_paper, highlightbackground = "gray", highlightthickness = 1)
canvas.grid(row = 0, column = 1, padx = 5, pady = 5, sticky="NSEW")

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", pencil_draw)


# TOOLS

## ROW 0
label_tools = Label(frame1, text = 'Tools', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 0, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 1
btn_pencil = Button(frame1, text = 'Pencil',  width = 100, height = 30, font = ("Helvetica", 14), command = lambda: change_tool('pencil'))
btn_pencil.grid(row = 1, columnspan = 3, padx = 4, pady = 2, sticky = "NEWS")

## ROW 2
btn_brush = Button(frame1, text = 'Brush', width = 100, height = 30, font = ("Helvetica", 14), command = lambda: change_tool('brush'))
btn_brush.grid(row = 2, columnspan = 3, padx = 4, pady = 2, sticky = "NEWS")

## ROW 3
btn_circle = Button(frame1, text = '〇', width = 30, height = 30, font = ("Helvetica", 14), command = lambda: change_tool('circle'))
btn_circle.grid(row = 3, column = 0, padx = 1, pady = 2, sticky = "E")
btn_rectangle = Button(frame1, text = '▢', width = 30, height = 30, font = ("Helvetica", 14), command = lambda: change_tool('rectangle'))
btn_rectangle.grid(row = 3, column = 1, padx = 1, pady = 2, sticky = "NEWS")
btn_polygon = Button(frame1, text = '⬠', width = 30, height = 30, font = ("Helvetica", 14), command = lambda: change_tool('polygon'))
btn_polygon.grid(row = 3, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 4
btn_erase = Button(frame1, text = 'Eraser', width = 100, height = 30, font = ("Helvetica", 14), command = lambda: change_tool('eraser'))
btn_erase.grid(row = 4, columnspan = 3, pady = 2, padx = 4, sticky = "NEWS")

## ROW 5
label_tools = Label(frame1, text = 'Line size', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 5, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 6
btn_size_1 = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 10), command = lambda: change_size(2))
btn_size_1.grid(row = 6, column = 0, padx = 1, pady = 2, sticky = "E")
btn_size_2 = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 16), command = lambda: change_size(5))
btn_size_2.grid(row = 6, column = 1, padx = 1, pady = 2, sticky = "NEWS")
btn_size_3 = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 24), command = lambda: change_size(10))
btn_size_3.grid(row = 6, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 7
label_tools = Label(frame1, text = 'Shape outline', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 7, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 8
scale_outline = Scale(frame1, from_=0, to=10, orient=HORIZONTAL, bg = "sky blue", showvalue = 0 ,takefocus = 0)
scale_outline.grid(row = 8, columnspan = 3, padx = 4, sticky = "NSEW")

# COLORS

## ROW 9
label_tools = Label(frame1, text = 'Colors', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 9, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 10
btn_c_black = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Black", command = lambda: change_color("Black"))
btn_c_black.grid(row = 10, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_gray = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Gray", command = lambda: change_color("Gray"))
btn_c_gray.grid(row = 10, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_white = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "White", command = lambda: change_color("White"))
btn_c_white.grid(row = 10, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 11
btn_c_navy = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Navy", command = lambda: change_color("Navy"))
btn_c_navy.grid(row = 11, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_blue = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Blue", command = lambda: change_color("Blue"))
btn_c_blue.grid(row = 11, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_cyan = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Cyan", command = lambda: change_color("Cyan"))
btn_c_cyan.grid(row = 11, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 12
btn_c_green = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Green", command = lambda: change_color("Green"))
btn_c_green.grid(row = 12, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_olive = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Olive", command = lambda: change_color("Olive"))
btn_c_olive.grid(row = 12, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_lime = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Lime", command = lambda: change_color("Lime"))
btn_c_lime.grid(row = 12, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 13
btn_c_red = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Red", command = lambda: change_color("Red"))
btn_c_red.grid(row = 13, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_orange = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Orange", command = lambda: change_color("Orange"))
btn_c_orange.grid(row = 13, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_yellow = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Yellow", command = lambda: change_color("Yellow"))
btn_c_yellow.grid(row = 13, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 14
btn_c_brown = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Brown", command = lambda: change_color("Brown"))
btn_c_brown.grid(row = 14, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_purple = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Purple", command = lambda: change_color("Purple"))
btn_c_purple.grid(row = 14, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_pink = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Pink", command = lambda: change_color("Pink"))
btn_c_pink.grid(row = 14, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 15
label_tools = Label(frame1, text = 'other', font = ("Helvetica", 12), bg = color_frame_left)
label_tools.grid(row = 15, column = 0, pady = 2, sticky = "NSEW")
btn_c_other = Button(frame1, text = '●', width = 62, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Black", command = choose_other_color)
btn_c_other.grid(row = 15, column = 1, columnspan = 2, padx = 4, pady = 2, sticky = "WE")


## ROW 16
btn_clear = Button(frame1, text = 'Clear all',  width = 100, height = 30, font = ("Helvetica", 14), bg = '#EA6653', fg = "White", command = clear_all)
btn_clear.grid(row = 16, columnspan = 3, padx = 4, pady = 30, sticky = "NEWS")

root.mainloop()