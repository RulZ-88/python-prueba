import re  # Para usar expresiones regulares

def buscar_rut(rut):
    print(f"Buscando RUT: {rut}")  # Simulación

while True:
    try:
        opcion = int(input("Digite su opción por favor: "))
        if opcion == 1:
            rut = input("Ingrese el RUT sin puntos y con guion (ej: 12345678-9): ")

            # Validar el formato del RUT: 7 u 8 dígitos + guion + 1 dígito o 'k'
            if re.match(r"^\d{7,8}-[\dkK]$", rut):
                buscar_rut(rut)
                break  # Salir del bucle si es válido
            else:
                print("Formato de RUT inválido. Intente nuevamente (ej: 12345678-9).")
    except ValueError:
        print("Ingrese solo números para la opción, por favor. Vuelva a intentarlo.")



def buscar_rut(rut):
    print(f"Buscando RUT: {rut}")  # Simulación

def validar_rut(rut):
    if "-" not in rut:
        return False

    partes = rut.split("-")
    if len(partes) != 2:
        return False

    cuerpo, verificador = partes

    # Validar que el cuerpo tenga solo números (7 u 8 dígitos)
    if not cuerpo.isdigit() or not (7 <= len(cuerpo) <= 8):
        return False

    # Validar que el verificador sea un dígito o 'k'/'K'
    if not (verificador.isdigit() or verificador.lower() == 'k'):
        return False

    return True

while True:
    try:
        opcion = int(input("Digite su opción por favor: "))
        if opcion == 1:
            rut = input("Ingrese el RUT sin puntos y con guion (ej: 12345678-9): ")

            if validar_rut(rut):
                buscar_rut(rut)
                break
            else:
                print("RUT inválido. Intente nuevamente. Ejemplo: 12345678-9")
    except ValueError:
        print("Ingrese solo números para la opción, por favor. Vuelva a intentarlo.")



def validar_rut_v3(rut):
    guion_encontrado = False
    cuerpo = ""
    verificador = ""

    for char in rut:
        if not guion_encontrado:
            if char.isdigit():
                cuerpo += char
            elif char == "-" and len(cuerpo) >= 7:
                guion_encontrado = True
            else:
                return False
        else:
            verificador += char

    # Validar condiciones finales
    if len(cuerpo) < 7 or len(cuerpo) > 8:
        return False
    if len(verificador) != 1:
        return False
    if not (verificador.isdigit() or verificador.lower() == 'k'):
        return False

    return True
