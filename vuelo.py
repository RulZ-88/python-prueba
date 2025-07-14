import random

# Datos de ejemplo
vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 12"],
    "ARCO": ["Arica", "Concepción", "2025-07-11", "14:45", "Puerta 3"],
    "COTO": ["Copiapó", "Tocopilla", "2025-07-12", "10:20", "Puerta 5"],
}

info_vuelos = {
    "SAPA": [75000, 5, ['3A', '3B', '3C', '3D', '3E']],
    "ARCO": [68000, 4, ['4A', '4B', '4C', '4D']],
    "COTO": [72000, 3, ['5A', '5B', '5C']],
}

compras = {}  # Diccionario para guardar compras

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Buscar vuelos")
    print("2. Comprar pasaje")
    print("3. Ver stock")
    print("4. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        origen = input("Ciudad origen (vacío si no aplica): ").strip()
        destino = input("Ciudad destino (vacío si no aplica): ").strip()
        precio_texto = input("Precio máximo (vacío si no aplica): ").strip()

        if precio_texto != "":
            try:
                precio_max = int(precio_texto)
            except:
                print("⚠️ Precio inválido. Se ignorará el filtro de precio.")
                precio_max = None
        else:
            precio_max = None

        print("\n🔍 Vuelos encontrados:")
        for codigo in vuelos_chile:
            vuelo = vuelos_chile[codigo]
            info = info_vuelos[codigo]

            ciudad_origen = vuelo[0]
            ciudad_destino = vuelo[1]
            precio = info[0]

            if origen != "" and ciudad_origen.lower() != origen.lower():
                continue
            if destino != "" and ciudad_destino.lower() != destino.lower():
                continue
            if precio_max is not None and precio > precio_max:
                continue

            print(f"{codigo} - {ciudad_origen} a {ciudad_destino} - ${precio}")

    elif opcion == "2":
        codigo = input("Código del vuelo: ").strip().upper()

        if codigo not in vuelos_chile:
            print("❌ El código no existe.")
            continue

        nombre = input("Nombre del pasajero: ").strip()
        rut = input("RUT del pasajero: ").strip()

        info = info_vuelos[codigo]
        asientos_disponibles = info[2]

        if len(asientos_disponibles) == 0:
            print("❌ No hay asientos disponibles.")
            continue

        asiento = random.choice(asientos_disponibles)
        asientos_disponibles.remove(asiento)
        info[1] -= 1  # Restar un asiento

        # Guardar compra
        if codigo in compras:
            compras[codigo].append([nombre, rut, asiento])
        else:
            compras[codigo] = [[nombre, rut, asiento]]

        print(f"✅ Compra realizada. Pasajero: {nombre}, Asiento: {asiento}")

    elif opcion == "3":
        origen = input("Filtrar por origen (vacío si no aplica): ").strip()
        destino = input("Filtrar por destino (vacío si no aplica): ").strip()

        print("\n📦 Stock de pasajes:")
        for codigo in vuelos_chile:
            vuelo = vuelos_chile[codigo]
            ciudad_origen = vuelo[0]
            ciudad_destino = vuelo[1]
            asientos = info_vuelos[codigo][1]

            if origen != "" and ciudad_origen.lower() != origen.lower():
                continue
            if destino != "" and ciudad_destino.lower() != destino.lower():
                continue

            print(f"{codigo}: {ciudad_origen} → {ciudad_destino} - Asientos disponibles: {asientos}")

    elif opcion == "4":
        print("👋 Hasta luego.")
        break

    else:
        print("❌ Opción no válida.")
