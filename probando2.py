nombre_1 = ""
edad_1 = 0
nombre_2 = ""
edad_2 = 0
nombre_3 = ""
edad_3 = 0
cantidad_usuarios = 0

while True:
    try:
        print("""
Por favor ingrese la opción:
1.- Ingresar usuario y edad.
2.- Calcular edad promedio.
3.- Salir.
""")
        opcion_usuario = int(input("Digite la opción: "))

        if opcion_usuario == 3:
            break

        elif opcion_usuario == 1:
            if cantidad_usuarios == 0:
                nombre_1 = input("Ingrese el nombre del primer usuario: ")
                while True:
                    try:
                        edad_1 = int(input("Ingrese la edad del primer usuario: "))
                        break
                    except ValueError:
                        print("Edad inválida. Ingrese un número entero.")
                cantidad_usuarios += 1

            elif cantidad_usuarios == 1:
                nombre_2 = input("Ingrese el nombre del segundo usuario: ")
                while True:
                    try:
                        edad_2 = int(input("Ingrese la edad del segundo usuario: "))
                        break
                    except ValueError:
                        print("Edad inválida. Ingrese un número entero.")
                cantidad_usuarios += 1

            elif cantidad_usuarios == 2:
                nombre_3 = input("Ingrese el nombre del tercer usuario: ")
                while True:
                    try:
                        edad_3 = int(input("Ingrese la edad del tercer usuario: "))
                        break
                    except ValueError:
                        print("Edad inválida. Ingrese un número entero.")
                cantidad_usuarios += 1

            else:
                print("No se permiten más ingresos (el máximo es 3).")

        elif opcion_usuario == 2:
            if cantidad_usuarios == 0:
                print("No hay usuarios registrados aún.")
            else:
                suma_edades = edad_1 + edad_2 + edad_3
                promedio = suma_edades / cantidad_usuarios
                print(f"La edad promedio de los {cantidad_usuarios} usuarios es: {promedio:.2f} años")

        else:
            print("Opción no válida. Intente de nuevo.")

    except ValueError:
        print("Error: debe ingresar un número entero para la opción del menú.")
