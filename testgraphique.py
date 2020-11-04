from tkinter import *

fen1 = Tk()
text1 = Label(fen1, text='Hello world', fg='red')
text1.pack()
bou1 = Button(fen1, text='Quitter', command=fen1.destroy)
bou1.pack()
fen1.mainloop()
