#--Ejercicio 4--#
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def total():
    kids1 = int(kids.get())
    adults1 = int(adults.get())
    dia1 = dia.get().upper()
    if dia1 == "VIERNES" or dia1 == "JUEVES":
        kids2 = 5000 * kids1
        adults2 = 7000 * adults1
        total1 = adults2 + kids2
        totalP.delete(0, tk.END)
        totalP.insert(0, str(total1))
    elif dia1 == "SABADO" or dia1 == "DOMINNGO":
        kids1 = 8000 * kids1
        adults1 = 10000 * adults1
        total1 = adults1 + kids1
        totalP.delete(0,tk.END)
        totalP.insert(0, total1)
    else:
        mensaje4 = messagebox.showwarning("error","ingrese un dia valido")




if __name__=='__main__':
    club = Tk()
    club.geometry("300x300")
    club.resizable(0,0)
    mensaje1 = tk.Label(club,text="Dia de la semana")
    mensaje1.place(x=30,y=50)
    dia = tk.Entry(club)
    dia.place(x=130,y=50)
    #------#
    mensaje2 = tk.Label(club,text="Cantidad de niños")
    mensaje2.place(x=23,y=100)
    kids = tk.Entry(club)
    kids.place(x=130,y=100)
    #------#
    mensaje3 = tk.Label(club,text="Cantidad de adultos")
    mensaje3.place(x=13,y=150)
    adults = tk.Entry(club)
    adults.place(x=130,y=150)
    #---Boton calcular--#
    calcular = tk.Button(club,text="Calcular",command=total)
    calcular.place(x=125,y=215)
    #---Total a pagar--#
    totalP = tk.Entry(club)
    totalP.place(x=90,y=250)
    








    club.mainloop()