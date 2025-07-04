def verificar_passwd(passwd):
    mayus = False
    especial = False

    for caracter in passwd:
        if caracter.isupper():
            mayus = True
        if caracter in ["*", "-", "!", "_", ",", "."]:
            especial = True

    if not mayus or not especial or len(passwd) < 9:
        print("La contraseña debe contener al menos 9 caracteres")
        print("La contraseña debe contener al menos 1 mayúscula")
        print("La contraseña debe contener al menos 1 caracter especial de la lista: ", ["*", "-", "!", "_", ",", "."])
        return False
    else:
        return True

def artistas_por_pais(pais):
    shows_en_pais = []
    for key in shows:
        if shows[key][1].lower() == pais.lower():
            shows_en_pais.append({"artista": shows[key][0], "fecha": shows[key][2]})
    if len(shows_en_pais) == 0:
        print("No hay shows en este país")
    else:
        print("Los shows en este país son:")
        for i in shows_en_pais:
            print(i["artista"], "-", i["fecha"])

def shows_por_mes(mes):
    cant_shows = 0
    total_shows = len(shows)

    if total_shows == 0:
        print("No hay shows registrados actualmente.")
        return

    for key in shows:
        
            fecha = shows[key][2].split("-")
            if int(fecha[1]) == mes:
                cant_shows += 1
       

    porcentaje = (cant_shows * 100) / total_shows
    print(f"Hay {cant_shows} show(s) en el mes {mes}.")
    print(f"Eso representa el {round(porcentaje, 1)}% del total de shows.")

def eliminar_artista_por_nombre(nombre):
    eliminados = []
    for key in list(shows):  # Creamos una lista para poder eliminar sin error durante la iteración
        if shows[key][0].lower() == nombre.lower():
            eliminados.append(shows.pop(key))
    if eliminados:
        print(f"Se eliminaron {len(eliminados)} show(s) del artista '{nombre.title()}'.")
    else:
        print("No se encontraron shows de ese artista.")

# ==================== DATOS ====================
usuarios = {
    "admin": "Admin*2025"
}

shows = {
    "A001": ["Taylor Swift", "Estados Unidos", "15-09-2025"],
    "A002": ["Bad Bunny", "Puerto Rico", "03-08-2025"],
    "A003": ["Rosalía", "España", "21-10-2025"],
    "A004": ["BLACKPINK", "Corea del Sur", "05-07-2025"],
    "A005": ["Dua Lipa", "Reino Unido", "18-08-2025"],
    "A006": ["BTS", "Corea del Sur", "12-09-2025"],
    "A007": ["Shakira", "Colombia", "25-11-2025"],
    "A008": ["Karol G", "Colombia", "02-12-2025"],
    "A009": ["The Weeknd", "Canadá", "30-06-2025"],
    "A010": ["BTS", "Corea del Sur", "01-03-2025"],
    "A011": ["Taylor Swift", "Estados Unidos", "22-05-2025"],
    "A012": ["Rosalía", "España", "14-12-2025"],
    "A013": ["Dua Lipa", "Reino Unido", "09-11-2025"],
    "A014": ["BLACKPINK", "Corea del Sur", "20-04-2025"],
    "A015": ["Karol G", "Colombia", "10-07-2025"],
    "A016": ["Bad Bunny", "Puerto Rico", "27-09-2025"],
    "A017": ["Shakira", "Colombia", "03-06-2025"],
    "A018": ["The Weeknd", "Canadá", "17-10-2025"],
    "A019": ["Taylor Swift", "Estados Unidos", "06-01-2025"]
}

# ==================== LOGIN ====================
login = False
print("#" * 41)
print("# Bienvenidos al sistema de shows en vivo #")
print("#" * 41)

while True:
    print('''
    1. Iniciar sesión
    2. Registrar nuevo usuario
    3. Salir
    ''')
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError as error:
        print("Ingrese un valor válido.")
        continue

    if opcion == 3:
        print("Gracias por usar el sistema de shows en vivo")
        break

    elif opcion == 1:
        user = input("Ingrese su nombre de usuario: ")
        passwd = input("Ingrese su contraseña: ")

        if user in usuarios and passwd == usuarios[user]:
            print("Usuario ingresado exitosamente!")
            login = True
            break
        else:
            print("Credenciales incorrectas!")

    elif opcion == 2:
        if login:
            nuevo_user = input("Ingrese el nombre de usuario: ")
            if nuevo_user in usuarios:
                print("Este usuario no está disponible!")
            else:
                passwd = input("Ingrese la contraseña: ")
                if verificar_passwd(passwd):
                    usuarios[nuevo_user] = passwd
                    print("Usuario registrado correctamente!")
                else:
                    print("No se pudo registrar el usuario")
        else:
            print("Debe iniciar sesión como administrador para registrar nuevos usuarios.")

# ==================== MENÚ PRINCIPAL ====================
while login:
    print('''
    *** SISTEMA DE SHOWS EN VIVO ***

    1. Mostrar artistas por país
    2. Porcentaje de shows en un mes
    3. Eliminar artista por nombre
    4. Salir
    ''')
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError as error:
        print("Valor inválido. Intente nuevamente.")
        continue

    if opcion == 4:
        print("Gracias por usar el sistema de shows en vivo")
        break
    elif opcion == 1:
        pais = input("Ingrese el nombre de un país: ")
        artistas_por_pais(pais)
    elif opcion == 2:
        try:
            mes = int(input("Ingrese el mes a analizar (1 a 12): "))
            if 1 <= mes <= 12:
                shows_por_mes(mes)
            else:
                print("Debe ser un número entre 1 y 12.")
        except ValueError:
            print("Entrada inválida, debe ser un número.")
    elif opcion == 3:
        artista = input("Ingrese el nombre del artista a eliminar: ")
        eliminar_artista_por_nombre(artista)
    else:
        print("Opción no válida. Intente otra vez.")
