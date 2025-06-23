my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = input(" ingrese sus palabras : \n")
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
               
print("Ordenada:")
print(my_list)


my_list = ["zorro", "abeja", "gato"]
my_list.sort()
print(my_list)  # ['abeja', 'gato', 'zorro']