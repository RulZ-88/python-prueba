# Paso 1: Crear una lista vacía llamada beatles
beatles = []

# Paso 2: Agregar los miembros iniciales de la banda usando append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3: Usar un bucle for y append() para pedirle al usuario que agregue los siguientes miembros
for i in range(2):  # Vamos a pedir dos nombres al usuario
    member = input("Por favor ingresa el nombre de un miembro de la banda: ")
    beatles.append(member)

# Mostrar la lista después de agregar los miembros
print("Lista después de agregar los miembros:", beatles)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best usando del
del beatles[3]
del beatles[3]

# Mostrar la lista después de eliminar a Stu y Pete
print("Lista después de eliminar a Stu Sutcliffe y Pete Best:", beatles)

# Paso 5: Usar el método insert() para agregar a Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")

# Mostrar la lista final
print("Lista final con Ringo Starr al principio:", beatles)
