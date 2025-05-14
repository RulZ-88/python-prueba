import pygame

# Inicializar pygame para música
pygame.mixer.init()
pygame.mixer.music.load("chrono.mp3")  # Cambia el nombre del archivo si es necesario
pygame.mixer.music.play(-1)

print(
"""\033[91m
+================================+
| ¡Bienvenida, bebé! 💕          |
| Introduce una palabra          |
| y adivina qué palabra eh       |
| elegido para ti. ❤️            |
| ¿Cuál es la palabra secreta?   |
+================================+
"""
)

palabra_secreta = "potito"
adivinanza = input("Ingresa la palabra secreta: \n ")

while adivinanza != palabra_secreta:
    print("\033[92m¡Sigue adivinando!\033[0m")

    # Preguntar por la primera pista
    respuesta = input("¿Quieres una pista? (Presiona 1 para pista o cualquier otra tecla para seguir intentando): \n ")

    if respuesta == "1":
        print("Pista 1: Es algo que me gusta mucho 😏")

        # Volver a adivinar después de la primera pista
        adivinanza = input("Ingresa la palabra secreta: \n ")
        if adivinanza == palabra_secreta:
            break

        # Preguntar por la segunda pista si sigue sin acertar
        respuesta2 = input("¿Quieres una segunda pista? (Presiona 2 para pista o sigue intentando): \n ")

        if respuesta2 == "2":
            print("Pista 2: Es blanquito, grande y redondito 😍")
        else:
            print("¡Sigue intentando, tú puedes! ❤️")
    else:
        print("¡Intenta de nuevo, amor! ✨")

    # Volver a pedir la adivinanza en cada ciclo
    adivinanza = input("Ingresa la palabra secreta: \n ")

print("\033[95m¡Bien mi amor, adivinaste! Ahora tienes que pasármelo 🙊💕\033[0m")
input("\nPresiona Enter para cerrar el programa... 💋")
