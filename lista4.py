my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
 
for color in my_list:
    print(color)
print(len(my_list))
del my_list[4]
print(my_list)
print(len(my_list))



lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
 
for number in lst:
    add += number
    lst_2.append(add)
 
print(lst_2)