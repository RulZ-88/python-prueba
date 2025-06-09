
#Esto es una lista vacía
mi_lista = []

print(mi_lista)

#Esto es una lista inicializada con enteros 
enteros = [1,2,3,4,5,6,1230]
print(enteros)

#Accedo a la posición de un elemento de la lista
print("el 4to elemento  es:", enteros[3])

#Las lista se pueden recorrer de la siguiente manera
#El valor de i es igual al elemento de la lista
#Desde el elemento 0 al n, donde n es el valor de el último elemento
for i in enteros:
    print(i)



palabra = "paralelepipedo"
print(palabra)
#Accedo a un valor único
print(palabra[5])

#Proceso la palabra:
for i in palabra:
    palabra += i
print(palabra)


enteros = [3,2,20,4,7,1,20,18]
print("lista desordenada: ", enteros)
print("sorted: ", sorted(enteros))
print("sorted -1: ", sorted(enteros,reverse=True))