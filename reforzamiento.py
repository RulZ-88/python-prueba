productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}
         #modelo    #precio_stock                                       
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,2], 'FS1230HD': [249990,0]}

def stock_marca(marca):

    
    total_stock = 0

    for clave in productos:

        key = productos[clave]
        mark = key [0]

        if marca.lower() == mark.lower():

            if clave in stock:

                total_stock += stock[clave][1]
    else:      
         print("no se encontro la marca")

    print(total_stock)

        

   

def busqueda_precio(precio_min , precio_max):

    lista_encontrados = []
    encontrados = False

    for clave in stock:

        
        precio = stock[clave][0]
        validar_stock = stock[clave][1]

        if precio_min <= precio <= precio_max and validar_stock > 0:
            if clave in productos:
                marca = productos[clave][0]
            lista_encontrados.append(f"la marca es: {marca} - modelo es {clave}")
            encontrados = True

    if not encontrados:
        print( " no hay modelos en ese precio")

    else :
        print(sorted(lista_encontrados))


def actualizar_precio(modelo , p):

    

    if modelo in stock:

        precio = stock[modelo][0]

        print(precio)

        precio = p

        return  True
    return False

    
            

            
while True:
    print("""
            *** MENU PRINCIPAL ***
        1. Stock marca.
        2. Búsqueda por precio.
        3. Actualizar precio.
        4. Salir. 
            """)


    opcion = input("ingrese su opcion  ")

    if opcion == "1" :

        marca = input ("ingrese la marca  ")
        stock_marca(marca)

    if opcion == "2" :

        precio_min = int(input ("ingrese precio minimo "))
        precio_max = int(input ( "ingrese precio maximo"))

        busqueda_precio(precio_min , precio_max)

    if opcion == "3" :

        while True:

            modelo = input (" ingrese el modelo ")
            p= input (" ingrese el precio")

            if actualizar_precio(modelo,p):

                print("precio se actualizo")

            else :
                print("modelo no existe")

            otro = input("desea actualizar otro modelo escriba si / no ?")

            if otro.lower() == "si":
                continue

            else:
                break
                



        






        
    
























    
   



    




               



    














