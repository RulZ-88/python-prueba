

productos = {

  '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
  '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
  'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
  'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
  'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
  '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
  '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
  'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}


stock = {

  '8475HD': [387990,10],'2175HD': [327990,4],'JjfFHD': [424990,1],
  'fgdxFHD': [664990,21],'123FHD': [290890,32],
  '342FHD': [444990,7],'GF75HD': [749990,2],'UWU131HD': [349990,1],'FS1230HD': [249990,0],

}

def stock_marca(marca):

  total = 0

  marca = marca.lower()

  for modelo, i in productos.items():

    if i[0].lower() == marca:

      total += stock.get(modelo, [0,0])[1]

  print(f"el stock es: {total}")



def busqueda_precio(precio_minimo, precio_maximo):

  resultado = []

  for modelo, datos_stock in stock.items():

    precio, cantidad_stock = datos_stock

    if precio_minimo <= precio <= precio_maximo and cantidad_stock > 0:

      marca = productos.get(modelo, [None])[0]

      if marca:

        resultado.append(f"{marca}_{modelo}")

  if resultado:

    print(f"los notebooks entre  el rango de precio son: {sorted(resultado)}")

  else:

    print("no hay notebooks en ese rango de precios")



def actualizar_precio(modelo, nuevo_precio):

  if modelo in stock:

    stock[modelo][0] = nuevo_precio

    return True

  else:

    return False



while True:

  print("""

    *** MENU PRINCIPAL ***
    1. Stock marca.💻
    2. Búsqueda por precio.🤑
    3. Actualizar precio.✅
    4. Salir. ✌️

        """)


  opcion = input("ingrese opcion: ")



  if opcion == "1":

    marca = input("ingrese la marca : ")

    stock_marca(marca)



  elif opcion == "2":

    while True:

      try:

        precio_minimo = int(input("ingrese precio minimo: "))

        precio_maximo = int(input("ingrese precio maximo: "))

        break

      except ValueError as error:

        print(f"debe ingresar valores enteros para el precio !! {error}")

    busqueda_precio(precio_minimo, precio_maximo)



  elif opcion == "3":

    while True:

      modelo = input("ingrese el modelo : ")

      try:

        nuevo_precio = int(input("ingrese nuevo precio: "))

      except ValueError:

        print("debe ingresar  valores enteros para el precio")

        continue

      if actualizar_precio(modelo, nuevo_precio):

        print("se actualizo el precio")

      else:

        print("El modelo no existe ")

      otra = input(" desea actualizar otro precio ??  ingrese (si/no)?: ").lower()

      if otra == "no":

        break



  elif opcion == "4":

    print("Programa finalizado ")

    break



  else:

    print("porfavor ingrese una opcion valida")
    



  


