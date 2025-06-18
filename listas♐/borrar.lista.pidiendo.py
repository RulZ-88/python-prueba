
lista=["a", "b","B", "c", "d","D","F","f"]

eliminar=input("ingrese el valor que desea eliminar de la lista")
for _ in lista:
    if eliminar.lower() in lista:
        lista.remove(eliminar.lower())
        print(f"{eliminar} eliminado de la lista.")
    
    elif eliminar.upper() in lista:
            lista.remove(eliminar.upper())
            print(f"el elemento eliminado de la lista es: {eliminar}")

print("Lista actualizada:", lista)