palabra = "paralelepipedo"
lista = []

for letra in palabra:
    lista.insert(0, letra)  # inserta cada letra al inicio

# Convertimos la lista en una cadena e imprimimos
print("".join(lista))



palabra = "paralelepipedo"
print(palabra[::-1])  # oditpelepilarap