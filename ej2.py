#ingresar datos
print("---BUSCAR NUMERO ALEATORIO---")
num1=int(input(
    "Ingrese limite inferior: "))
num2=int(input(
    "Ingrese el limite superior: "))

from random import randint
if num1<num2:
    num_aleatorio=randint(num1,num2)
    #intento 1
    num_ingresado_1=int(input("Intente adivinar: "))
    if num_ingresado_1==num_aleatorio:
        print("Felicidades, acertaste al primer intento :)")
    else:
        if num_ingresado_1<num_aleatorio:
           print("El numero es mayor")
        elif num_ingresado_1>num_aleatorio:
           print("El numero es menor")
    
       #intento 2
        num_ingresado_2=int(input("Intente de nuevo: "))
        if num_ingresado_2==num_aleatorio:
            print("Felicidades, acertaste al segundo intento :)")
        else:
            if num_ingresado_2<num_aleatorio:
               print(
                   "El numero es mayor\n" \
                   "Te dare una pista:")
               if abs(num_aleatorio-num_ingresado_1)<abs(num_aleatorio-num_ingresado_2):
                   print("El numero que buscas esta mas cerca de ",num_ingresado_1," que de ",num_ingresado_2)
               else:
                   print("El numero que buscas esta mas cerca de ",num_ingresado_2," que de ",num_ingresado_1)
            elif num_ingresado_2>num_aleatorio:
               print(
                   "El numero es menor\n"
                   "Te dare una pista:")
               if abs(num_aleatorio-num_ingresado_1)<abs(num_aleatorio-num_ingresado_2):
                   print("El numero que buscas esta mas cerca de ",num_ingresado_1," que de ",num_ingresado_2)
               else:
                   print("El numero que buscas esta mas cerca de ",num_ingresado_2," que de ",num_ingresado_1)

            #intento 3
            num_ingresado_3=int(input("Intente la ultima vez: "))
            if num_ingresado_3==num_aleatorio:
                print("Felicidades, acertaste al tercer intento :)")
            else:
                print(
                  "Perdiste :(\n" \
                  "El numero era: ",num_aleatorio)
else:
   print("Datos no validos")