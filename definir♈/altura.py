def calcular_altura(bloques):
    altura = 0
    bloques_necesarios = 1

    while bloques >= bloques_necesarios:
        bloques -= bloques_necesarios
        altura += 1
        bloques_necesarios += 1

    return altura

# Pedimos al usuario cuántos bloques tiene
bloques = int(input("Ingrese la cantidad de bloques disponibles:\n"))
altura = calcular_altura(bloques)

print(f"La altura máxima de la pirámide es: {altura}")
