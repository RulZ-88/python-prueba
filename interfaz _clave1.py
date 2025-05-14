import tkinter as tk
from tkinter import messagebox

clave_correcta = "1989"

def verificar_clave():
    clave_ingresada = entrada_clave.get()
    if clave_ingresada == clave_correcta:
        messagebox.showinfo("Acceso Permitido", "hola amorcito rico  :3")
        ventana.quit()
    else:
        mensaje.set("Clave incorrecta")
        boton_pista.config(state=tk.NORMAL)

def mostrar_pista():
    messagebox.showinfo("Pista", "Es su año de nacimiento bobiña :p" )

