import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import random
import threading
import time

# Configurar ventana principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ventana = ctk.CTk()
ventana.title("🦇 Reino Gótico 🦇")
ventana.geometry("800x600")
ventana.resizable(False, False)

# -------------------------------
# Fondo con Imagen
# -------------------------------

# Cargar imagen de fondo (asegúrate de tener un archivo .jpg o .png en la misma carpeta)
try:
    fondo_img = Image.open("fondo_castillo.jpg")  # Cambia por tu imagen
    fondo_img = fondo_img.resize((800, 600))
    fondo_foto = ImageTk.PhotoImage(fondo_img)

    fondo_label = tk.Label(master=ventana, image=fondo_foto)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print("No se pudo cargar la imagen de fondo.")

# -------------------------------
# Animación de Murciélagos
# -------------------------------

# Cargar imagen de murciélago (pequeño png)
try:
    murcielago_img = Image.open("murcielago.png")
    murcielago_img = murcielago_img.resize((50, 30))
    murcielago_foto = ImageTk.PhotoImage(murcielago_img)
except:
    murcielago_foto = None
    print("No se pudo cargar la imagen del murciélago.")

murcielagos = []

def mover_murcielagos():
    while True:
        for murcielago in murcielagos:
            x, y = murcielago.winfo_x(), murcielago.winfo_y()
            murcielago.place(x=x + random.choice([-2, -1, 0, 1, 2]), y=y + random.choice([1, 2]))
            if y > 600:
                murcielago.place(x=random.randint(0, 750), y=0)
        time.sleep(0.05)

def crear_murcielagos():
    for _ in range(5):  # 5 murciélagos
        lbl = tk.Label(master=ventana, image=murcielago_foto, bg="black")
        lbl.place(x=random.randint(0, 750), y=random.randint(0, 400))
        murcielagos.append(lbl)

# -------------------------------
# Juego de Acertijos Oscuros
# -------------------------------

acertijos = {
    "Siempre estoy delante, pero nunca puedo ser visto. ¿Qué soy?": "el futuro",
    "Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. ¿Qué soy?": "un mapa",
    "Cuanto más me quitas, más grande me vuelvo. ¿Qué soy?": "un agujero",
}

preguntas = list(acertijos.keys())
pregunta_actual = random.choice(preguntas)

def verificar_respuesta():
    respuesta = entrada_respuesta.get().strip().lower()
    correcta = acertijos.get(pregunta_actual, "")
    if respuesta == correcta:
        etiqueta_resultado.configure(text="¡Correcto, criatura de la noche! 🦇", text_color="green")
        nueva_pregunta()
    else:
        etiqueta_resultado.configure(text="No es correcto... piensa como un inmortal. ⚰️", text_color="red")

def nueva_pregunta():
    global pregunta_actual
    pregunta_actual = random.choice(preguntas)
    etiqueta_pregunta.configure(text=pregunta_actual)
    entrada_respuesta.delete(0, tk.END)

# Widgets del juego
etiqueta_pregunta = ctk.CTkLabel(ventana, text=pregunta_actual, font=("Georgia", 18), text_color="white", bg_color="#000000")
etiqueta_pregunta.place(x=100, y=100)

entrada_respuesta = ctk.CTkEntry(ventana, width=300)
entrada_respuesta.place(x=250, y=200)

boton_verificar = ctk.CTkButton(ventana, text="Verificar", command=verificar_respuesta, fg_color="#550000", hover_color="#AA0000")
boton_verificar.place(x=350, y=250)

etiqueta_resultado = ctk.CTkLabel(ventana, text="", font=("Georgia", 16))
etiqueta_resultado.place(x=280, y=320)

# -------------------------------
# Iniciar Animaciones
# -------------------------------
crear_murcielagos()
hilo_animacion = threading.Thread(target=mover_murcielagos, daemon=True)
hilo_animacion.start()

# -------------------------------
# Ejecutar app
# -------------------------------
ventana.mainloop()
