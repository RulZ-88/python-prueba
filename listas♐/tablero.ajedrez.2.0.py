EMPTY = 1

# Crear el tablero
board = [[EMPTY for i in range(8)] for j in range(8)]
board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"
board[4][2] = "KNIGHT"
board[3][4] = "PAWN"

# Contadores
rook_count = 0
knight_count = 0
pawn_count = 0

# Recorremos todo el tablero
for row in board:
    for piece in row:
        if piece == "ROOK":
            rook_count += 1
        elif piece == "KNIGHT":
            knight_count += 1
        elif piece == "PAWN":
            pawn_count += 1

# Función para imprimir el tablero
def print_board(board):
    print("  +" + "--------+" * 8)
    for i, row in enumerate(board):
        row_str = f"{8 - i} |"
        for cell in row:
            if cell == "ROOK":
                content = "ROOK"
            elif cell == "KNIGHT":
                content = "KNIG"
            elif cell == "PAWN":
                content = "PAWN"
            else:
                content = "    "
            row_str += f" {content:4} |"
        print(row_str)
        print("  +" + "--------+" * 8)
    print("    a      b      c      d      e      f      g      h")

# Imprimir tablero ordenado
print_board(board)

# Imprimir resultados
print(f"Torres: {rook_count}")
print(f"Caballos: {knight_count}")
print(f"Peones: {pawn_count}")  
input("Presiona Enter para continuar...")
