




def validar_codigo_fortificados(codigo):
  if (len(codigo) >= 6 and
    any(c.isupper() for c in codigo) and
    any(c.isdigit() for c in codigo) and
    not any(c.isspace()for c in codigo)):
    return True
  return False

def validar_codigo_iluminados(codigo):

  if (len(codigo) >= 5 and
    sum(1 for c in codigo if c.isupper()) >= 3 and
    any(c.isdigit() for c in codigo) and
    not(c.isspace()for c in codigo)):
    return True
  return False

        

def comprar_fortificados():
  global stock_fortificados
  if stock_fortificados <= 0:
    print("Entradas agotadas para los Fortificados")
    return
  nombre = input("Ingrese nombre de comprador: ")

  if nombre in comprar_forti:
    print("nombre ya registrado")
    return


  tipo = input("ingrese tipo de entrada (G/V): ").upper()
  if tipo not in ["G", "V"]:
    print("Tipo de entrada no válido.")
    return

  while True:

    codigo = input("ingrese codigo de confirmacion: ")

    if validar_codigo_fortificados(codigo):

      print("codigo validado")

      comprar_forti.append(nombre)

      stock_fortificados -= 1

      print("¡Entrada registrada con éxito para los Fortificados!")
      break

    else:

      print("Codigo no valido intente nuevamente")


def comprar_iluminados():

  global stock_iluminados

  if stock_iluminados <= 0:
    print("entradas agotadas para los Iluminados")
    return
  nombre = input("Ingrese nombre de comprador: ")

  if nombre in comprar_ilu:
    print("nombre ya registrado")
    return

  tipo = input("ingrese tipo de entrada (CV/PAL): ").upper()

  if tipo not in ["CV", "PAL"]:

    print("Tipo de entrada no valida")

    return



  while True:

    codigo = input("ingrese codigo de confirmación: ")
    if validar_codigo_iluminados(codigo):
      print("Codigo validado.")

      comprar_ilu.append(nombre)

      stock_iluminados -= 1

      print("Entrada registrada con exito para los Iluminados")

      break
    else:

      print("codigo no valido intente nuevamente")

def mostrar_stock():

  print(f"entradas disponibles para los Fortificados: {stock_fortificados}")

  print(f"entradas disponibles para los Iluminados: {stock_iluminados}")

comprar_ilu = []
comprar_forti = []


stock_iluminados = 500
stock_fortificados = 500


while True:
    print(""" Bienvenido al sistema de venta de entradas
                 🤘! CONCIERTOS ROCK AND CHILE!🤘
          1.- Comprar entrada a los Fortificados."

          2.- Comprar entrada a los Iluminados"

          3.- Stock de entradas para ambos conciertos"

          4.- Salir """)
    try:
         opcion = int(input("porfavor digite su  opcion: "))
         if opcion == 1:
          comprar_fortificados()
         elif opcion == 2:
          comprar_iluminados()
         elif opcion == 3:
          mostrar_stock()
         elif opcion == 4:
           print("gracias por usar el programa , Hasta luego🤘 ")
           break
         else:
          print("debe ingresar una opción valida segun el menú!!")
    except ValueError as error:
      print(f"ingrese solo numeros enteros porfavor(1-2-3-4) {error}")













































    
    
 
      

    











































































