def verificar_numeros(numeros):
    '''
    Esta función debe verificar que todos los elementos de una lista sean números reales
    de modo que las operaciones matemáticas posteriores puedan llevarse a cabo.
    ¿Tiene argumentos?¿Tiene return?
    '''
    for numero in numeros:
        try:
            float(numero)  # Intentar convertir a float para verificar si es un número real
        except ValueError:
            print(f"'{numero}' no es un número válido.")
            return False
    return True  # Si todos los elementos son números reales, retorna True
       

       

def sumar_numeros(numeros):
    '''
    Esta función debe sumar todos los números que ingresen en una lista y entregar el resultado final.
    Evidentemente tiene un argumento de entrada que debe ser una lista de números reales y un retorno con el resultado
    '''
    resultado = 0
    for numero in numeros:
        resultado += float(numero)  # Convertir cada número a float y sumarlo
    return resultado  # Retornar el resultado de la suma
    
   

def multiplicar_numeros():
    '''
    Esta función debe multiplicar todos los números que ingresen en una lista y entregar el resultado final.
    Evidentemente tiene un argumento de entrada que debe ser una lista de números reales y un retorno con el resultado
    '''
    return

def dividir_numeros():
    '''
    Esta función debe dividir todos los números que ingresen en una lista y entregar el resultado final.
    Evidentemente tiene un argumento de entrada que debe ser una lista de números reales y un retorno con el resultado
    Debe verificar ZeroDivisionError
    '''
    return

def calcular_factorial():
    '''
    Esta función debe calcular el factorial de un número y entregar el resultado.
    '''
    return

print("¡Bienvenido al sistema que lo calcula todo!")

while True:
    print("¿Qué desea calcular hoy?")
    print('''
1) Suma de números
2) Multiplicar números
3) Calcular factorial
4) Dividir números
5) Salir
          ''')
    
    opcion = int(input())
    if opcion == 5:
        print("Gracias por venir, nos vemos pronto!")
        exit
    if opcion == 1:
        numeros = input("Ingrese los números a sumar separados por un espacio: ")
        numeros = numeros.split(" ")
        if verificar_numeros(numeros):
            resultado = sumar_numeros(numeros)
            print("La suma es: ", resultado)
        else:
            print("else?")

    if opcion == 2:
        numeros = input("Ingrese los números a multiplicar separados por un espacio: ")
        numeros = numeros.split(" ")
        if verificar_numeros(numeros):
            resultado = multiplicar_numeros(numeros)
            print("La multiplicación es: ", resultado)
        else:
            print("else?")

    if opcion == 3:
        try:
            numero = 0
            numero = int(input("Ingrese el número al cual calcular el factorial: "))
        except ValueError as error:
            print(error)
        if numero > 0:
            resultado = calcular_factorial(numero)
            print("El resutlado es: ", resultado)
    if opcion == 4:
        numeros = input("Ingrese los números a dividir separados por un espacio: ")
        numeros = numeros.split(" ")
        if verificar_numeros(numeros):
            resultado = dividir_numeros(numeros)
            print("La multiplicación es: ", resultado)
        else:
            print("else?")       