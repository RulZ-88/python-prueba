# estudiantes.py
estudiantes = [
    {
        "nombre": "Ana",
        "apellido": "González",
        "correo": "ana.gonzalez@email.com",
        "asignaturas": [
            {
                "codigo": "MAT101",
                "nombre": "Matemáticas",
                "horario": "Lunes 8:00-10:00",
                "notas": [5.5, 6.7, 4.3, 6.1]
            },
            {
                "codigo": "FIS101",
                "nombre": "Física",
                "horario": "Miércoles 10:00-12:00",
                "notas": [3.9, 5.2, 4.8, 6.0]
            }
        ]
    },
    {
        "nombre": "Carlos",
        "apellido": "Pérez",
        "correo": "carlos.perez@email.com",
        "asignaturas": [
            {
                "codigo": "QUI101",
                "nombre": "Química",
                "horario": "Martes 9:00-11:00",
                "notas": [6.4, 5.8, 6.7, 6.5]
            },
            {
                "codigo": "BIO101",
                "nombre": "Biología",
                "horario": "Jueves 13:00-15:00",
                "notas": [4.0, 4.6, 3.7, 5.0]
            }
        ]
    },
    {
        "nombre": "Lucía",
        "apellido": "Ramírez",
        "correo": "lucia.ramirez@email.com",
        "asignaturas": [
            {
                "codigo": "HIS101",
                "nombre": "Historia",
                "horario": "Lunes 11:00-13:00",
                "notas": [5.1, 5.3, 4.9, 5.7]
            },
            {
                "codigo": "LIT101",
                "nombre": "Literatura",
                "horario": "Viernes 9:00-11:00",
                "notas": [6.2, 6.0, 5.9, 6.4]
            }
        ]
    },
    {
        "nombre": "Diego",
        "apellido": "Morales",
        "correo": "diego.morales@email.com",
        "asignaturas": [
            {
                "codigo": "MAT101",
                "nombre": "Matemáticas",
                "horario": "Lunes 8:00-10:00",
                "notas": [3.5, 4.7, 5.1, 5.8]
            },
            {
                "codigo": "FIS101",
                "nombre": "Física",
                "horario": "Miércoles 10:00-12:00",
                "notas": [6.3, 6.5, 6.2, 6.1]
            }
        ]
    },
    {
        "nombre": "Sofía",
        "apellido": "López",
        "correo": "sofia.lopez@email.com",
        "asignaturas": [
            {
                "codigo": "QUI101",
                "nombre": "Química",
                "horario": "Martes 9:00-11:00",
                "notas": [5.6, 4.8, 5.0, 6.3]
            },
            {
                "codigo": "BIO101",
                "nombre": "Biología",
                "horario": "Jueves 13:00-15:00",
                "notas": [6.7, 6.2, 5.5, 6.1]
            }
        ]
    },
    {
        "nombre": "Miguel",
        "apellido": "Vargas",
        "correo": "miguel.vargas@email.com",
        "asignaturas": [
            {
                "codigo": "HIS101",
                "nombre": "Historia",
                "horario": "Lunes 11:00-13:00",
                "notas": [4.4, 5.0, 5.2, 4.8]
            },
            {
                "codigo": "LIT101",
                "nombre": "Literatura",
                "horario": "Viernes 9:00-11:00",
                "notas": [6.1, 6.3, 6.5, 6.4]
            }
        ]
    },
    {
        "nombre": "Isabel",
        "apellido": "Fernández",
        "correo": "isabel.fernandez@email.com",
        "asignaturas": [
            {
                "codigo": "MAT101",
                "nombre": "Matemáticas",
                "horario": "Lunes 8:00-10:00",
                "notas": [5.7, 6.4, 5.8, 6.0]
            },
            {
                "codigo": "FIS101",
                "nombre": "Física",
                "horario": "Miércoles 10:00-12:00",
                "notas": [4.6, 5.1, 5.9, 5.7]
            }
        ]
    },
    {
        "nombre": "Javier",
        "apellido": "Castillo",
        "correo": "javier.castillo@email.com",
        "asignaturas": [
            {
                "codigo": "QUI101",
                "nombre": "Química",
                "horario": "Martes 9:00-11:00",
                "notas": [6.0, 5.6, 6.3, 6.7]
            },
            {
                "codigo": "BIO101",
                "nombre": "Biología",
                "horario": "Jueves 13:00-15:00",
                "notas": [4.9, 5.0, 5.2, 5.4]
            }
        ]
    },
    {
        "nombre": "Valentina",
        "apellido": "Ortega",
        "correo": "valentina.ortega@email.com",
        "asignaturas": [
            {
                "codigo": "HIS101",
                "nombre": "Historia",
                "horario": "Lunes 11:00-13:00",
                "notas": [5.2, 5.8, 6.0, 6.2]
            },
            {
                "codigo": "LIT101",
                "nombre": "Literatura",
                "horario": "Viernes 9:00-11:00",
                "notas": [6.5, 6.7, 6.3, 6.1]
            }
        ]
    },
    {
        "nombre": "Andrés",
        "apellido": "Mendoza",
        "correo": "andres.mendoza@email.com",
        "asignaturas": [
            {
                "codigo": "MAT101",
                "nombre": "Matemáticas",
                "horario": "Lunes 8:00-10:00",
                "notas": [5.0, 5.4, 5.8, 6.1]
            },
            {
                "codigo": "FIS101",
                "nombre": "Física",
                "horario": "Miércoles 10:00-12:00",
                "notas": [4.7, 5.1, 5.6, 5.9]
            }
        ]
    }
]

print(estudiantes[1]["asignaturas"][0]["notas"][3])






# Función para buscar estudiante
def buscar_estudiante(nombre="Miguel", apellido=None):
    coincidencias = []
    for i, est in enumerate(estudiantes):
        if apellido:
            if est["nombre"] == nombre and est["apellido"] == apellido:
                coincidencias.append((i, est))
        else:
            if est["nombre"] == nombre:
                coincidencias.append((i, est))

    # Imprimir resultados de forma legible
    if coincidencias:
        for pos, est in coincidencias:
            print(f"Estudiante encontrado en posición {pos}:")
            print(f"  Nombre: {est['nombre']} {est['apellido']}")
            print(f"  Correo: {est['correo']}")
            print("  Asignaturas:")
            for asignatura in est["asignaturas"]:
                promedio = sum(asignatura["notas"]) / len(asignatura["notas"])
                print(f"    - {asignatura['nombre']} ({asignatura['codigo']}), promedio: {promedio:.2f}")
    else:
        print("No se encontraron coincidencias.")

    return coincidencias

# Llamada a la función
buscar_estudiante()  # Por defecto buscará a Sofía


# Lista de estudiantes (debes tenerla completa arriba, aquí se asume que ya existe)

# Función para buscar estudiante
def buscar_estudiante(nombre, apellido=None):
    coincidencias = []
    for i, estudiante in enumerate(estudiantes):
        if apellido:
            if estudiante["nombre"] == nombre and estudiante["apellido"] == apellido:
                coincidencias.append((i, estudiante))
        else:
            if estudiante["nombre"] == nombre:
                coincidencias.append((i, estudiante))

    # Imprimir resultados de forma legible
    if coincidencias:
        for pos, estudiante in coincidencias:
            print(f"\nEstudiante encontrado en posición {pos}:")
            print(f"  Nombre: {estudiante['nombre']} {estudiante['apellido']}")
            print(f"  Correo: {estudiante['correo']}")
            print("  Asignaturas:")
            for asignatura in estudiante["asignaturas"]:
                promedio = sum(asignatura["notas"]) / len(asignatura["notas"])
                print(f"    - {asignatura['nombre']} ({asignatura['codigo']}), promedio: {promedio:.2f}")
    else:
        print("\nNo se encontraron coincidencias.")

    return coincidencias

# Solicitar datos al usuario
nombre_usuario = input("Ingrese el nombre del estudiante: ").strip().lower()
apellido_usuario = input("Ingrese el apellido del estudiante (puede dejar vacío): ").strip().lower()

# Llamar a la función con los datos ingresados
if apellido_usuario == "":
    buscar_estudiante(nombre_usuario)
else:
    buscar_estudiante(nombre_usuario, apellido_usuario)

