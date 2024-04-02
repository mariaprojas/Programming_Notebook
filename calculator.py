from Tkinter import *
def Operacion():
    n1=float(cajaop1.get())
    n2=float(cajaop2.get())
    op=cajaoperando1.get()
    if op=='+':
        suma= n1+n2
        resul=StringVar()
        resul.set(suma)
        labelr=Label(root,textvariable=resul)
        labelr.place(x=250,y=210)
    elif op=='-':
        resta=n1-n2
        resul=StringVar()
        resul.set(resta)
        labelr=Label(root,textvariable=resul)
        labelr.place(x=250,y=210)
    elif op=='*':
        multiplicacion=n1*n2
        resul=StringVar()
        resul.set(multiplicacion)
        labelr=Label(root,textvariable=resul)
        labelr.place(x=250,y=210)
    elif op=='/':
        division=n1/n2
        resul=StringVar()
        resul.set(division)
        labelr=Label(root,textvariable=resul)
        labelr.place(x=250,y=210)
    elif op=='%':
        modulo=n1%n2
        resul=StringVar()
        resul.set(division)
        labelr=Label(root,textvariable=resul)
        labelr.place(x=250,y=210)
        
root=Tk()
root.title ("Calculator")
root.geometry ("400x250+400+200")
Labelcalculator=Label(root,text="Calculator",fg="purple",font=("Gothic",30),height=2)
Labelcalculator.pack()
op1=Label(root,text="op1",height=2,fg="blue",font="Gothic")
op1.pack()
operador1=StringVar()
cajaop1=Entry(root,textvariable=operador1)
cajaop1.place(x=250,y=95)
op2=Label(root,text="op2",height=2,fg="blue",font="Gothic")
op2.pack()
operador2=StringVar()
cajaop2=Entry(root,textvariable=operador2)
cajaop2.place(x=250,y=132)
operando=Label(root,text="operando",height=2,fg="blue",font="Gothic")
operando.pack()
operando1=StringVar()
cajaoperando1=Entry(root,textvariable=operando1)
cajaoperando1.place(x=250,y=172)
resultado=Label(root,text="resultado",height=2,fg="blue",font="Gothic")
resultado.pack()
bottom1=Button(root,text="Calcular",command= Operacion)
bottom1.pack()
root.mainloop()
