EMPTY=1



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

# Imprimir resultados
print(f"Torres: {rook_count}")
print(f"Caballos: {knight_count}")
print(f"Peones: {pawn_count}")  
