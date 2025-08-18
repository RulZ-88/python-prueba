def saludar(dia):
    match dia:
        case "lunes":
            print("Ánimo, es lunes.")
        case "viernes":
            print("Ya casi es fin de semana.")
        case "sábado" | "domingo":
            print("¡Es fin de semana!")
        case _:
            print("Es un día normal.")


dia = input("que dia es?")
saludar(dia)   # Imprime: Ya casi es fin de semana.
