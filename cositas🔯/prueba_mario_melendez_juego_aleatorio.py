import random


#saludo inicial
print("""
****************************************
* Bienvenido al juego de numeros       *
*            aleatorios                *
****************************************
      
SIGA LAS SIGUIENTES INTRUCCIONES :
SOLO TIENES 3 OPORTUNIDADES SINO GAME OVER 😢
""")


#se pide los limites al usuario
limite_1 = int(input("ingrese limite inferior:🕹️ \n"))

limite_2 = int(input("ingrese limite superior: 🕹️ \n "))

# se valida que el limite inferior sea menor

if limite_1 >= limite_2:

  print("el limite inferior debe ser MENOR! que el superior ingresalo nuevamente.")

else:

  # genera un numero aleatorio
  num_secreto = random.randint(limite_1, limite_2)
  
  #intento1
  intento_uno = int(input("adivina 🎲: \n "))

   

  if intento_uno == num_secreto:

    print("BIENNNNNN ADIVINASTE!!! 🎆🎇")

  else:

    if intento_uno < num_secreto:

      print("el numero es mayor jojojo")

    else:

      print("el numero es menor jojojo")

     

    #intento2

    intento_dos = int(input("adivina 🎲: "))

     

    if intento_dos == num_secreto:

      print("BIENNNNNN ADIVINASTE!!! 🎆🎇")

    else:

      if intento_dos < num_secreto:

        print("el numero  es mayor jojojo ")

      else:

        print("el numero es menor jojojo")

       

      #darle pistas al usuario

      distancia1 = abs(num_secreto - intento_uno)

      distancia2 = abs(num_secreto - intento_dos)
                       
      if distancia1 < distancia2:

        print(f"una pista: el numero esta mas cerca de {intento_uno} que de {intento_dos}.")

      elif distancia2 < distancia1:

        print(f"una pista: el numero  esta mas cerca de {intento_dos} que de {intento_uno}.")

      else:

        print(" una pista: estas igual de cerca en ambos intentos.")

       

      #intento3

      intento3 = int(input("ultima oportunidad! adivina 🎲: \n "))

       

      if intento3 == num_secreto:

        print("BIENNNNNN ADIVINASTE!!! 🎆🎇")

      else:

        print(f"perdiste 😭 el numero era: {num_secreto}.")