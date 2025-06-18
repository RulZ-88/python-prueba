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
        print("La contraseña debe contener al menos 1 caracter especial de la lista: ",["*", "-", "!", "_", ",", "."])
        return False
    else: 
        return True

def artistas_por_pais(pais):
    shows_en_pais = []
    for key in shows:
        if shows[key][1].lower() == pais.lower():
            shows_en_pais.append({ "artista":  shows[key][0], "fecha": shows[key][2]})
    if len(shows_en_pais) == 0:
        print("No hay show en este país")
    else:
        print("Los shows en este país son: ")
        for i in shows_en_pais:
            print(i["artista"], i["fecha"])

def shows_por_mes(mes):
    cant_shows = 0
    for key in shows:
        fecha = shows[key][2].split("-")
        try:
            if int(fecha[1]) == mes:
                cant_shows +=1
        except ValueError as error:
            print("Error:", error)
            return
    print("El porcentaje de shows en ese mes es de: ", round((cant_shows*100)/len(shows),1))

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

login = False
print("#"*41)
print("#Bienvenidos al sistema de shows en vivo#")
print("#"*41)

while True:


    print('''
    1. Iniciar sesión
    2. Registrar nuevo usuario
    3. Salir
    ''')
    try:
        opcion = 0
        opcion = int(input())    
    except ValueError as error:
        print("Ingrese un valor válido")
        print("Error: ", error)
    
    if opcion == 3:
        print("Gracias por usar el sistema de shows en vivo")
        break
    if opcion == 1:
        user = input("Ingrese su nombre de usuario: ")
        passwd = input("Ingrese su contraseña: ")

        if user in usuarios:
            if passwd == usuarios[user]:
                print("Usuario ingresado exitosamente!")
                login = True
                break
            else:
                print("Credenciales incorrectas!")
        else:
            print("Credenciales incorrectas!")
    if opcion == 2:
        user = input("Ingrese el nombre de usuario: ")
        if user in usuarios:
            print("Este usuario no está disponible!")
        else:
            passwd = input("Ingrese la contraseña: ")
            if verificar_passwd(passwd):
                usuarios[user] = passwd
                print("Usuario registrado correctamente!")
            else:
                print("No se pudo registrar el usuario")

while True and login:
    print('''
    *** SISTEMA DE SHOWS EN VIVO ***

    1. Mostrar artistas por país
    2. Porcentaje de shows en un mes
    3. Eliminar artista por nombre
    4. Salir

    ''')
    try:
        opcion = 0
        opcion = int(input())
        if not (opcion >= 1 and opcion <=4):
            print("Opción inválida")
    except ValueError as error:
        print("Valor inválido")
        print("Error: ", error)
    
    if opcion == 4:
        print("Gracias por usar el sistema de shows en vivo")
        break
    if opcion == 1:
        pais = input("Ingrese el nombre de un país: ")
        artistas_por_pais(pais)
    if opcion == 2:
        try:
            mes = int(input("Ingrese el mes a analizar: "))
            if mes >=1 and mes <=12:
                shows_por_mes(mes)
            else:
                print("Tiene que elegir un valor entre 1 y 12 inclusive.")
        except ValueError as error:
            print("Valor inválido")
            print("Error: ", error)          