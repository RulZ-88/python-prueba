my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = "m"

 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
 