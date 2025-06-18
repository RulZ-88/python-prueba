nombres = []

while True:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

    respuesta = input("¿Desea agregar otro nombre? (Sí / No): ")
    if respuesta.lower() == "no":
        break

# Encontrar el nombre con menor cantidad de caracteres usando len()
nombre_mas_corto = nombres[0]

for nombre in nombres:
    if len(nombre) < len(nombre_mas_corto):
        nombre_mas_corto = nombre

# Eliminar el nombre más corto
nombres.remove(nombre_mas_corto)

# Mostrar resultados
print("\nNombre eliminado:", nombre_mas_corto)
print("Nombres restantes:", nombres)
