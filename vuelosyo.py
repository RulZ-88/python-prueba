import random

# Datos de ejemplo (puedes ampliarlos cuando quieras)
vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 1"],
    "ARCO": ["Arica", "Concepción", "2025-07-11", "14:45", "Puerta 2"],
    "COTO": ["Copiapó", "Tocopilla", "2025-07-12", "10:20", "Puerta 3"]
}

info_vuelos = {
    "SAPA": [75000, 3, ['3A', '3B', '3C']],
    "ARCO": [68000, 2, ['4A', '4B']],
    "COTO": [72000, 1, ['5A', '5B', '5C']]
}

pasajes_comprados = {}

def buscar_vuelos():
    print("si desea SOLO origen,escribalo. si desea solo destino, escribalo. si desea ambos escriba en ambos \n")
    origen = input("Origen (vacío si no aplica): ").strip().lower()
    destino = input("Destino (vacío si no aplica): ").strip().lower()
    precio_input = input("Precio máximo (vacío si no aplica): ").strip()

    if precio_input != "":
        try:
            precio_max = int(precio_input)
        except:
            print("⚠️ Precio inválido. Se ignorará.")
            precio_max = None
    else:
        precio_max = None

    print("\n🔍 Vuelos encontrados:")
    encontrado = False
    for codigo in vuelos_chile:
        vuelo = vuelos_chile[codigo]
        info = info_vuelos[codigo]
        ciudad_origen = vuelo[0]
        ciudad_destino = vuelo[1]
        precio = info[0]

        if origen != "" and ciudad_origen.lower() != origen:
            continue
        if destino != "" and ciudad_destino.lower() != destino:
            continue
        if precio_max is not None and precio > precio_max:
            continue

        print(f"{codigo}: {ciudad_origen} → {ciudad_destino}, ${precio}, Asientos: {info[1]}")
        encontrado = True

    if not encontrado:
        print("❌ No se encontraron vuelos.")

def comprar_pasaje():
    codigo = input("Código del vuelo: ").strip().upper()
    if codigo not in vuelos_chile:
        print("❌ Código no válido.")
        return

    if info_vuelos[codigo][1] <= 0:
        print("❌ No hay asientos.")
        return

    nombre = input("Nombre: ").strip()
    rut = input("RUT: ").strip()

    if codigo not in pasajes_comprados:
        pasajes_comprados[codigo] = {}

    # Verificar si ese RUT ya compró
    for asiento in pasajes_comprados[codigo]:
        if pasajes_comprados[codigo][asiento][1] == rut:
            print("⚠️ Ese RUT ya compró pasaje en este vuelo.")
            return

    asiento = info_vuelos[codigo][2].pop(random.randint(0, len(info_vuelos[codigo][2]) - 1))
    info_vuelos[codigo][1] -= 1
    pasajes_comprados[codigo][asiento] = [nombre, rut]
    print(f"✅ Compra exitosa. Asiento: {asiento}")

def mostrar_stock():
    origen = input("Origen (vacío si no aplica): ").strip().lower()
    destino = input("Destino (vacío si no aplica): ").strip().lower()

    print("\n📦 Stock de vuelos:")
    encontrado = False
    for codigo in vuelos_chile:
        vuelo = vuelos_chile[codigo]
        disponibles = info_vuelos[codigo][1]

        if origen != "" and vuelo[0].lower() != origen:
            continue
        if destino != "" and vuelo[1].lower() != destino:
            continue

        print(f"{codigo}: {vuelo[0]} → {vuelo[1]} - Asientos disponibles: {disponibles}")
        encontrado = True

    if not encontrado:
        print("❌ No se encontraron vuelos.")

def ver_pasajes():
    codigo = input("Código del vuelo: ").strip().upper()
    if codigo not in pasajes_comprados or len(pasajes_comprados[codigo]) == 0:
        print("No hay pasajes comprados en este vuelo.")
        return

    print(f"🎫 Pasajes del vuelo {codigo}:")
    for asiento in pasajes_comprados[codigo]:
        datos = pasajes_comprados[codigo][asiento]
        print(f"Asiento {asiento}: {datos[0]} ({datos[1]})")

# ---------------- MENÚ PRINCIPAL ------------------
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar vuelos")
        print("2. Comprar pasaje")
        print("3. Mostrar stock")
        print("4. Ver pasajes comprados")
        print("5. Salir")
        opcion = input("Elige una opción:  ").strip()

        if opcion == "1":
            while True:
                
            buscar_vuelos()
        elif opcion == "2":
            comprar_pasaje()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            ver_pasajes()
        elif opcion == "5":
            print("👋 Gracias por usar el sistema de vuelos.")
            break
        else:
            print("❌ Opción inválida.")

# Ejecutar el menú
menu()
