
numeros = int(input("¿Cuántos datos deseas ingresar? "))
lista = []

# Ingreso de datos
for i in range(numeros):
    dato = input("Ingresa un dato: ")
    lista.append(dato)

print(f"\nLista original: {lista}")

numeros_eliminados = []

# Eliminación de dos datos
for i in range(2):
    eliminar = input("¿Qué dato deseas eliminar? ")
    if eliminar in lista:
        lista.remove(eliminar)
        numeros_eliminados.append(eliminar)
    else:
        print(f"El dato '{eliminar}' no está en la lista.")

print(f"\nLista actual: {lista}")
print(f"Lista de datos eliminados: {numeros_eliminados}")