impar = 0
par = 0

while True:
    try:
        number = int(input("Introduce un número entero!!!!!! o escribe 0 para detener: "))
        
        if number == 0:
            break
        
        if number % 2 == 1:
            # Incrementar el contador de números impares
            impar += 1
        else:
            # Incrementar el contador de números pares
            par += 1

    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")

# Imprimir resultados
print("Conteo de números impares:", impar)
print("Conteo de números pares:", par)
input("jugador 1 , elije tu tipo de pokémon : \n")