import random 
vuelos_chile = {
"SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 12"],
"ARCO": ["Arica", "Concepción", "2025-07-11", "14:45", "Puerta 3"],
"COTO": ["Copiapó", "melipilla", "2025-07-12", "10:20", "Puerta 5"],
"ANTI": ["Antofagasta", "Iquique", "2025-07-13", "07:15", "Puerta 7"],
"VAOS": ["Valdivia", "Osorno", "2025-07-14", "09:50", "Puerta 4"],
"SELA": ["Serena", "La Serena", "2025-07-15", "13:00", "Puerta 2"],
"RIAN": ["Rancagua", "Antofagasta", "2025-07-16", "17:25", "Puerta 6"],
"TEAR": ["Temuco", "Arica", "2025-07-17", "12:10", "Puerta 8"],
"CHIQ": ["Chillán", "Quellón", "2025-07-18", "11:30", "Puerta 1"],
"PACO": ["santiago", "Coyhaique", "2025-07-19", "15:40", "Puerta 10"],
"RAME": ["rancagua", "melipilla", "2025-07-19", "15:40", "Puerta 10"],
}
info_vuelos = {
    "SAPA": [75000, 45, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D']],
    "ARCO": [68000, 30, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F']],
    "COTO": [72000, 20, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E']],
    "ANTI": [83000, 50, ['2A', '2B', '2C', '2J', '2K', '2L', '3A', '3B', '3C', '3D', '3E', '3F', '4A', '4B', '4C', '4D', '4E', '4F']],
    "VAOS": [56000, 35, ['5A', '5B', '5C', '5D', '5E', '5F', '6A', '6B', '6C', '6D', '6E', '6F', '7A', '7B', '7C', '7D']],
    "SELA": [49000, 25, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D']],
    "RIAN": [91000, 70, ['2A', '2B', '2C', '2J', '2K', '2L', '3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C']],
    "TEAR": [94000, 90, ['1A', '1B', '1C', '1D', '1E', '1F', '2A', '2B', '2C', '2D', '2E', '2F']],
    "CHIQ": [63000, 40, ['4A', '4B', '4C', '4D', '4E', '4F', '5A', '5B', '5C', '5D']],
    "PACO": [58000, 30, ['3A', '3B', '3C', '4A', '4B', '4C', '5A', '5B', '5C', '5D', '5E']],
    "RAME": [60000, 30, ['3A', '3B', '3C', '4A', '4B', '4C', '5A', '5B', '5C', '5D', '5E']],
}

pasajes_comprados = {
    "18078662-7": [
        ["SAPA", "Mario", "3A"],
        ["ARCO", "Mario", "3B"]
    ]
}


def filtros():

    filtrados = []

    for clave in vuelos_chile:

        origen = vuelos_chile[clave][0]
        destino = vuelos_chile[clave][1]
        
        

        if clave in info_vuelos:
            precio = info_vuelos[clave][0]
            filtrados.append((clave,origen,destino,precio))

    return filtrados

def busquedas(por_origen = None, por_destino = None ,precio_max = None):


    
    resultado = filtros()
    encontrados = False
    for clave, origen,destino,precio in resultado:

        if por_origen  and origen.lower() != por_origen.lower():
            continue
            
            
        if por_destino  and destino.lower() != por_destino.lower():
            continue
             
             
        if precio_max  is  not None and precio > precio_max :
            continue

        print (f"origen {origen}  destino {destino}  precio {precio}")
        encontrados = True

            
    if not encontrados:
        print(" no hay vuelos con ese filtro")


def vuelos_disponibles():


    for clave in vuelos_chile:

        

        origen,destino,fecha,horario,puerta = vuelos_chile[clave]

        print(f" {clave} {origen} {destino} {fecha} {horario} {puerta}")
            

def stock_pasajes(dato):

   

    if dato in info_vuelos:
    
        
        stock = info_vuelos[dato][1]

        if stock > 0 :

            print(f"codigo {dato} -  stock :{stock}")

        else :
            print("no hay stock para ese vuelo")


    else:
        print ("codigo de vuelo no encontrado")


   
   


def comprar_pasajes(codigo, cantidad):
    if codigo in info_vuelos:
        stock_pasaje = info_vuelos[codigo][1]
        asientos = info_vuelos[codigo][2]

        if stock_pasaje <= 0:
            print("No hay pasajes disponibles para este vuelo.")
            return

        if stock_pasaje < cantidad:
            print(f"No hay esa cantidad de pasajes disponibles. Solo quedan {stock_pasaje}.")
            return

        for i in range(cantidad):
            nombre = input("Introduzca su nombre: ")
            rut = input("Introduzca su RUT sin puntos y con guion: ")

            if len(asientos) == 0:
                print("No hay más asientos disponibles.")
                break

            asiento_asignado = random.choice(asientos)
            asientos.remove(asiento_asignado)

            # Si el RUT no está, se crea la entrada
            if rut not in pasajes_comprados:
                pasajes_comprados[rut] = []

                pasajes_comprados[rut].append([codigo, nombre, asiento_asignado])

                print(f"Pasaje comprado con éxito. Asiento asignado: {asiento_asignado}")
            else : print("el rut ya tiene pasaje comprado")

        # Actualizar el stock y los asientos del vuelo
        info_vuelos[codigo][1] -= cantidad
        info_vuelos[codigo][2] = asientos

    else:
        print("Código de vuelo no encontrado.")


def devolver_pasaje(rut):
    if rut in pasajes_comprados and pasajes_comprados[rut]:  # Si el rut existe y tiene pasajes
        print(f"Pasajes registrados para el RUT {rut}:")
        for i, pasaje in enumerate(pasajes_comprados[rut], start=1):
            print(f"{i}) Código: {pasaje[0]}, Nombre: {pasaje[1]}, Asiento: {pasaje[2]}")

        try:
            seleccion = int(input("Ingrese el número del pasaje que desea devolver: ")) - 1

            if 0 <= seleccion < len(pasajes_comprados[rut]):
                codigo, nombre, asiento = pasajes_comprados[rut].pop(seleccion)

                # Devolver el asiento y aumentar el stock
                info_vuelos[codigo][1] += 1
                info_vuelos[codigo][2].append(asiento)

                print("✅ Pasaje devuelto con éxito.")
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Entrada no válida. Debe ser un número.")
    else:
        print("❌ No hay pasajes registrados con ese RUT.")



                
def revisar_pasajes(rut):
    if rut in pasajes_comprados and pasajes_comprados[rut]:
        print(f"Pasajes registrados para el RUT {rut}:")
        for i, pasaje in enumerate(pasajes_comprados[rut], start=1):
            print(f"{i}) Código: {pasaje[0]}, Nombre: {pasaje[1]}, Asiento: {pasaje[2]}")
    else:
        print("No se encontraron pasajes para ese RUT.")


            





          
            



            










   
        

    

    





         



    

   




    
while True:
    
    print("""
        *******Bienvenido***** 
        1) buscar vuelos
        2) stock pasaje
        3) comprar pasaje 
        4) Salir
        """)
     
    opcion = input("Digite su opcion  ")

    if opcion ==  "1":
        
        while True:

            print("""
                  
           1) buscar vuelos por origen
           2) buscar vuelos por destino
           3) buscar vuelos origen y destino
           4) buscar por precio
           5) ver vuelos disponibles
           6) volver al menú principal

          

            """)
            opcion_submenu = input("Digite su opcion  ")

            if opcion_submenu == "1":

                busqueda_origen = input("ingrese el origen   ")
                busquedas(por_origen = busqueda_origen)
            
            elif opcion_submenu == "2":

                busqueda_destino = input("ingrese el destino")
                busquedas(por_destino = busqueda_destino)

            elif opcion_submenu == "3":
                busqueda_origen = input("ingrese el origen   ")
                busqueda_destino = input("ingrese el destino")
                busquedas(por_origen = busqueda_origen ,por_destino = busqueda_destino)

            elif opcion_submenu == "4":

                busqueda_precio = int(input("ingrese el precio maximo "))
                busquedas(precio_max  = busqueda_precio)

            elif opcion_submenu == "5":
                
                vuelos_disponibles()

            elif opcion_submenu == "6":
                break

    elif opcion == "2":

        opcion_user2 = input("ingrese el codigo del vuelo  ").upper()
        stock_pasajes (opcion_user2)


    elif opcion == "3":
      while True:
        print("""
              1) comprar pasajes
              2) devolver pasajes
              3) revisar pasajes comprados por rut
              4) salir 
      
        """)
        opcion_submenu2 = input("Digite su opcion  ")

        if opcion_submenu2 == "1":
            while True:
                codigo_user = input ("ingrese el codigo del vuelo a comprar:  ").upper()
                try:
                    comprar_user = int(input ("Cuantos pasajes desea comprar?:  "))
                    comprar_pasajes(codigo_user , comprar_user)
                    break
                except ValueError as error:
                    print("Digite solo numéros")

        elif opcion_submenu2 == "2":
            
            buscar_rut = input ("ingrese el rut  ")

            devolver_pasaje(buscar_rut)

        elif opcion_submenu2 == "3":
             rut_check = input("Ingrese el RUT: ")
             revisar_pasajes(rut_check)

                
            
      
        

        


                 


            





