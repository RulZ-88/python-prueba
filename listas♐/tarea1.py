
"""
1)	Escriba un programa que permita almacenar 3 nombres solicitados
 por pantalla en una lista, luego el sistema deberá mostrar el nombre 
 que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla.
"""
nombres = []

for i in range(3):
    usuario = input("Ingrese un nombre: ")
    nombres.append(usuario)


nombre_mas_largo = nombres[0]  

for nombre in nombres:
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre

print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")



nombres = []

for i in range(3):
    usuario = input("Ingrese un nombre: ")
    nombres.append(usuario)

def contar_caracteres(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

nombre_mas_largo = nombres[0]
longitud_mas_larga = contar_caracteres(nombre_mas_largo)

for nombre in nombres:
    longitud_actual = contar_caracteres(nombre)
    if longitud_actual > longitud_mas_larga:
        nombre_mas_largo = nombre
        longitud_mas_larga = longitud_actual

print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")
print(longitud_actual)