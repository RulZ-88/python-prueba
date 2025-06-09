import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw() 

contraseña = simpledialog.askstring("Contraseña", "Ingrese su contraseña:", show='*')

print("Contraseña ingresada:", contraseña)