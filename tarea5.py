import json
# Lista de productos disponibles y sus precios
productos = ["Pan", "Leche", "Huevos", "Arroz", "Jugo"]
precios = [1000, 1200, 2000, 1500, 1800]

# Lista para guardar productos seleccionados
carrito = []
try:
    with open("carrito.json", "r") as archivo:
        carrito = json.load(archivo)
except FileNotFoundError:
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
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto} - ${precios[i-1]}")

        
        try:
            seleccion = int(input("Seleccione el número del producto que desea agregar: "))
            if 1 <= seleccion <= len(productos):
                carrito.append(seleccion - 1)
                print(f"✅ Producto '{productos[seleccion - 1]}' agregado al carrito.")
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("⚠️ Entrada inválida. Ingrese un número.")

    elif opcion == "2":
        if carrito:
            print("\n--- Productos en la canasta ---")
            for i in carrito:
                print(f"- {productos[i]} - ${precios[i]}")
        else:
            print("🛒 La canasta está vacía.")

    elif opcion == "3":
        total = sum(precios[i] for i in carrito)
        print(f"\n💰 Total a pagar: ${total}")

    elif opcion == "4":
        with open("carrito.json", "w") as archivo:
         json.dump(carrito, archivo)
        print("👋 Gracias por su compra. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción no válida. Intente nuevamente.")





