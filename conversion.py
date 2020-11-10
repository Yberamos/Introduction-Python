from tkinter import *


def convertion_C_to_f(event):
    temp_c = eval(entry_celcius.get())
    tempf = (temp_c-32)/1.8
    varTF.set(str(tempf))


def convertion_f_to_C(event):
    temp_f = eval(entry_f.get())
    tempc = temp_f * 1.8 +32
    varTC.set(str(tempc))


fenetre = Tk()

Label(fenetre, text='Celcius: ').grid(row=1, sticky=E)
varTC = StringVar()
entry_celcius = Entry(fenetre, textvariable=varTC)
entry_celcius.bind("<Return>", convertion_C_to_f)
entry_celcius.grid(row=2, column=2)


Label(fenetre, text='F°: ').grid(row=2, sticky=E)
varTF = StringVar()
entry_f = Entry(fenetre, textvariable=varTF)
entry_f.grid(row=1, column=2)
entry_f.bind("<Return>", convertion_f_to_C)

fenetre.mainloop()
