import customtkinter as ctk
import random
import pygame

# Inicializar pygame para música
pygame.mixer.init()
pygame.mixer.music.load("chrono.mp3")  # Cambia el nombre si quieres
pygame.mixer.music.play(-1)  # Música infinita

# Configurar apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Crear ventana
ventana = ctk.CTk()
ventana.title("¡SUPER Adivina el Número!")
ventana.geometry("600x450")

# Número aleatorio y contador
numero_secreto = random.randint(1, 100)
intentos = 0

# Función para verificar número
def verificar(event=None):
    global intentos
    intento = entrada.get()
    if intento.isdigit():
        intento = int(intento)
        intentos += 1
        if intento == numero_secreto:
            resultado.configure(text=f"🎉¡Ganaste en {intentos} intentos!🎉", text_color="lime", font=("Arial", 24))
            ventana.configure(fg_color="purple")  # Cambia fondo
            entrada.configure(state="disabled")  # Desactiva entrada
        elif intento < numero_secreto:
            resultado.configure(text="📉 ¡Demasiado bajo!", text_color="orange", font=("Arial", 20))
        else:
            resultado.configure(text="📈 ¡Demasiado alto!", text_color="orange", font=("Arial", 20))
    else:
        resultado.configure(text="⚠️ Ingresa un número válido.", text_color="yellow", font=("Arial", 20))
    entrada.delete(0, "end")  # Borra entrada

# Widgets
titulo = ctk.CTkLabel(ventana, text="Adivina el número (1-100)", font=("Arial Black", 28))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(ventana, placeholder_text="Escribe un número y presiona ENTER", width=300)
entrada.pack(pady=10)

resultado = ctk.CTkLabel(ventana, text="", font=("Arial", 18))
resultado.pack(pady=30)

# Enlazar Enter
ventana.bind('<Return>', verificar)

# Ejecutar ventana
ventana.mainloop()
