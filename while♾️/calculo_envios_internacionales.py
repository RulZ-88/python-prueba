i = 0

while True:
  print('Bienvenido al Sistema de Cálculo de Envíos Internacionales')
  print('')
  print('=== INICIO DE SESIÓN ===')
  print('')
  usuario = input("Ingrese su usuario: ")
  contraseña = input("Ingrese su contraseña: ")

  if usuario == "admin" and contraseña == "1234":
    print('¡Acceso concedido!')
    while True:
        print('''
            === MENÚ ===
                1. Ingresar datos del envío
                2. Calcular el costo del envío internacional
                3. Salir
             ''')
        try:
            opcion = int(input()) #Linea de error potencial
        except ValueError:
            print("Por favor ingrese una opción válida.")
            opcion = 0

        if opcion == 1 or opcion == 2 or opcion == 3:
            if opcion == 1:
                    print("Por favor ingrese los siguientes datos: ")
                    nombre_receptor = input("Ingrese su Nombre del receptor: ")
                    rut_receptor = input("Ingrese el RUT del receptor: ")
                    direccion_destino = input("Ingrese la Dirección de destino: ")
                    correo_remitente = input("Ingrese el Correo electrónico del remitente: ")
                    rut_remitente = input("Ingrese el RUT del remitente: ")
                    telefono_remitente = input("Ingrese el Teléfono del remitente: ")
            if opcion == 2:
                cantidad_articulos = int(input("Ingrese la Cantidad total de artículos: "))

                cantidad_articulos_electronica = 0
                cantidad_articulos_alimentos = 0
                cantidad_articulos_arte = 0
                
                for contador in range(cantidad_articulos):
                    tipo_articulo = input(f"Tipo del artículo {contador+1} : ")
                    if tipo_articulo == 'electronica':
                        cantidad_articulos_electronica+=1

                    if tipo_articulo == 'alimentos':
                        cantidad_articulos_alimentos+=1

                    if tipo_articulo == 'arte':
                        cantidad_articulos_arte+=1
            
                largo_paquete = float(input("Ingrese largo del paquete (cm): "))
                ancho_paquete = float(input("Ingrese ancho del paquete (cm): "))
                alto_paquete = float(input("Ingrese ancho del paquete (cm): "))

                volumen_total = largo_paquete + ancho_paquete + alto_paquete
                
                #Costo base: $5 por cada 10 cm de volumen (redondeando hacia arriba).
                costo_base = (volumen_total/10) * 5

                costo_electronica = 0
                costo_arte = 0
                costo_alimentos = 0

                impuesto_electronica = 0
                impuesto_arte = 0
                impuesto_alimentos = 0

                if cantidad_articulos_electronica > 0:
                    costo_electronica = costo_base + costo_base*0.18
                    impuesto_electronica = costo_base*0.18
                    print(cantidad_articulos_electronica, 'artículos electrónicos (18% impuesto)')
                
                if cantidad_articulos_arte > 0:
                    costo_arte = costo_base + costo_base*0.1
                    impuesto_arte = costo_base*0.1
                    print(cantidad_articulos_arte, 'artículos arte (10% impuesto)')

                if cantidad_articulos_alimentos > 0:
                    costo_alimentos = costo_base + costo_base*0.05
                    impuesto_alimentos = costo_base*0.05
                    print(cantidad_articulos_alimentos, 'artículos alimento (5% impuesto)')

                costo_total = costo_electronica + costo_arte + costo_alimentos
                impuesto_total = impuesto_electronica + impuesto_arte + impuesto_alimentos
                print("Impuesto total: ", impuesto_total)
                print("Costo total: ",costo_total)

            if opcion == 3:
                print("Gracias por su preferencia, hasta luego")
                break
        
        else:
           print("Ingrese una opción válida")
    break  #Para terminar el otro bucle
  else:
    i += 1
    print("Contraseña o usuario incorrecto, intente nuevamente")
    print("")
    if i == 3:
      print("Acceso denegado.")
      break
  