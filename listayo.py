
lista=["x","b","c","d"]
print(lista)

print(len(lista))

lista[:2]= ["a","e"]
print(lista)


lista.insert(2,"i")
print(lista)
lista.append(69)
print(lista)
del lista[1]
print(lista)
lista.append("d")
print(lista)

print(f"{lista.index('d',0)}")
# Mostrar los índices donde está la letra "d"
indices_d = [i for i, valor in enumerate(lista) if valor == "d"]
print(indices_d)