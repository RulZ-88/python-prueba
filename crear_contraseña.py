print(""" Cree su contraseña 🔏
   1. El largo de la contraseña debe ser de mínimo 8 caracteres y máximo 16.
   2. Debe tener al menos un número
   3. Debe tener al menos una letra, no importando si es mayúscula o minúscula.
   4. Debe tener como máximo un caracter especial. La lista de caracteres especiales son: -_*.!?#$%
   5. No puede tener espacios en blanco.
   6. No puede terminar con un caracter especial.
""")

caracteres_especiales = "-_*.!?#$%"

while True:
    pass_usuario = input("Digitela, Por favor: \n")

    
    if len(pass_usuario) < 8:
        print("La contraseña debe tener mínimo 8 caracteres ❌")
        continue
    elif len(pass_usuario) > 16:
        print("La contraseña debe tener máximo 16 caracteres ❌")
        continue

  
    tiene_numero = False
    tiene_letra = False
    tiene_espacio = False
    cuenta_especiales = 0

    for caracter in pass_usuario:
        if caracter.isdigit():
            tiene_numero = True
        elif caracter.isalpha():
            tiene_letra = True
        elif caracter in caracteres_especiales:
            cuenta_especiales += 1
        elif caracter.isspace():
            tiene_espacio = True

    
    if not tiene_numero:
        print("La contraseña debe tener al menos un número ❌")
        continue
    if not tiene_letra:
        print("La contraseña debe tener al menos una letra ❌")
        continue
    if tiene_espacio:
        print("La contraseña no puede tener espacios en blanco ❌")
        continue
    if cuenta_especiales > 1:
        print("La contraseña solo puede tener como máximo un carácter especial ❌")
        continue
    if pass_usuario[-1] in caracteres_especiales:
        print("La contraseña no puede terminar con un carácter especial ❌")
        continue


    print("¡Contraseña creada exitosamente! ✅")
    break