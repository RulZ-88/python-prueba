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
