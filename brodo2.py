entradas_disponibles = 50
MAX_ENTRADAS = 50



while True:
    print("""
***** Cine brodo *****
Bienvenido al sistema de venta de entradas del Cine brodo
1. Ver cuántas entradas quedan.
2. Comprar una cantidad de entradas.
3. Devolver entradas.
4. Salir del sistema.""")
    
    opcion = int(input("Ingrese la opción por favor: \n"))

    if opcion == 1:
        print(f"Las entradas disponibles son: {entradas_disponibles}")

    elif opcion == 2:
        comprar_entradas = int(input("¿Cuántas entradas desea comprar?\n"))
        if comprar_entradas > entradas_disponibles:
            print(f"Sr. usuario, solamente tenemos {entradas_disponibles} entradas disponibles.")
        elif comprar_entradas <= 0:
            print("Debe comprar al menos una entrada.")
        else:
            entradas_disponibles -= comprar_entradas
            print(f"Compra exitosa. Ha comprado {comprar_entradas} y quedan {entradas_disponibles} disponibles.")

    elif opcion == 3:
        devolver_entradas = int(input("¿Cuántas entradas desea devolver?\n"))
        if devolver_entradas <= 0:
            print("Debe devolver al menos una entrada.")
        elif entradas_disponibles + devolver_entradas > MAX_ENTRADAS:
            print(f"No se pueden devolver más de {MAX_ENTRADAS - entradas_disponibles} entradas. El tope máximo es {MAX_ENTRADAS}.")
        else:
            entradas_disponibles += devolver_entradas
            print(f"Devolución exitosa. Ha devuelto {devolver_entradas} y hay {entradas_disponibles} disponibles.")

    elif opcion == 4:
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción entre 1 y 4.")

    


