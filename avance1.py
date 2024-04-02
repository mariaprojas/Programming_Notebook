# -*- coding: cp1252 -*-
import sys
from Tkinter import *
root =Tk()
root.title("PoluApp")
root.geometry("500x500")
root.config(bg="azure3")


widget = Label(None, text='Bienvenidos a PoluApp',height=3,fg = 'DeepPink2', font=('Elephant', 22),bg="azure3")
widget.pack()
 
etiqueta= Label(text="\n\n\n\nPoluApp pretende brindar informaci�n clara,\n respecto a los tipos de contaminaci�n m�s comunes,\n es decir, contaminaci�n del suelo, del agua,\n del aire, lum�nica y ac�stica.",bg="azure3",font=('LucidaHandwriting',12))
etiqueta.pack()
etiqueta1= Label(text="Creditos: \nYennifer Vega Rodriguez\n Maria Paula Rojas Ortega\n  Valentina Guevara Arango\n\n Universidad de Antioquia, 2017" ,bg="azure3",width=50, height=50, anchor="s",font=('Arial', 7)) 
etiqueta1.pack()
img=PhotoImage(file="flechaverde.gif")
logoimg=PhotoImage(file="logo.gif")
def menu():
  opcion=0
  while (opcion<1 or opcion>5):
    print("Tipos de contaminaci�n")
    print("1. Contaminaci�n luminica")
    print("2. Contaminaci�n del agua")
    print("3. Contaminaci�n del suelo")
    print("4. Contaminaci�n del aire")
    print("5. Terminar")
    opcion=input("Digite la opcion 1-5:")
  return opcion
  menu()
  opcion=menu()
  while opcion<1 or opcion>5:
    print("opcion invalida")
    opcion=menu()
  while opcion!=5:
    if opcion==1:
      print"\n\n"
      print "Contaminacion luminica"
      print "Consiste en el brillo del cielo nocturno producido por la mala calidad del alumbrado de nuestras ciudades. Esto significa que enviamos la luz hacia arriba en vez de enviarla hacia el suelo, donde realmente se necesita."
      print "Dedic�ndonos a iluminar el cielo no s�lo derrochamos nuestro dinero sino que abusamos de los recursos naturales, agredimos el h�bitat de animales nocturnos y migratorios, y arrebatamos a nuestros hijos la contemplaci�n del cielo estrellado."
    elif opcion==2:
      print"\n\n"
      print "Contaminacion del agua"  
      print "El agua que procede de fuentes superficiales (r�os, lagos y quebradas), es objeto d�a a d�a de una severa contaminaci�n, producto de las actividades del hombre; �ste agrega al agua sustancias ajenas a su composici�n, modificando la calidad de �sta. Se dice que est� contaminada pues no puede utilizarse como generalmente se hace."
    elif opcion==3:
      print"\n\n"
      print "Contaminacion del suelo"  
      print "El suelo se contamina cuando una sustancia, que no pertenece a este, sin importar su estado o composicion hace contacto con �l,debido al uso de pesticidas para la agricultura; por riego con agua contaminada; por el polvo de zonas urbanas y las carreteras; o por los relaves mineros y desechos industriales derramados en su superficie, depositados en estanques o enterrados. "
    elif opcion==4:
      print"\n\n"
      print "En construcci�n"  
    elif opcion==5:
      print("Fin del programa")
      print "\n\n"
  opcion=menu()
flechav = Button(root,image=img,height=31,width=31,command=menu,bg="azure3").place(x=420,y=430)
logo= Label(image=logoimg,height=62,width=62,bg="azure3").place(x=228,y=100)



root.mainloop()
