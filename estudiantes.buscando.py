import unicodedata

# Lista de estudiantes
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
        "nombre": "Mario",
        "apellido": "Meléndez",
        "correo": "tio_demonio@email.com",
        "telefono": "950526636",
        "asignaturas": []  # Puedes poner una lista vacía si no hay asignaturas
    },
    {
    
    
        "nombre": "Miguél",
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
    }
] 


def quitar_tildes(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(
        c for c in texto_normalizado if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_tildes

def buscar_estudiante(nombre, apellido=None):
    nombre = quitar_tildes(nombre.lower())
    if apellido:
        apellido = quitar_tildes(apellido.lower())

    coincidencias = []
    for i, est in enumerate(estudiantes):
        nombre_est = quitar_tildes(est["nombre"].lower())
        apellido_est = quitar_tildes(est["apellido"].lower())

        if apellido:
            if nombre_est == nombre and apellido_est == apellido:
                coincidencias.append((i, est))
        else:
            if nombre_est == nombre:
                coincidencias.append((i, est))

    if coincidencias:
        for pos, est in coincidencias:
            print(f"Estudiante encontrado en posición {pos}:")
            print(f"  Nombre: {est['nombre']} {est['apellido']}")
            print(f"  Correo: {est['correo']}")
            print("  Asignaturas:")
            for asignatura in est["asignaturas"]:
                promedio = sum(asignatura["notas"]) / len(asignatura["notas"])
                print(f"    - {asignatura['nombre']} ({asignatura['codigo']}), promedio: {promedio:.1f}")
    else:
        print("No se encontraron coincidencias.")

    return coincidencias

# Pedir datos al usuario
nombre_usuario = input("Ingrese el nombre del estudiante: ").strip().lower()
apellido_usuario = input("Ingrese el apellido del estudiante (puede dejar vacío): ").strip().lower()

# Llamar la función según si el apellido fue ingresado o no
if apellido_usuario == "":
    buscar_estudiante(nombre_usuario)
else:
    buscar_estudiante(nombre_usuario, apellido_usuario)
