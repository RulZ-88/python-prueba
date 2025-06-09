matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")# muestra matrix ordenada

print(f"{matrix[0][0]}") # muestra el numero 1
print(f"{matrix[1][0]}")
print(f"{matrix[2][1]}")
print(f"{matrix[0][2]} \n")

for row in matrix:

    for elementos in row:
        print(elementos, end=" ")
    print()
        