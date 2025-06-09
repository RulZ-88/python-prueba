# Lista de productos disponibles y sus precios
productos = ["Pan", "Leche", "Huevos", "Arroz", "Jugo"]
precios = [1000, 1200, 2000, 1500, 1800]

# Lista para guardar productos seleccionados
carrito = []

while True:
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Menú de Productos ---")
        for i in range(len(productos)):
            print(f"{i+1}. {productos[i]} - ${precios[i]}")

        seleccion = input("Seleccione el número del producto que desea agregar: ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= 5:
                carrito.append(seleccion - 1)  # Guardamos el índice del producto
                print(f"✅ Producto '{productos[seleccion - 1]}' agregado al carrito.")
            else:
                print("❌ Opción inválida.")
        else:
            print("⚠️ Por favor, ingrese un número válido.")

    elif opcion == "2":
        if carrito:
            print("\n--- Productos en la canasta ---")
            for i in carrito:
                print(f"- {productos[i]} - ${precios[i]}")
        else:
            print("🛒 La canasta está vacía.")

    elif opcion == "3":
        total = 0
        for i in carrito:
            total += precios[i]
        print(f"\n💰 Total a pagar: ${total}")

    elif opcion == "4":
        print("👋 Gracias por su compra. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción no válida. Intente nuevamente.")
