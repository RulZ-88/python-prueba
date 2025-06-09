
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes ingresar un número válido.")
except ZeroDivisionError:
    print("No puedes dividir por cero.")

while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        break  # Salir del bucle si no hay error
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

print(f"El número ingresado es: {numero}")