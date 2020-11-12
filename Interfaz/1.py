import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

#FUNCION SUMA
def sumar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA+numeroB
    NR.set(numeroR)
    limpiarCampos()

#FUNCION RESTA
def restar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA-numeroB
    NR.set(numeroR)
    limpiarCampos()

#FUNCION MULTIPLICACION
def multiplicacion():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA*numeroB
    NR.set(numeroR)
    limpiarCampos()

#FUNCION DIVISION
def division():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA/numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana=tk.Tk()
ventana.config(width=400,height=400)

#NA
etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)

#NB
etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)

#NR
etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)


#SUMA
botonTransportarS=Button(ventana,text="Sumar A y B", command=sumar)
botonTransportarS.place(x=0,y=90)

#RESTA
botonTransportarR=Button(ventana,text="Restar A y B", command=restar)
botonTransportarR.place(x=0,y=120)

#MULTIPLICACION
botonTransportarM=Button(ventana,text="Multiplicar A y B", command=multiplicacion)
botonTransportarM.place(x=0,y=150)

#DIVISION
botonTransportarD=Button(ventana,text="Dividir A y B", command=division)
botonTransportarD.place(x=0,y=180)

ventana.mainloop()
