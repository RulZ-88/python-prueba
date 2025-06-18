cadena = input("Introduce una frase: ")
palabra = input("Introduce la palabra que deseas eliminar: ")

indice = cadena.find(palabra)

if indice != -1:
    subcadena = cadena[0:indice] + cadena[indice + len(palabra):]
    print(f"Cadena resultante: {subcadena}")
else:
    print("La palabra no fue encontrada en la frase.")


cadena = input("Introduce una frase: ")
palabra = input("Introduce la palabra que deseas eliminar: ")

subcadena = cadena.replace(palabra, "")
print(f"Cadena resultante: {subcadena}")