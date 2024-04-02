# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
import time
import datetime
def pyc():
        p=cajapalabra.get()
        c=cajaclave.get()
        if (p=="santo" or p=="Santo"):
                if (c=="sena" or c=="Sena"):
                        showinfo("Hora",datetime.datetime.now())
                else:
                        showinfo("Error","Clave no válida")
        else:

                showinfo("Error","Palabra no válida")

ventana=Tk()
ventana.title("Palabra y clave")
labelpyc=Label(ventana,text="Palabra y clave",fg="purple",font=("Gothic",30),height=2)
labelpyc.pack()
ventana.geometry("400x250+400+200")
label1=Label(ventana,text="Digite palabra",font=("Gothic",12))
label1.place(x=90,y=85)
label2=Label(ventana,text="Digite clave",font=("Gothic",12))
label2.place(x=90,y=115)
palabra=StringVar()
cajapalabra=Entry(ventana,textvariable=palabra)
cajapalabra.place(x=240,y=85)
clave=StringVar()
cajaclave=Entry(ventana,textvariable=clave)
cajaclave.place(x=240,y=115)
image=PhotoImage(file="a.gif")
angel = Label(ventana, image=image).place(x=50,y=150)
boton=Button(ventana,text="Listo",command=pyc)
boton.place(x=190,y=150)
ventana.mainloop()

