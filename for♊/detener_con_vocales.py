
palabra=input("ingrese la palabra \n")
letra=input("ingrese la letra para detener \n")

for caracter in palabra:
    if caracter.lower() == letra.lower():
        break
    elif caracter.lower() == "a":
        continue
    elif caracter.lower() == "e":
        continue
    elif caracter.lower() == "i":
        continue
    elif caracter.lower() == "o":
        continue
    elif caracter.lower() == "u":
        continue
    
    print(caracter,end="")
    



