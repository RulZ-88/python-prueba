
rows=int(input("¿cuantas filas tendra la matriz?"))
columna=int(input("¿cuantas columnas tendra la matriz?"))
matrix=[]

for row_posicion in range(rows):
    row=[]
    for elemento in range(columna):
        row.append(input(f"introduzca un elemento para la fila {row_posicion}"))
    matrix.append(row)

for row in matrix:
    print(row)