def sumar(lista_numeros):
    return sum(lista_numeros)

entrada = input("Ingrese los números a sumar separados por signo '+' (ej: 5,10,15): ")
usuario = [int(num.strip()) for num in entrada.split("+")]
resultado = sumar(usuario)

print("La suma de los números es:", resultado)


def sumar(numeros):
    return sum(numeros)

numeros = []

while True:
    entrada = input("Indique el número a sumar (o escriba 'fin' para terminar): ")

    if entrada.lower() == "fin":
        break

    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("⚠️ Entrada inválida. Por favor ingrese solo números o 'fin'.")

resultado = sumar(numeros)
print("La suma de los números es:", resultado)
