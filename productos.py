productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,2], 'FS1230HD': [249990,0]}





def stock_marca(marca):


    encontrados = False
    total_stock = 0

    for clave in productos:
        datos = productos[clave]  # accede a la lista de características
        if datos[0].lower() == marca:     # datos[0] es la marca
            if clave in stock:
                precio_stock = stock[clave]  # lista: [precio, stock]
                total_stock += precio_stock[1]
                encontrados = True
    
                            
    if not encontrados:
        print(f" no se encontraron  productos de esa marca {marca}")
    else:  print(f"el stock para la marca {marca} es de : {total_stock}")



def buscar_precio(precio_min,precio_max):

    encontrados = False
    lista_encontrados= []
    
    for clave in stock:
        datos = stock[clave]
        total_stock =  datos[1]
        
        
        if datos[0] >= precio_min and datos[0] <= precio_max:
            if total_stock > 0 :
             lista_encontrados.append(f" Marca  : {productos[clave][0]} - Modelo {clave}")
             encontrados = True
             
    
    if not encontrados:
              print( "no hay notebooks en ese rango de precios")
    else:
        for item in sorted(lista_encontrados):
            print(item)
   

def actualizar_precio(modelo, precio):
    
    
    for clave in stock:

       

        if clave.lower()  == modelo.lower():
            print(stock[clave][0])
            stock[clave][0] = precio
            print(stock[clave][0])
            return True

            
    return False        


    



                 
while True:

    print("""
        *** MENU PRINCIPAL ***
    1. Stock marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir. 
        """)

    opcion = input ("ingrese su opcion  ")
    if opcion == "1":
        marca = input ("ingrese la marca  ").lower()
        stock_marca(marca)

    elif opcion == "2":
    
     while True:


        try:
            precio_min = int(input ("ingrese el precio minimo   "))
            precio_max =  int(input (" ingrese el precio maximo  "))
            buscar_precio(precio_min,precio_max)
            break
        except ValueError as error:
            print(f"ingrese solo numeros enteros { error}")

    elif opcion == "3":
        
        modelo = input ("ingrese el modelo").lower()
        precio = int(input("ingrese el precio "))
        actualizar_precio(modelo,precio)

        if not actualizar_precio(modelo, precio):
            print("modelo no encontrado")
        else:
            print("se ah actualizado el precio ")

    elif opcion == "4":
        print("gracias , cerrando...")
    
    else:
        print("elija una opcion del 1-4")

