password = input("Ingrese su contraseña: ")

cont_caracteres = 0
cont_letras = 0
cont_numeros = 0
cont_especiales = 0
cont_espacios = 0

for i in password:
    cont_caracteres += 1
    if i.isalpha():
        cont_letras += 1
    if i.isnumeric():
        cont_numeros += 1
    if i.isspace():
        cont_espacios += 1
    if i in "-_*.!?#$%@":
        cont_especiales += 1 

if cont_caracteres < 8 or cont_caracteres > 16:
    print("Contraseña inválida")
elif cont_numeros <= 0:
    print("Contraseña inválida")
elif cont_letras <= 0:
    print("Contraseña inválida falta letra")
elif cont_especiales > 1:
    print("Contraseña inválida falta caracter")
elif cont_espacios > 0:
    print("Contraseña inválida")
elif i in "-_*.!?#$%@":
    print("Contraseña inválida")
else:
    print("Contraseña válida")