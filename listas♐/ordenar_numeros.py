def ordenar_numeros():
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingresa una lista de números separados por espacio: ")
    numeros = list(map(int, numeros.split()))

    # Solicitar al usuario el orden de la clasificación
    orden = input("¿Deseas ordenar de mayor a menor (m) o de menor a mayor (v)? (Escribe 'm' para mayor a menor, 'v' para menor a mayor): ").lower()

    # Ordenar la lista según la elección del usuario
    if orden == 'm':
        numeros.sort(reverse=True)  # Ordenar de mayor a menor
    elif orden == 'v':
        numeros.sort()  # Ordenar de menor a mayor
    else:
        print("Opción no válida, por favor ingresa 'm' para mayor a menor o 'v' para menor a mayor.")
        return  # Termina la función si la opción no es válida

    # Mostrar la lista ordenada
    print("Lista ordenada:", numeros)

# Llamar a la función
ordenar_numeros()
