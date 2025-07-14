
import random

vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 1"],
    "ARCO": ["Arica", "Concepcion", "2025-07-11", "14:45", "Puerta 2"],
    "COTO": ["Copiapo", "Tocopilla", "2025-07-12", "10:20", "Puerta 3"]
}

info_vuelos = {
    "SAPA": [75000, 3, ['3A', '3B', '3C']],
    "ARCO": [68000, 2, ['4A', '4B']],
    "COTO": [72000, 1, ['5A', '5B', '5C']]
}

pasajes_comprados ={}



def sub_menu_busqueda():
     
     while True:
        print("\n***** SUBMENÚ BUSCAR VUELOS *****")
        print("1- buscar vuelo por origen")
        print("2- buscar vuelo por destino")
        print("3- buscar vuelo por origen y destino")
        print("4- buscar vuelo por precio")
        print("5- volver al menú principal")
        opcion = input("Digite su opción: ").strip()

        if opcion == "1":
            origen= input("ingrese el origen  ")
            filtros_busqueda(buscar_origen= origen)


        elif opcion == "2":
            destino = input("ingrese el destino").lower()
            filtros_busqueda(buscar_destino=destino)

        elif opcion == "3":
             origen= input("ingrese el origen  ").lower()
             destino = input("ingrese el destino").lower()
             filtros_busqueda(buscar_origen= origen, buscar_destino=destino)

        elif opcion == "4":
            precio = input("ingrese el precio")

        elif opcion == "5":
            break

        else:
            print("Opcion invalida")

           

def filtros_busqueda(buscar_origen="", buscar_destino="", precio_maximo=None):
    encontrados = False

    for codigo, vuelo in vuelos_chile.items():
        origen, destino, fecha, hora, puerta = vuelo
        precio = info_vuelos[codigo][0]

        if (not buscar_origen or origen.lower() == buscar_origen.lower()) and \
           (not buscar_destino or destino.lower() == buscar_destino.lower()) and \
           (not precio_maximo or precio <= precio_maximo):

            print(f"\nVuelo {codigo}:")
            print(f"{origen} ➝ {destino} | Fecha: {fecha} | Hora: {hora} | {puerta}")
            print(f"Precio: ${precio}")
            encontrados = True

    if not encontrados:
        print("No hay vuelos que coincidan con tu búsqueda.")







def filtros_busqueda(buscar_origen="", buscar_destino="", precio_maximo=None):
    encontrados = False

    for codigo, vuelo in vuelos_chile.items():
        origen, destino, fecha, hora, puerta = vuelo
        precio = info_vuelos[codigo][0]

        # Validaciones individuales
        origen_valido = True
        destino_valido = True
        precio_valido = True

        # Validar origen
        if buscar_origen != "":
            if origen.lower() != buscar_origen.lower():
                origen_valido = False

        # Validar destino
        if buscar_destino != "":
            if destino.lower() != buscar_destino.lower():
                destino_valido = False

        # Validar precio
        if precio_maximo is not None:
            if precio > precio_maximo:
                precio_valido = False

        # Mostrar vuelo si pasa todos los filtros
        if origen_valido and destino_valido and precio_valido:
            encontrados = True
            print(f"\nVuelo {codigo}:")
            print(f"{origen} ➝ {destino} | Fecha: {fecha} | Hora: {hora} | {puerta}")
            print(f"Precio: ${precio}")

    if not encontrados:
        print("No hay vuelos que coincidan con tu búsqueda.")

















































# ---------------- MENÚ PRINCIPAL ------------------

while True:
        print("\n--- MENÚ ---")
        print("1. Buscar vuelos")
        print("2. Comprar pasaje")
        print("3. Mostrar stock")
        print("4. Ver pasajes comprados")
        print("5. Salir")
        opcion = input("Elige una opción:  ").strip()

        if opcion == "1":
           sub_menu_busqueda()
        elif opcion == "2":
            print()
        elif opcion == "3":
            print()
        elif opcion == "4":
            print()
        elif opcion == "5":
            print("👋 Gracias por usar el sistema de vuelos.")
            break
        else:
            print("❌ Opción inválida.")