"""
# Crear una lista
elementos = ["A", "B", "C"]
print("Lista original:", elementos)

# Acceder a elementos
print("Primer elemento:", elementos[0])
print("Último elemento:", elementos[-1])

# Agregar elementos
elementos.append("D")
print("Después de append:", elementos)

# Insertar en una posición específica
elementos.insert(1, "X")
print("Después de insert:", elementos)

# Eliminar elementos
elementos.remove("B")
print("Después de remove:", elementos)

# Eliminar con pop
ultimo = elementos.pop()
print("Después de pop:", elementos)
print("Elemento eliminado:", ultimo)

# Cambiar valor
elementos[0] = "Z"
print("Después de cambiar:", elementos)

# Ordenar y revertir
elementos.sort()
print("Ordenada:", elementos)
elementos.reverse()
print("Reversa:", elementos)

# Recorrer una lista
print("Recorriendo lista:")
for item in elementos:
    print(item)

# Verificar si hay un elemento
print("¿Está 'X' en la lista?", "X" in elementos)







# Crear un diccionario
registro = {
    "clave1": "valor1",
    "clave2": 100,
    "clave3": True
}
print("Diccionario original:", registro)

# Acceder a elementos
print("Clave1:", registro["clave1"])
print("Clave2 con get:", registro.get("clave2"))
print("Clave inexistente con get:", registro.get("clave4", "No existe"))

# Modificar o agregar datos
registro["clave2"] = 200
registro["clave4"] = "nuevo valor"
print("Después de modificar:", registro)

# Eliminar elementos
registro.pop("clave3")
print("Después de pop:", registro)

# Recorrer el diccionario
print("Recorriendo diccionario:")
for clave, valor in registro.items():
    print(clave, ":", valor)

# Claves, valores e items
print("Claves:", list(registro.keys()))
print("Valores:", list(registro.values()))
print("Items:", list(registro.items()))


"""
























































usuarios=[]

#validaciones------------------------------------------------------------------------------
def validar_contraseña(contraseña):
    if len(contraseña)<8 or " " in contraseña or not any(c.isalpha()for c in contraseña)or not any(c.isdigit()for c in contraseña):
        print("Contraseña inválida. Intente otra.")
        return False
    return True

def validar_sexo(sexo):
    if sexo!="M" and sexo!="F":
        print("Debe ingresar M o F solamente. Intente de nuevo.")
        return False
    return True

def validar_usuario(nombre):
    for usuario in usuarios:
        if usuario["nombre"]==nombre:
            print("Usuario ya existente. Intente otro.")
            return False
    return True

#defs principales---------------------------------------------------------------------------
def ingresar_usuario():
    while True:
        nombre=input("Ingrese nombre de usuario:\n")
        if validar_usuario(nombre):break 
    while True:
        sexo=input("Ingrese sexo:\n(Solamente M o F)\n")
        if validar_sexo(sexo):break
    while True:
        contraseña=input("Ingrese contraseña:\n")
        if validar_contraseña(contraseña):break
    usuarios.append({"nombre":nombre,"sexo":sexo,"contraseña":contraseña})
    print("Usuario ingresado con éxito.")
    return

def buscar_usuario():
    nombre=input("Ingrese nombre de usuario:\n")
    for usuario in usuarios:
        if usuario["nombre"]==nombre:
            print("El sexo del usuario es",usuario["sexo"],"y la contraseña es",usuario["contraseña"])
            return
    print("El usuario no se encuentra.")           
def eliminar_usuario():

    nombre=input("Ingrese nombre de usuario:\n")
    for usuario in usuarios:
        if usuario["nombre"]==nombre:
            usuarios.remove(usuario)
            print("Usuario eliminado con exito.")
            return
    print("No se pudo eliminar usuario.")

#main----------------------------------------------------------------------------------------
while True:
    try:
        print("""
        *****MENU*****
        1.-Ingresar usuario.
        2.-Buscar usuario.
        3.-Eliminar usuario.
        4.-Salir.

        Ingrese una opción:  
        """)
        opcion=int(input())
        if opcion==1:ingresar_usuario()
        elif opcion==2:buscar_usuario()
        elif opcion==3:eliminar_usuario()
        elif opcion==4:
            print("Programa terminado...")
            break
        else:print("Ingrese una opción válida.")
    except ValueError:print("Ingrese una opción válida.")