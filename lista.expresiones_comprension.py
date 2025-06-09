# Sin utilizar expresiones de comprensión
cuadrados = []

for x in range(10):
    if x%2 == 0:
        cuadrado = x**2
        cuadrados.append(cuadrado)

print("Sin expresiones de comprensión:", cuadrados)



# Utilizando expresiones de comprensión

cuadrados = [x**2 for x in range(10) if x%2 == 0]
print("Con expresiones de comprensión:", cuadrados)



# Creando un diccionario con expresiones de comprensión
print("\n\nDiccionario creado con expresiones de comprensión:")

personas = [("Carlos", 30), ("Gerardo", 25), ("Maria", 35)]

diccionarios_personas = {nombre: edad for nombre, edad in personas if edad >= 30}
print("Diccionario personas:", diccionarios_personas)








































