from tkinter import *
from tkinter import ttk
from tkmacosx import Button

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
frame2 = Frame(root, width = 680, heigh = 580, background = color_paper, highlightbackground = "gray", highlightthickness = 1)
frame1.grid(row = 0, column = 0, sticky="NSEW")
frame2.grid(row = 0, column = 1, padx = 5, pady = 5, sticky="NSEW")

# TOOLS

## ROW 0
label_tools = Label(frame1, text = 'Tools', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 0, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 1
btn_pencil = Button(frame1, text = 'Pencil',  width = 100, height = 30, font = ("Helvetica", 14))
btn_pencil.grid(row = 1, columnspan = 3, padx = 4, pady = 2, sticky = "NEWS")

## ROW 2
btn_brush = Button(frame1, text = 'Brush', width = 100, height = 30, font = ("Helvetica", 14))
btn_brush.grid(row = 2, columnspan = 3, padx = 4, pady = 2, sticky = "NEWS")

## ROW 3
btn_circle = Button(frame1, text = '〇', width = 30, height = 30, font = ("Helvetica", 14))
btn_circle.grid(row = 3, column = 0, padx = 1, pady = 2, sticky = "E")
btn_rectangle = Button(frame1, text = '▢', width = 30, height = 30, font = ("Helvetica", 14))
btn_rectangle.grid(row = 3, column = 1, padx = 1, pady = 2, sticky = "NEWS")
btn_triangle = Button(frame1, text = '△', width = 30, height = 30, font = ("Helvetica", 14))
btn_triangle.grid(row = 3, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 4
btn_erase = Button(frame1, text = 'Eraser', width = 100, height = 30, font = ("Helvetica", 14))
btn_erase.grid(row = 4, columnspan = 3, pady = 2, padx = 4, sticky = "NEWS")

## ROW 5
label_tools = Label(frame1, text = 'Size', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 5, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 6
btn_size_1 = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 10))
btn_size_1.grid(row = 6, column = 0, padx = 1, pady = 2, sticky = "E")
btn_size_2 = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 16))
btn_size_2.grid(row = 6, column = 1, padx = 1, pady = 2, sticky = "NEWS")
btn_size_3 = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 24))
btn_size_3.grid(row = 6, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 7
label_tools = Label(frame1, text = 'Transparent', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 7, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 8
scale_transparen = Scale(frame1, from_=0, to=10, orient=HORIZONTAL, bg = color_frame_left, showvalue = 0)
scale_transparen.grid(row = 8, columnspan = 3, padx = 4, sticky = "NSEW")

# COLORS

## ROW 9
label_tools = Label(frame1, text = 'Colors', font = ("Helvetica", 14), bg = color_frame_left)
label_tools.grid(row = 9, columnspan = 3, pady = 2, sticky = "NSEW")

## ROW 10
btn_c_black = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Black")
btn_c_black.grid(row = 10, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_gray = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Gray")
btn_c_gray.grid(row = 10, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_white = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "White")
btn_c_white.grid(row = 10, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 11
btn_c_navy = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Navy")
btn_c_navy.grid(row = 11, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_blue = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Blue")
btn_c_blue.grid(row = 11, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_cyan = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Cyan")
btn_c_cyan.grid(row = 11, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 12
btn_c_green = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Green")
btn_c_green.grid(row = 12, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_olive = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Olive")
btn_c_olive.grid(row = 12, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_lime = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Lime")
btn_c_lime.grid(row = 12, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 13
btn_c_red = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Red")
btn_c_red.grid(row = 13, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_orange = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Orange")
btn_c_orange.grid(row = 13, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_yellow = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Yellow")
btn_c_yellow.grid(row = 13, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 14
btn_c_brown = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Brown")
btn_c_brown.grid(row = 14, column = 0, padx = 1, pady = 2, sticky = "E")
btn_c_purple = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Purple")
btn_c_purple.grid(row = 14, column = 1, padx = 1, pady = 2, sticky = "EW")
btn_c_pink = btn_circle = Button(frame1, text = '●', width = 30, height = 30, font = ("Helvetica", 30),  bg = color_c_button_bg, fg = "Pink")
btn_c_pink.grid(row = 14, column = 2, padx = 1, pady = 2, sticky = "W")

## ROW 15
label_tools = Label(frame1, text = 'other', font = ("Helvetica", 12), bg = color_frame_left)
label_tools.grid(row = 15, column = 0, pady = 2, sticky = "NSEW")
btn_c_other = Button(frame1, text = '●', width = 62, height = 30, font = ("Helvetica", 30), bg = color_c_button_bg, fg = "Black")
btn_c_other.grid(row = 15, column = 1, columnspan = 2, padx = 4, pady = 2, sticky = "WE")


root.mainloop()