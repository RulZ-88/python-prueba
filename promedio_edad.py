
usuario_1 = ""
usuario_2 = ""
usuario_3 = ""
edad_1 = 0
edad_2 = 0
edad_3 = 0
cant_usuario = 0
promedio = 0
while True:
    print('''
1.- Ingresar usuario y edad.
2.- Calcular edad promedio.
3.- Salir
          ''')
    opcion = int(input())
    if opcion == 3:
        break
    if opcion == 1:
        while cant_usuario < 3:
            try:
                if cant_usuario == 0:
                    usuario_1 = input("Ingrese usuario 1: ")
                    edad_1 = int(input("Ingrese edad 1: "))
                    cant_usuario += 1
                    break
                if cant_usuario == 1:
                    usuario_2 = input("Ingrese usuario 2: ")
                    edad_2 = int(input("Ingrese edad 2: "))
                    cant_usuario += 1
                    break
                if cant_usuario == 2:
                    usuario_3 = input("Ingrese usuario 3: ")
                    edad_3 = int(input("Ingrese edad 3: "))
                    cant_usuario += 1
                    break
            except ValueError as error:
                print(error)
        if cant_usuario >= 3:
            print("No puede ingresar más usuarios")
    if opcion == 2:
        try:
            promedio = (edad_1 + edad_2 + edad_3) / cant_usuario
        except ZeroDivisionError as error:
            print(error)
        print("El promedio de las edades es: ",round(promedio,2))
        