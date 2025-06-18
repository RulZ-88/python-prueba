nombres = []
apellidos = []

# Pedimos 3 nombres
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

# Pedimos 3 apellidos
for i in range(3):
    apellido = input(f"Ingrese el apellido {i+1}: ")
    apellidos.append(apellido)

# Ordenamos ambas listas
nombres.sort()
apellidos.sort()

# Mostramos las listas ordenadas
print("\nNombres ordenados:")
for nombre in nombres:
    print(nombre)

print("\nApellidos ordenados:")
for apellido in apellidos:
    print(apellido)
