# Inicializamos la variable con un número muy pequeño para empezar la comparación
largest_number = -99999999

# Contador para saber si se ingresaron números válidos
counter = 0

# Pedimos el primer número al usuario
number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# Mientras el número no sea -1, seguimos pidiendo e inspeccionando números
while number != -1:
    counter += 1  # Aumentamos el contador de números válidos

    # Si el número actual es mayor que el más grande registrado, lo actualizamos
    if number > largest_number:
        largest_number = number

    # Pedimos otro número para la siguiente iteración
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# Al salir del bucle, mostramos el resultado
if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
