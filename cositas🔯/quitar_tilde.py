import unicodedata

# Función para quitar tildes
def quitar_tildes(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


estudiantes = [
    {
        "nombre": "Ana",
        "apellido": "González",
        "correo": "ana.gonzalez@email.com",
        "asignaturas": [
            {"codigo": "MAT101", "nombre": "Matemáticas", "horario": "Lunes 8:00-10:00", "notas": [5.5, 6.7, 4.3, 6.1]},
            {"codigo": "FIS101", "nombre": "Física", "horario": "Miércoles 10:00-12:00", "notas": [3.9, 5.2, 4.8, 6.0]}
        ]
    },
    {
        "nombre": "Mario",
        "apellido": "Meléndez",
        "correo": "tio_demonio@email.com",
        "telefono": "950526636",
        "asignaturas": [
            {
                "codigo": "NEC666",
                "nombre": "Necromorphia",
                "horario": "Domingos",
                "notas": [7.0, 6.9, 6.8]
            }
        ]
    },
    {
        "nombre": "Joaquín",
        "apellido": "Osorio",
        "correo": "joaquin.osorio@gmail.com",
        "asignaturas": [
            {
                "codigo": "MAT102",
                "nombre": "Matemáticas",
                "horario": "Martes 9:00-11:00",
                "notas": [6.5, 7.0, 5.8, 5.1]
            },
            {
                "codigo": "HIS101",
                "nombre": "Historia",
                "horario": "Jueves 14:00-16:00",
                "notas": [6.9, 5.9, 7.0, 6.5]
            }
        ]
    }
]

def buscar_estudiante(nombre, apellido=None):
    nombre = quitar_tildes(nombre.lower())
    apellido = quitar_tildes(apellido.lower()) if apellido else None

    for i, est in enumerate(estudiantes):
        nom = quitar_tildes(est["nombre"].lower())
        ape = quitar_tildes(est["apellido"].lower())

        if nom == nombre and (apellido is None or ape == apellido):
            print(f"Estudiante encontrado en posición {i}:")
            print(f"  Nombre: {est['nombre']} {est['apellido']}")
            print(f"  Correo: {est['correo']}")
            print("  Asignaturas:")
            for a in est["asignaturas"]:
                prom = sum(a["notas"]) / len(a["notas"]) if a["notas"] else 0
                print(f"    - {a['nombre']} ({a['codigo']}), promedio: {prom:.1f}")
            print()
    else:
        print("No se encontraron coincidencias.")


nombre_usuario = input("Ingrese el nombre del estudiante: ").strip()
apellido_usuario = input("Ingrese el apellido del estudiante (puede dejar vacío): ").strip()

buscar_estudiante(nombre_usuario, apellido_usuario if apellido_usuario else None)
