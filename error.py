import random

# ------------------ DATOS INICIALES ------------------
vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 1"],
    "ARCO": ["Arica", "Concepcion", "2025-07-11", "14:45", "Puerta 2"],
    "COTO": ["Copiapo", "Tocopilla", "2025-07-12", "10:20", "Puerta 3"]
}

info_vuelos = {
    "SAPA": [75000, 3, ['3A', '3B', '3C']],
    "ARCO": [68000, 2, ['4A', '4B']],
    "COTO": [72000, 3, ['5A', '5B', '5C']]
}

pasajes_comprados = []

# ------------------ FUNCIONES ------------------

def filtros_busqueda(buscar_origen="", buscar_destino="", precio_maximo=None):
    encontrados = False

    for codigo, vuelo in vuelos_chile.items():
        origen, destino, fecha, hora, puerta = vuelo
        precio = info_vuelos[codigo][0]

        if (not buscar_origen or origen.lower() == buscar_origen.lower()) and \
           (not buscar_destino or destino.lower() == buscar_destino.lower()) and \
           (not precio_maximo or precio <= precio_maximo):

            print("\nVuelo", codigo)
            print(origen, "→", destino, "| Fecha:", fecha, "| Hora:", hora, "|", puerta)
            print("Precio: $", precio)
            encontrados = True

    if not encontrados:
        print("No hay vuelos que coincidan con tu búsqueda.")

def sub_menu_busqueda():
    while True:
        print("\n*** SUBMENÚ BUSCAR VUELOS ***")
        print("1. Buscar por origen")
        print("2. Buscar por destino")
        print("3. Buscar por origen y destino")
        print("4. Buscar por precio máximo")
        print("5. Volver al menú principal")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            origen = input("Ingresa el origen: ")
            filtros_busqueda(buscar_origen=origen)
        elif opcion == "2":
            destino = input("Ingresa el destino: ")
            filtros_busqueda(buscar_destino=destino)
        elif opcion == "3":
            origen = input("Origen: ")
            destino = input("Destino: ")
            filtros_busqueda(buscar_origen=origen, buscar_destino=destino)
        elif opcion == "4":
            try:
                precio = int(input("Precio máximo: "))
                filtros_busqueda(precio_maximo=precio)
            except:
                print("Debe ingresar un número.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def mostrar_vuelos():
    for cod in vuelos_chile:
        vuelo = vuelos_chile[cod]
        info = info_vuelos[cod]
        print(cod, "-", vuelo[0], "→", vuelo[1], "|", vuelo[2], vuelo[3], "|", vuelo[4], "| Precio: $", info[0], "| Cupos:", info[1])

def comprar_pasaje():
    print("\nVUELOS DISPONIBLES:")
    mostrar_vuelos()

    codigo = input("Ingresa el código del vuelo que deseas: ").strip().upper()
    if codigo not in vuelos_chile:
        print("Código inválido.")
        return

    precio, cupos, asientos = info_vuelos[codigo]
    if cupos == 0 or len(asientos) == 0:
        print("No quedan asientos disponibles.")
        return

    # Asignar asiento aleatorio
    asiento_elegido = random.choice(asientos)

    nombre = input("Nombre del pasajero: ").strip()

    # Guardar pasaje
    pasajes_comprados.append({
        "pasajero": nombre,
        "vuelo": codigo,
        "asiento": asiento_elegido,
        "precio": precio
    })

    # Actualizar asientos y cupos
    asientos.remove(asiento_elegido)
    info_vuelos[codigo][1] -= 1

    print("✅ Pasaje comprado con éxito.")
    print("Pasajero:", nombre)
    print("Vuelo:", codigo)
    print("Asiento asignado:", asiento_elegido)
    print("Precio: $", precio)

def mostrar_stock():
    print("\nSTOCK DE VUELOS:")
    for cod in info_vuelos:
        cupos = info_vuelos[cod][1]
        asientos = info_vuelos[cod][2]
        print(cod, "→ cupos:", cupos, "| asientos disponibles:", asientos)

def ver_pasajes():
    if len(pasajes_comprados) == 0:
        print("\nAún no hay pasajes comprados.")
    else:
        print("\nPASAJES COMPRADOS:")
        for p in pasajes_comprados:
            print(p["pasajero"], "- Vuelo:", p["vuelo"], "- Asiento:", p["asiento"], "- Precio: $", p["precio"])

# ------------------ MENÚ PRINCIPAL ------------------

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Buscar vuelos")
    print("2. Comprar pasaje")
    print("3. Mostrar stock")
    print("4. Ver pasajes comprados")
    print("5. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        sub_menu_busqueda()
    elif opcion == "2":
        comprar_pasaje()
    elif opcion == "3":
        mostrar_stock()
    elif opcion == "4":
        ver_pasajes()
    elif opcion == "5":
        print("👋 Gracias por usar el sistema.")
        break
    else:
        print("Opción inválida.")
