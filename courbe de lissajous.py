from tkinter import *
from math import sin, cos


def move():
    global x, y, angle
    angle = angle + 0.1

    xp, yp = x, y

    x = sin(2*angle)
    y = cos(3*angle)

    x, y = x * 120 + 150, y * 120 + 150
    can.coords(balle, x - 10, y - 10, x + 10, y + 10)
    can.create_line(xp, yp, x, y, fill="blue")


x, y, angle = 150., 270., 0
fenetre = Tk()
fenetre.title('Courbes de Lissajous')

can = Canvas(fenetre, height=300, width=300, bg='ivory')
can.pack()

Button(fenetre, text='Go', command=move).pack()


balle = can.create_oval(x-10, y-10, x+10, y+10, fill='red', width=1)

fenetre.mainloop()
