from tkinter import *


def drawcircle():
    global X1, Y1, COULEUR
    can.create_oval(X1, Y1, X1 + 100, Y1 + 100, width=2, outline=COULEUR)


def changecoord():
    coord = [[20, 30], [120, 30], [220, 30], [70, 80], [170, 80]]
    coul = ['red', 'yellow', 'blue', 'green', 'black']
    global X1, Y1, COULEUR, INDEX

    X1, Y1 = coord[INDEX][0], coord[INDEX][1]
    COULEUR = coul[INDEX]
    INDEX += 1


def f():
    changecoord()
    drawcircle()


base = Tk()
can = Canvas(base, width=335, height=220, bg='white')
can.pack()
bou = Button(base, text="Quitter", command=base.quit)
bou.pack(side=RIGHT)

INDEX = 0
X1, Y1, COULEUR = 0, 0, ""
i = 0
while i <5:

    bou = Button(base, text="Cercle "+str(i), command=f)
    bou.pack(side=LEFT)
    i = i + 1

base.mainloop()
