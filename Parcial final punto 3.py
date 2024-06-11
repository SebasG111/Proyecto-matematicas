#---interfaz calculadora---
from tkinter import *
import tkinter as tk


def mk():
    convertir = float(valor.get())
    km = 1.60934
    resultado = km * convertir
    result.delete(0, tk.END)
    result.insert(0, str(resultado))



def gl():
    convertir = float(valor.get())
    l1 = 3.785411784
    resultado = l1 * convertir
    result.delete(0, tk.END)
    result.insert(0, str(resultado))



def lk():
    convertir = float(valor.get())
    lk1 = 0.45359237
    resultado = lk1 * convertir
    result.delete(0, tk.END)
    result.insert(0, resultado)



def mh():
    convertir = float(valor.get())
    mh1 = 1.60934
    resultado = mh1 * convertir
    result.delete(0, tk.END)
    result.insert(0, resultado)



if __name__=='__main__':
    calculadora = Tk()
    calculadora.geometry("350x350")
    calculadora.resizable(0,0)
    resultado = "55"
    #----Textos---#
    mensaje1 = tk.Label(calculadora,text="Valor a convertir")
    mensaje1.pack()
    #---Primer entry--#
    valor = tk.Entry(calculadora)
    valor.pack()
    #---Botones---#
    milla = tk.Button(calculadora, text="Milla a kilometro", width=20, height=1, command=mk)
    milla.place(x=20, y=100)
    galon = tk.Button(calculadora,text="Galon a litro",width=20,height=1,command=gl)
    galon.place(x=180,y=100)
    libra = tk.Button(calculadora, text="Libra a kilogramo", width=20,height=1,command=lk)
    libra.place(x=20, y=125)
    milla = tk.Button(calculadora, text="Milla/hora a Km/hora", width=20,height=1,command=mh)
    milla.place(x=180,y=125)
    #----Salida---#
    result = tk.Entry(calculadora)
    result.place(x=120,y=300)


    calculadora.mainloop()
