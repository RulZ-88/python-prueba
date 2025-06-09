

print("bienvenido al calculo de envios internacionales")
usuario="admin"
clave="1234"
numero_intentos=0
acceso_usuario=""
acceso_clave=""
cantidad_electronica=0
cantidad_arte=0
cantidad_alimentos=0
cantidad_otros=0
impuestos_total=0
volumen_total=0
costo_base=0
costo_unitario=0




while numero_intentos < 3:
    
    acceso_usuario= input("ingrese su nombre de usuario : \n")
    acceso_clave= input("ingrese su contraseña : \n")
    
    if usuario == acceso_usuario and clave == acceso_clave:
    
      print("Bienvenido")
      break
    else:
       print("usuario o clave incorrectos")
       numero_intentos+=1
if numero_intentos == 3 : print("acceso denegado")
else:
   while True:
     print( """"
      1. Ingresar datos del envío
      2. Calcular el costo del envío internacional
      3. Salir
     """)
     
     opcion =int(input("ingrese el numero de la opcion : \n"))
     
     if opcion == 1: # Opción 1: Ingresar datos del envío

       Nombre_receptor=input("ingrese el nombre: \n")
       rut_receptor=input("ingrese el rut del receptor : \n")
       Dirección_destino=input("ingrese la direccion de destino: \n")
       Correo_electrónico=input("ingrese el correo electronico : \n")
       rut_remitente=input("ingrese el rut del remitente : \n")
       Teléfono_remitente=input("ingrese el telefono del remitente : \n")
     elif opcion == 2:
        cantidad_articulos=int(input("ingrese la cantidad total de articulos que va a declarar \n"))
        print(f"La cantidad de articlos declarados son :{cantidad_articulos} \n" )
       
                                 
        for i in range(cantidad_articulos):
            tipo_articulo= int(input(f"""ingrese el articulo numero {i +1} a declarar: ?
                                     si el articulo es electronica presione 1
                                     si el articulo es Arte        presione 2 
                                     si el articulo es alimentos   presione 3  
                                     si el articulo es otros       presione 4 
                                     Ingrese su opcion:' '"""))
            
             
        
        if tipo_articulo == 1:
           cantidad_electronica+= 1
        elif tipo_articulo == 2 :
           cantidad_arte+=1
        elif tipo_articulo == 3 :
           cantidad_alimentos+=1
        elif tipo_articulo == 4:
           cantidad_otros +=1
        
     
        largo=float(input("ingrese el largo del paquete (en cm) " ))
        ancho=float(input("ingrese el ancho del paquete (en cm) " ))
        alto=float(input("ingrese el alto del paquete (en cm)  " ))
        volumen_total=largo+ancho+alto
        
        if volumen_total % 10 == 0:
          unidades_10cm = volumen_total // 10
        else:
           unidades_10cm = (volumen_total // 10) + 1

               # Convertir a entero por si acaso
        unidades_10cm = int(unidades_10cm)
        costo_base = unidades_10cm * 5
        costo_unitario = costo_base / cantidad_articulos
       
       
        if cantidad_electronica > 0:
           impuestos_total+= costo_unitario * 0.18
        if cantidad_arte > 0:
              impuestos_total += costo_unitario * 0.10
        if cantidad_alimentos >0:
                 impuestos_total += costo_unitario * 0.05
      
        print(f"""El costo base  por las dimenciones del paquete es :{costo_base}
                  Los impuestos aplicados por los tipos de articulos son :{impuestos_total}         
                   El costo total del envio es : ${costo_base+ impuestos_total}""" )
        
     
      
     
     
     elif opcion == 3:
        print("Hasta pronto!")
        break   



           

           
           
                          
                  

     

