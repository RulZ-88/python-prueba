import customtkinter as ctk
import tkinter as tk

# Configuración inicial de la ventana
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ventana = ctk.CTk()
ventana.title("Juego Secreto ❤️‍🔥")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Variables del juego
palabra_secreta = "dalia"

# Funciones
def verificar_palabra():
    intento = entrada.get().strip().lower()
    if intento == palabra_secreta:
        etiqueta_resultado.configure(text="¡ADIVINASTE JOJOJOJ ❤️‍🔥!", text_color="green")
    else:
        etiqueta_resultado.configure(text="Sigue adivinando 😏", text_color="red")

def mostrar_pista():
    etiqueta_pista.configure(text="Una mina que te comiste 😏😏❤️", text_color="pink")

# Widgets
titulo = ctk.CTkLabel(ventana, text="¡Bienvenido a mi juego, brodoo!", font=("Arial", 20))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(ventana, width=300, placeholder_text="Ingresa la palabra secreta")
entrada.pack(pady=10)

boton_verificar = ctk.CTkButton(ventana, text="Verificar", command=verificar_palabra)
boton_verificar.pack(pady=10)

boton_pista = ctk.CTkButton(ventana, text="Pedir una pista", command=mostrar_pista)
boton_pista.pack(pady=5)

etiqueta_pista = ctk.CTkLabel(ventana, text="", font=("Arial", 14))
etiqueta_pista.pack(pady=5)

etiqueta_resultado = ctk.CTkLabel(ventana, text="", font=("Arial", 16))
etiqueta_resultado.pack(pady=20)

# Función para usar "Enter" en vez de hacer click
def enter(event):
    verificar_palabra()

ventana.bind("<Return>", enter)

# Ejecutar la ventana
ventana.mainloop()
