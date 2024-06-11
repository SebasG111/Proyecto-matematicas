from tkinter import *
import tkinter as tk
from tkinter import messagebox


def calvulate_val():
    palco1 = palco.get().upper()
    type2 = type1.get().upper()
    value1 = float(value.get())
    if palco1 == "PALCO":
        if type2 == "PREE-VENTA":
            final_value = value1 * 22000
        elif type2 == "VENTA NORMAL":
            final_value = value1 * 29000
        else:
            message1 = messagebox.showwarning(
                "WARNING", "THE TYPE VALUE IS INCORRECT")
    elif palco1 == "PLATEA":
        if type2 == "PREE-VENTA":
            final_value = value1 * 30000
        elif type2 == "VENTA NORMAL":
            final_value = value1 * 38000
        else:
            message1 = messagebox.showwarning(
                "WARNING", "THE TYPE VALUE IS INCORRECT")
    else:
        message2 = messagebox.showwarning(
            "WARNING", "THE LOCATE SELECT IS INCORRECT")
    aport = 0.15 * final_value
    finalV.delete(0, tk.END)
    finalV.insert(0, final_value)
    aportF.delete(0, tk.END)
    aportF.insert(0, aport)


if __name__ == '__main__':
    teater = Tk()
    teater.geometry("500x500")
    # ------#
    message4 = tk.Label(teater, text="Locate: ")
    message4.place(x=105, y=50)
    palco = tk.Entry(teater)
    palco.place(x=150, y=50)
    # ------#
    message5 = tk.Label(teater, text="Type: ")
    message5.place(x=110, y=75)
    type1 = tk.Entry(teater)
    type1.place(x=150, y=75)
    # ------#
    message6 = tk.Label(teater, text="Num: ")
    message6.place(x=110, y=100)
    value = tk.Entry(teater)
    value.place(x=150, y=100)
    # ------#
    calculate = tk.Button(teater, text="calculate", command=calvulate_val)
    calculate.place(x=200, y=150)
    # ------#
    finalV = tk.Entry(teater)
    message7 = tk.Label(teater, text="Total to pay: ")
    message7.place(x=80, y=180)
    aportF = tk.Entry(teater)
    message8 = tk.Label(teater, text="Aport: ")
    message8.place(x=80, y=200)
    finalV.place(x=170, y=180)
    aportF.place(x=170, y=200)
    teater.mainloop()
