# 1. Recorrer una lista simple
nombres = ["Ana", "Luis", "Carla"]
for nombre in nombres:
    print(f"{nombre}")
print()


# 2. Recorrer un diccionario simple (clave y valor)
edades = {"Ana": 25, "Luis": 30, "Carla": 22}

for nombre, edad in edades.items():
    print(nombre, "tiene", edad, "años")
print()



# 3. Recorrer una lista de diccionarios
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]

for usuario in usuarios:
    print(usuario["nombre"], "tiene", usuario["edad"], "años")
print()

# 4. Recorrer un diccionario que contiene listas
cursos = {
    "Python": ["Ana", "Luis"],
    "Java": ["Carla", "Pedro"]
}

for curso, alumnos in cursos.items():
    print("Curso:", curso)
    for alumno in alumnos:
        print(" -", alumno)





usuarios = []

# ---------------------- Validaciones ----------------------
def validar_contraseña(contraseña):
    if (
        len(contraseña) >= 8 and
        " " not in contraseña and
        any(c.isalpha() for c in contraseña) and
        any(c.isdigit() for c in contraseña)and
        any(c.isupper()for c in contraseña)
    ):
        return True
    print("❌ Contraseña inválida. Debe tener al menos 8 caracteres, contener letras y números, y no incluir espacios.")
    return False

def validar_sexo(sexo):
    if sexo.upper() in ["M", "F"]:
        return True
    print("❌ Sexo inválido. Ingrese 'M' o 'F'.")
    return False

def nombre_disponible(nombre):
    return all(usuario["nombre"] != nombre for usuario in usuarios)

# ---------------------- Funciones principales ----------------------
def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario:\n").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            continue
        if nombre_disponible(nombre):
            break
        print("❌ Usuario ya existente. Intente con otro nombre.")

    while True:
        sexo = input("Ingrese sexo (M o F):\n").strip().upper()
        if validar_sexo(sexo):
            break

    while True:
        contraseña = input("Ingrese contraseña:\n").strip()
        if validar_contraseña(contraseña):
            break

    usuarios.append({"nombre": nombre, "sexo": sexo, "contraseña": contraseña})
    print(f"✅ Usuario '{nombre}' ingresado con éxito.")

def buscar_usuario():
    nombre = input("Ingrese nombre de usuario a buscar:\n").strip()
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"👤 Usuario encontrado: Sexo: {usuario['sexo']}, Contraseña: {usuario['contraseña']}")
            return
    print("❌ Usuario no encontrado.")

def eliminar_usuario():
    nombre = input("Ingrese nombre de usuario a eliminar:\n").strip()
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            usuarios.remove(usuario)
            print(f"✅ Usuario '{nombre}' eliminado con éxito.")
            return
    print("❌ No se pudo encontrar al usuario.")

# ---------------------- Menú principal ----------------------
def mostrar_menu():
    print("""
    ***** MENÚ DE USUARIOS *****
    1. Ingresar usuario
    2. Buscar usuario
    3. Eliminar usuario
    4. Salir
    """)

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                ingresar_usuario()
            elif opcion == 2:
                buscar_usuario()
            elif opcion == 3:
                eliminar_usuario()
            elif opcion == 4:
                print("👋 Programa terminado.")
                break
            else:
                print("❌ Opción no válida. Ingrese un número del 1 al 4.")
        except ValueError:
            print("❌ Entrada inválida. Debe ingresar un número.")

# Ejecutar programa
main()
