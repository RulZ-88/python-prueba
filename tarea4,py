usuarios = []
clave = []

while True:
    print("\n----- MENÚ -----")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario = input("Ingrese su nombre de usuario: ")
        claves = input("Ingrese su contraseña: ")

        if usuario in usuarios:
            indice = usuarios.index(usuario)
            if clave[indice] == claves:
                print("✅ Inicio de sesión exitoso.")
            else:
                print("❌ Contraseña incorrecta.")
        else:
            print("❌ Usuario no encontrado.")

    elif opcion == "2":
        nuevo_usuario = input("Ingrese un nombre de usuario nuevo: ")

        if nuevo_usuario in usuarios:
            print("❌ El usuario ya existe.")
        else:
            nueva_clave = input("Ingrese una contraseña: ")
            usuarios.append(nuevo_usuario)
            clave.append(nueva_clave)
            print("✅ Usuario registrado con éxito.")

    elif opcion == "3":
        usuario_eliminar = input("Ingrese el nombre de usuario a eliminar: ")

        if usuario_eliminar in usuarios:
            indice = usuarios.index(usuario_eliminar)
            contrasenia_confirmacion = input("Ingrese la contraseña para confirmar: ")

            if clave[indice] == contrasenia_confirmacion:
                usuarios.pop(indice)
                clave.pop(indice)
                print("✅ Usuario eliminado con éxito.")
            else:
                print("❌ Contraseña incorrecta. No se eliminó el usuario.")
        else:
            print("❌ Usuario no encontrado.")

    elif opcion == "4":
        print("👋 Saliendo del programa.")
        break

    else:
        print("⚠️ Opción no válida. Intente nuevamente.")
