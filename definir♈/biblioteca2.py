# Sistema de Bibliotecas

usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": []},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]

# Funciones

def buscar_usuario(rut):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            return usuario
    return None

def registrar_usuario():
    
        nombre = input("Ingrese nombre del usuario: ")
        apellido = input("Ingrese apellido del usuario: ")
        rut = input("Ingrese RUT del usuario: ")
        if buscar_usuario(rut):
            print("⚠️ Ya existe un usuario con ese RUT.")
            return
        usuarios.append({"nombre": nombre, "apellido": apellido, "rut": rut, "libros": []})
        print("✅ Usuario registrado exitosamente.")
   

def registrar_libro():
    try:
        id_libro = max(libro["id"] for libro in libros) + 1
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor: ")
        isbn = input("Ingrese el ISBN: ")
        paginas = int(input("Ingrese la cantidad de páginas: "))
        cantidad = int(input("Ingrese la cantidad de ejemplares disponibles: "))
        libros.append({"id": id_libro, "titulo": titulo, "autor": autor, "ISBN": isbn, "paginas": paginas, "cantidad_disponible": cantidad})
        print("✅ Libro registrado correctamente.")
    except Exception as e:
        print(f"❌ Error al registrar el libro: {e}")

def prestar_libro(usuario):
    try:
        print("📚 Lista de libros disponibles:")
        for libro in libros:
            print(f'{libro["id"]} - {libro["titulo"]} (Disponibles: {libro["cantidad_disponible"]})')
        id_libro = int(input("Ingrese el ID del libro a prestar: "))
        for libro in libros:
            if libro["id"] == id_libro:
                if libro["cantidad_disponible"] > 0:
                    usuario["libros"].append(libro["titulo"])
                    libro["cantidad_disponible"] -= 1
                    print(f"✅ Libro '{libro['titulo']}' prestado exitosamente.")
                else:
                    print("⚠️ No hay ejemplares disponibles de ese libro.")
                return
        print("❌ Libro no encontrado.")
    except Exception as e:
        print(f"❌ Error al realizar el préstamo: {e}")

def devolver_libro(usuario):
    try:
        if not usuario["libros"]:
            print("⚠️ El usuario no tiene libros para devolver.")
            return
        print("📦 Libros actualmente en préstamo:")
        for i, libro in enumerate(usuario["libros"], 1):
            print(f"{i}. {libro}")
        opcion = int(input("Seleccione el número del libro a devolver: "))
        libro_devuelto = usuario["libros"].pop(opcion - 1)
        for libro in libros:
            if libro["titulo"] == libro_devuelto:
                libro["cantidad_disponible"] += 1
                print(f"✅ Libro '{libro_devuelto}' devuelto con éxito.")
                return
        print("⚠️ El libro no estaba en la base. Registrando nuevo libro.")
        registrar_libro()
    except Exception as e:
        print(f"❌ Error al devolver el libro: {e}")

# Programa principal

def menu():
    while True:
        print("\n--- 📚 Sistema de Biblioteca ---")
        print("1. Buscar usuario por RUT")
        print("2. Registrar nuevo usuario")
        print("3. Registrar nuevo libro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rut = input("Ingrese el RUT del usuario: ")
            usuario = buscar_usuario(rut)
            if usuario:
                print(f"👤 Usuario encontrado: {usuario['nombre']} {usuario['apellido']}")
                print("1. Realizar préstamo")
                print("2. Realizar devolución")
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    prestar_libro(usuario)
                elif subopcion == "2":
                    devolver_libro(usuario)
                else:
                    print("❌ Opción no válida.")
            else:
                print("⚠️ Usuario no encontrado. ¿Desea registrarlo?")
                registrar = input("Escriba 's' para registrar: ").lower()
                if registrar == 's':
                    registrar_usuario()

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            registrar_libro()

        elif opcion == "4":
            print("👋 Gracias por usar el sistema de biblioteca. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Por favor, intente nuevamente.")

# Ejecutar el programa
menu()
