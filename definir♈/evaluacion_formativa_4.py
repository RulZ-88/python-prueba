# Diccionario inicial de turistas
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"]
}

# --- Función Opción 1 ---
def turistas_por_pais(pais):
    resultado = []
    for clave in turistas.values():
        nombre = clave[0]
        pais_turista = clave[1]
        if pais_turista.lower() == pais.lower():
            resultado.append(nombre)
    if len(resultado) == 0:
        print("No hay turistas de ese pais.")
    else:
        print(f"turistas para el pais {pais} son :{resultado}")

# --- Función Opción 2 ---
def turistas_por_mes(mes):
    total = len(turistas)
    conteo = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_en_fecha = int(fecha.split("-")[1])  # Extraemos el mes como número
        if mes_en_fecha == mes:
            conteo += 1
    porcentaje = (conteo / total) * 100
    return round(porcentaje, 1)

# --- Función Opción 3 ---
def eliminar_turista():
    nombre_ingresado = input("Ingrese nombre del turista a eliminar: ").lower()
    eliminado = False
    for clave in list(turistas.keys()):
        if turistas[clave][0].lower() == nombre_ingresado:
            del turistas[clave]
            print("Turista eliminado con exito.")
            eliminado = True
            break
    if not eliminado:
        print("Turista no encontrado. No se pudo eliminar.")

# --- Programa Principal ---
def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            pais = input("\nIngrese pais a buscar: ")
            turistas_por_pais(pais)

        elif opcion == "2":
            while True:
                try:
                    mes = int(input("\nIngrese mes a buscar: "))
                    if 1 <= mes <= 12:
                        porcentaje = turistas_por_mes(mes)
                        print(f"El número de turistas equivale al {porcentaje} % del total.")
                        break
                    else:
                        print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                except ValueError:
                    print("Debe ingresar un número válido.")

        elif opcion == "3":
            eliminar_turista()

        elif opcion == "4":
            print("Programa terminado...")
            break

        else:
            print("Debe ingresar una opción válida!!")

# Ejecutar el programa
main()
