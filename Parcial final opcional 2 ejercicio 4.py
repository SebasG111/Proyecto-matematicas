#---Hotel---#
from tkinter import *
import tkinter as tk
from tkinter import messagebox


def reservar1():
    piso1 = int(ps.get())
    edificios1 = int(ed.get())
    habitacion1 = int(hb.get())
    if edificios1 == 1:
        edificio1[piso1-1][habitacion1-1] = TRUE
    elif edificios1 == 2:
        edificio2[piso1-1][habitacion1-1] = TRUE
    elif edificios1 == 3:
        edificio3[piso1-1][habitacion1-1] = TRUE
    else:
        ad = messagebox.showwarning("ADVERTENCIA", "VERIFIQUE SI A INGRESADO TODOS LOS DATOS")



def verf():
    piso1 = int(ps.get())
    edificios1 = int(ed.get())
    habitacion1 = int(hb.get())
    if edificios1 == 1:
        if edificio1[piso1-1][habitacion1-1] == FALSE:
            print("disponible")
        else:
            print("no disponible")
    elif edificios1 == 2:
        if edificio2[piso1-1][habitacion1-1] == FALSE:
            print("disponible")
        else:
            print("no disponible")
    elif edificios1 == 3:
        if edificio3[piso1-1][habitacion1-1] == FALSE:
            print("disponible")
        else:
            print("no disponible")
    else:
        ad = messagebox.showwarning("ADVERTENCIA", "VERIFIQUE SI A INGRESADO TODOS LOS DATOS")



def despejar():
    piso1 = int(ps.get())
    edificios1 = int(ed.get())
    habitacion1 = int(hb.get())
    if edificios1 == 1:
        edificio1[piso1-1][habitacion1-1] = FALSE
    elif edificios1 == 2:
        edificio2[piso1-1][habitacion1-1] = FALSE
    elif edificios1 == 3:
        edificio3[piso1-1][habitacion1-1] = FALSE
    else:
        ad = messagebox.showwarning("ADVERTENCIA", "VERIFIQUE SI A INGRESADO TODOS LOS DATOS")



if __name__=='__main__':
    hotel = Tk()
    hotel.geometry("650x650")
    hotel.resizable(0,0)
    edificio1 = [[FALSE for i in range(1,21)] for k in range(1,16)]
    edificio2 = [[FALSE for i in range(1,21)] for k in range(1,16)]
    edificio3 = [[FALSE for i in range(1,21)] for k in range(1,16)]
    #------#
    edificios = [i for i in range(1,4)]
    ed = tk.StringVar()
    mensaje1 = tk.Label(hotel,text="Elegir un edificio: ")
    edificio = tk.OptionMenu(hotel, ed, *edificios)
    edificio.pack()
    #-------#
    mensaje2 = tk.Label(hotel, text="Ingrese el piso: ")
    pisos = [i for i in range(1,16)]
    ps = StringVar()
    piso = tk.OptionMenu(hotel, ps, *pisos)
    piso.pack()
    #-------#
    mensaje3 = tk.Label(hotel,text="Escoja su habitacion: ")
    habitaciones = [i for i in range(1,21)]
    hb = tk.StringVar()
    habitacion = tk.OptionMenu(hotel, hb,*habitaciones)
    habitacion.pack()
    #-------#
    reservar = tk.Button(hotel, text="Reservar", command=reservar1)
    reservar.pack()
    #-------#
    disponibilidad = tk.Button(hotel, text="Disponibilidad", command=verf)
    disponibilidad.pack()
    #-------#
    liberar = tk.Button(hotel, text="Desocupar", command=despejar)
    liberar.pack()




    hotel.mainloop()
