'''
Programa: Sistema de bibliotecas.
Utilizar la lista de usuarios y personas definidas a continuación.
El programa debe mostrar un menú que permita:
1 - Buscar un usuario por su rut.
    1.1 - Si el usuario existe mostrar un menú para:
        1.1.1 - Realizar un préstamo de un libro, sólo si hay disponibles.
        1.1.2 - Realizar la devolución de un libro
            1.1.2.1 - Si el libro no existe, permitir registrar el libro que trajo la persona.
    1.2  - Si el usuario no existe, permitir registrar al usuario.
2 - Registrar un nuevo usuario.
3 - Registrar un nuevo libro.
4 - Salir

Debe hacer una función para:
1 - Buscar usuarios
2 - Registrar un usuario
3 - Registrar un libro

Debe usar try-except para verificar todos los posibles códigos peligrosos.
Debe usar mensajes amigables y coherentes con un programa pensado para el encargado de la 
biblioteca. Bien escritos y redactados, puede ayudarse de Chat GPT para esto.
'''

usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": []},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []},
    {"nombre": "Mario", "apellido": "Melendez","rut":"18078662-7","libros":[]}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]


def buscar_usuario(rut):
 for usuario in usuarios:
  if usuario["rut"] == rut:
   return usuario
 return None

def registrar_usuario():
 
   rut=input("ingrese el rut del usuario   ")
   if buscar_usuario(rut):
    print("El rut ingresado ya se encuentra registrado")
    return
   else:
    nombre = input("ingrese el nombre del usuario   ")
    apellido= input("ingrese el apellido   ")
    usuarios.append({"nombre":nombre,"apellido":apellido,"rut":rut})

def prestamo_libro(usuario_encontrado):
  eleccion=input("ingrese el titulo del libro a prestar:   ")
  for libro in libros:
   if libro["titulo"] == eleccion:
      if libro ["cantidad_disponible"] > 0:
        usuario_encontrado["libros"].append(libro["titulo"])
        libro["cantidad_disponible"] -= 1
        print(f" se ah prestado el libro {libro["titulo"]} al usuario {usuario_encontrado["nombre"], ["apellido"]}")
      else:
       print("el libro no esta disponible ")  
   else:
     print("no se encontro el libro")   
   
    
    
while True:


 print("""
 ****************************
       ¡Bienvenido!
 1 - Buscar usuario por rut
 2 - Registrar un usuario
 3 - Registrar un libro
 4 - Salir
    """)
 eleccion_usuario=int(input("digite la opcion : \n"))
 if eleccion_usuario == 1:
  rut=input("ingrese el rut sin puntos y con guion:   ")
  usuario_encontrado=buscar_usuario(rut)

 
  if usuario_encontrado:
   print(f"Usuario encontrado {usuario_encontrado['nombre']} {usuario_encontrado['apellido']}")
   while True:
    print(""" 
          1-Realizar un préstamo de un libro
          2- Realizar la devolución de un libro 
          3- volver al menú principal """)
          
   
    opcion_submenu=int(input("digite su opcion   "))
    if opcion_submenu == 1:
      prestamo_libro(usuario_encontrado)
     
     
    elif opcion_submenu == 2 :
     print("")
     
    elif  opcion_submenu == 3:
     break
    else:
     print("opcion no valida")

  
  else:
    print("usuario no encontrado , desea registrarlo?") 
     
 elif eleccion_usuario == 2:
  registrar_usuario()
 elif eleccion_usuario == 3:
  print("")
  
 elif eleccion_usuario == 4:
  print("hasta pronto!")
  break
 else:
  print("opcion invalida")

  
 
  
  
  
  

       
       
       
       
       
       