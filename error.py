# ----------------- DATOS -----------------
vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 1"],
    "ARCO": ["Arica",    "Concepcion",   "2025-07-11", "14:45", "Puerta 2"],
    "COTO": ["Copiapo",  "Tocopilla",    "2025-07-12", "10:20", "Puerta 3"]
}

# [precio, cupos, lista_de_asientos]
info_vuelos = {
    "SAPA": [75000, 3, ['3A', '3B', '3C']],
    "ARCO": [68000, 2, ['4A', '4B']],
    "COTO": [72000, 3, ['5A', '5B', '5C']]
}

pasajes_comprados = []    # guardaremos dicts: {"pasajero": ..., "vuelo": ..., ...}

# ----------------- FUNCIONES -----------------
def mostrar_vuelo(codigo):
    datos = vuelos_chile[codigo]
    info  = info_vuelos[codigo]
    print(codigo, "-", datos[0], "→", datos[1],
          "|", datos[2], datos[3], "|", datos[4],
          "| $", info[0], "| cupos:", info[1])

def filtros_busqueda(buscar_origen="", buscar_destino="", precio_maximo=None):
    global cupos,fecha ,hora , puerta
    encontrados = False
    for cod in vuelos_chile:
        origen, destino, fecha, hora, puerta = vuelos_chile[cod]
        precio, cupos, _ = info_vuelos[cod]

        # Validaciones simples
        ok_origen  = (buscar_origen == ""  or origen.lower()  == buscar_origen.lower())
        ok_destino = (buscar_destino == "" or destino.lower() == buscar_destino.lower())
        ok_precio  = (precio_maximo is None or precio <= precio_maximo)

        if ok_origen and ok_destino and ok_precio:
            mostrar_vuelo(cod)
            encontrados = True
    if not encontrados:
        print("No hay vuelos que coincidan con tu búsqueda.")

def comprar_pasaje():
    print("\nVUELOS DISPONIBLES:")
    for cod in vuelos_chile:
        mostrar_vuelo(cod)

    cod = input("Código del vuelo: ").strip().upper()
    if cod not in vuelos_chile:
        print("Código inválido."); return

    precio, cupos, asientos = info_vuelos[cod]
    if cupos == 0:
        print("No quedan asientos."); return

    print("Asientos libres:", asientos)   # muestra lista tal cual
    asiento = input("Elige asiento exacto: ").strip().upper()
    if asiento not in asientos:
        print("Asiento inválido."); return

    nombre = input("Nombre del pasajero: ").strip()

    # Guardar compra y actualizar stock
    pasajes_comprados.append({"pasajero": nombre, "vuelo": cod,
                              "asiento": asiento, "precio": precio})
    asientos.remove(asiento)
    info_vuelos[cod][1] = info_vuelos[cod][1] - 1

    print("Pasaje comprado:", nombre, "- Vuelo", cod, "- Asiento", asiento, "- $", precio)

def mostrar_stock():
    print("\nSTOCK:")
    for cod in info_vuelos:
        cupos = info_vuelos[cod][1]
        asientos = info_vuelos[cod][2]
        print(cod, "cupos:", cupos, "| asientos libres:", asientos)

def ver_pasajes():
    if pasajes_comprados == []:
        print("\nTodavía no hay pasajes comprados.")
        return
    print("\nPASAJES COMPRADOS:")
    for p in pasajes_comprados:
        print(p["pasajero"], "- Vuelo", p["vuelo"], "- Asiento", p["asiento"], "- $", p["precio"])

# ----------------- SUBMENÚ BÚSQUEDA -----------------
def sub_menu_busqueda():
    while True:
        print("\nSUBMENÚ BUSCAR")
        print("1. Por origen")
        print("2. Por destino")
        print("3. Por origen y destino")
        print("4. Por precio máximo")
        print("5. Volver")
        op = input("Opción: ").strip()

        if op == "1":
            origen = input("Origen: ")
            filtros_busqueda(buscar_origen=origen)
        elif op == "2":
            destino = input("Destino: ")
            filtros_busqueda(buscar_destino=destino)
        elif op == "3":
            origen  = input("Origen: ")
            destino = input("Destino: ")
            filtros_busqueda(buscar_origen=origen, buscar_destino=destino)
        elif op == "4":
            try:
                precio = int(input("Precio máximo: "))
                filtros_busqueda(precio_maximo=precio)
            except ValueError:
                print("Debe ser un número.")
        elif op == "5":
            break
        else:
            print("Opción inválida.")

# ----------------- MENÚ PRINCIPAL -----------------
while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Buscar vuelos")
    print("2. Comprar pasaje")
    print("3. Mostrar stock")
    print("4. Ver pasajes comprados")
    print("5. Salir")
    opcion = input("Elige opción: ").strip()

    if opcion == "1":
        sub_menu_busqueda()
    elif opcion == "2":
        comprar_pasaje()
    elif opcion == "3":
        mostrar_stock()
    elif opcion == "4":
        ver_pasajes()
    elif opcion == "5":
        print("Gracias por usar el sistema de vuelos.")
        break
    else:
        print("Opción inválida.")
