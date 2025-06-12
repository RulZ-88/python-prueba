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

print(estudiantes[1]["asignaturas"][0]["notas"][1])

suma_notas = 0
contador_notas = 0
for estudiante in estudiantes:
    for asignatura in estudiante["asignaturas"]:
        for nota in asignatura["notas"]:
            contador_notas += 1
            suma_notas += nota

print(suma_notas)

print("El promedio de notas total es: ", round(suma_notas/contador_notas,1))



nombres = [estudiante["nombre"] for estudiante in estudiantes ]

nombres.sort(key=len, reverse=True)
print(f"Nombres ordenados de mayor a menor: {nombres}")



for estudiante in estudiantes:
    for asignatura in estudiante["asignaturas"]:
        promedio = sum(asignatura["notas"]) / len(asignatura["notas"])
        asignatura["promedio"] = round(promedio, 1)
print("Asignaturas con promedio:")
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante['nombre']}")
    for asignatura in estudiante["asignaturas"]:
        print(f"  Asignatura: {asignatura['nombre']}, Promedio: {asignatura['promedio']}🗒️")


def buscar_estudiante(nombre, apellido=None):
    coincidencias = []
    for i, est in enumerate(estudiantes):
        if apellido:
            if est["nombre"] == nombre and est["apellido"] == apellido:
                coincidencias.append((i, est))
        else:
            if est["nombre"] == nombre:
                coincidencias.append((i, est))
    
    return coincidencias


