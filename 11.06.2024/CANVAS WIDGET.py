#The Canvas widget lets us display various graphics on the application. It can be used to draw simple shapes to complicated graphs. We can also display various kinds of custom widgets according to our needs.
'''C = Canvas(root, height, width, bd, bg, ..)'''
#Some common drawing methods:
#Creating an Oval
 oval = C.create_oval(x0, y0, x1, y1, options)

#Creating an arc
 arc = C.create_arc(20, 50, 190, 240, start=0, extent=110, fill="red")

#Creating a Line
 line = C.create_line(x0, y0, x1, y1, ..., xn, yn, options)

#Creating a polygon
 oval = C.create_polygon(x0, y0, x1, y1, ...xn, yn, options)

#EXAMPLE:
from tkinter import *


root = Tk()

C = Canvas(root, bg="yellow",
		height=250, width=300)

line = C.create_line(108, 120,
					320, 40,
					fill="green")

arc = C.create_arc(180, 150, 80,
				210, start=0,
				extent=220,
				fill="red")

oval = C.create_oval(80, 30, 140,
					150,
					fill="blue")

C.pack()
mainloop()
