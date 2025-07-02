def sumar():
    numeros = []  # Lista para almacenar los números a sumar
    

    
    while True:
        entrada = input("Ingrese un número a sumar (o 0 para terminar): ")
        print("🧾 Números ingresados:", numeros)

        
        try:
            numero = int(entrada)
        except ValueError:
            print("⚠️ Entrada inválida. Por favor ingrese un número.")
            

        if numero == 0:
            break
        
        numeros.append(numero)
    
    resultado = sum(numeros)
    print(f"✅ La suma de los números ingresados es: {resultado}")
    return resultado



sumar()