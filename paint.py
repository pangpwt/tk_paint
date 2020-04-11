from tkinter import *
from tkinter import ttk
from tkmacosx import Button

root = Tk()

root.geometry('800x600')
root.title('Pawitra Paint')
root.configure(background = '#DBDBDB')

color_paper = "White"
color_frame_left = "#DBF3F9"

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

root.mainloop()