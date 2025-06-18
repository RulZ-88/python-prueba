longitud = int(input("Ingrese cuántos elementos tendrá su lista: "))
lista = []

for _ in range(longitud):
    lista.append(int(input("Ingrese un dato para la lista: ")))

print("Lista inicial:", lista)
print(f"La suma de los elementos es {sum(lista)}")

# Ejemplo de operaciones adicionales
# Agregar un elemento
nuevo = int(input("Ingrese un nuevo dato para agregar a la lista: "))
lista.append(nuevo)

# Eliminar un elemento
a_eliminar = int(input("Ingrese el valor que desea eliminar de la lista: "))
if a_eliminar in lista:
    lista.remove(a_eliminar)
    print(f"{a_eliminar} eliminado de la lista.")
else:
    print(f"{a_eliminar} no está en la lista.")

# Mostrar la lista final
print("Lista actualizada:", lista)
print(f"La nueva suma de los elementos es {sum(lista)}")