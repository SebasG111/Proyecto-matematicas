#----Giro de italia---#

from tkinter import *
import tkinter as tk
from tkinter import messagebox

contador = 0



def añadir():
    global contador
    contador += 1
    if contador <= 20:
        tabla[0].append(nombre.get())
        tabla[1].append(float(tiempo1.get()))
        tabla[2].append(float(tiempo2.get()))
        tabla[3].append(float(tiempo3.get()))
        tabla[4].append(float(tiempo4.get()))
        tabla[5].append(float(tiempo5.get()))
        print(tabla)
    else:
       mensajeAD = messagebox.showwarning("ADVERTENCIA","LIMITE DE PARTICIPANTES EXCEDIDO")

def imprimir():
   
   ganador = ""
   ganador1 = 99999999
   total1 = 0
   for i in range(len(tabla[0])):
    for k in range(1,5):
        total1 += tabla[k][i]
        if total1 < ganador1:
            ganador1 = total1
            ganador = tabla[k][i]
   resultados.insert("1.0", ganador)


    
           

       

def ver():
   resultados.delete("1.0",tk.END)
   for i in range(len(tabla)-1, -1, -1):
      for k in range(len(tabla[i])):
        resultados.insert("1.0", str(tabla[i][k])+"   ")
        if k == len(tabla[i])-1:
           resultados.insert("1.0", "\n")
   resultados.insert("1.0", "Resultados: ")
      
       


if __name__=='__main__':
    italia = Tk()
    italia.geometry("650x800")
    mensaje1 = tk.Label(italia, text="Giro de italia")
    mensaje1.pack()
    #---------#
    tabla = [[],
        [],
        [],
        [],
        [],
        []]
    #---------#
    mensaje_nombre = tk.Label(italia,text="Nombre del ciclista: ")
    mensaje_nombre.place(x=100,y=100)
    nombre = tk.Entry(italia)
    nombre.place(x=250,y=100)
    #-------#
    mensajeT1 = tk.Label(italia,text="Tiempo etapa 1:")
    mensajeT1.place(x=100,y=150)
    tiempo1 = tk.Entry(italia)
    tiempo1.place(x=250,y=150)
    #-------#
    tiempo2 = tk.Entry(italia)
    tiempo2.place(x=250,y=200)
    mensajeT2 = tk.Label(italia,text="Tiempo etapa 2:")
    mensajeT2.place(x=100,y=200)
    #-------#
    tiempo3 = tk.Entry(italia)
    tiempo3.place(x=250,y=250)
    mensajeT3 = tk.Label(italia,text="Tiempo etapa 3:")
    mensajeT3.place(x=100,y=250)
    #-------#
    tiempo4 = tk.Entry(italia)
    tiempo4.place(x=250,y=300)
    mensajeT4 = tk.Label(italia,text="Tiempo etapa 4:")
    mensajeT4.place(x=100,y=300)
    #-------#
    tiempo5 = tk.Entry(italia)
    tiempo5.place(x=250,y=350)
    mensajeT5 = tk.Label(italia,text="Tiempo etapa 5:")
    mensajeT5.place(x=100,y=350)
    #-------#
    guardar = tk.Button(italia,text="Guardar",width=20,command=añadir)
    ganador = tk.Button(italia,text="Ganador",width=20,command=imprimir)
    consultar = tk.Button(italia,text="Consultar",width=20,command=ver)
    guardar.place(x=100,y=420)
    ganador.place(x=250,y=420)
    consultar.place(x=400,y=420)
    #--------#
    resultados = tk.Text(italia,width=77,height=20)
    resultados.place(x=10,y=450)




    italia.mainloop()