def hello(name): # definiendo una función
    print("Hello,", name) # cuerpo de la función
 
 
name = input("Ingresa tu nombre: ")
 
hello(name) # invocación de la función
 

def message(a="number",b="nombre"):
    print(f"su numero es : {a} su nombre es {b}")

a= int(input("ingrese un numero"))
b= input("ingrese su nombre")
message()
 