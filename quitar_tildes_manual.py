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
    }
]



def quitar_tildes_manual(texto):
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N'
    }
    for original, reemplazo in reemplazos.items():
        texto = texto.replace(original, reemplazo)
    return texto

resultado = quitar_tildes_manual(input("ingrese una palabra"))
print(resultado)  # Arboles en la montana