
longitud=(int(input("ingrese cuantos elementos tendra su lista")))
lista=[]
for _ in range(longitud):
    lista.append(int(input("ingrese datos en la lista")))
    
    print (lista)


print(f"la suma de los elementos es {sum(lista)}")
