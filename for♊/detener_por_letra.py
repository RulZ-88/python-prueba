usuario=input("ingrese la frase")
letra=input("ingrese la letra a detener")



for caracter in usuario:
    if caracter == letra:
        break
    print (caracter,end="")