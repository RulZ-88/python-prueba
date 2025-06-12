

entradas_disponibles=50
MAX_ENTRADA=50


while True:
  try:
    print("""
      *****📽️ Cine Duoc 📽️ *****
 Bienvenido al sistema de venta de entradas del Cine Duoc
 1. Ver entradas disponibles 👌
 2. Comprar entradas 🤑
 3. Devolver entradas ☹️
 4. Salir 🔚
      """)
 
    opcion_usuario=int(input("Selecciona una opción (1-4):\n")) # aqui le pedimos al usuario seleccionar una opcion del menú.
  
  
    if opcion_usuario == 4: # si el usuario ingresa 4 se sale del programa.
      print("Gracias por usar el sistema de ventas del Cine Duoc ¡Hasta pronto! 🎬")
      break
  
    elif  opcion_usuario == 1 : # si el usuario ingresa 1 se muestra la cantidad de entradas disponibles.
      print(f"Estimado usuario, quedan :{entradas_disponibles} entradas disponibles 👌")
   
 
    
    if  opcion_usuario == 2 : 
       if entradas_disponibles > 0: 
        comprar=int(input("Cuantas entradas desea comprar? \n")) 
        if comprar > entradas_disponibles: # si cantidad de entradas excede la cantidad disponible , no lo deja comprar entradas, volviendo al menú principal.
         print(f" ❌ Estimado usuario no puede comprar esa cantidad de entradas solo quedan {entradas_disponibles}")
        
        else:
           print(f"Estimado usuario ah comprado {comprar} entradas")
           entradas_disponibles-=comprar
       else:
         print(f"no quedan entradas disponibles : {entradas_disponibles}")
    if opcion_usuario == 3 : #si el usuario ingresa 3 puede devolver entradas.
      
       devolver=int(input("Cuantas entradas desea devolver? \n"))
       if devolver + entradas_disponibles > MAX_ENTRADA:
        print(f"estimado usuario el limite de entradas son  50 , no  puede devolver {devolver} , porque supera las  50 como limite. {entradas_disponibles}")
       else: 
        print(f"Se han devuelto {devolver} entradas  ")
        entradas_disponibles+=devolver


       
  except  ValueError as NameError:#si el usuario digita cualquier otra tecla que no sea un numero entero , se le informa al usuario , mostrandole el error.
     print(f"⚠️ Opción no válida ⚠️,ingrese solo numeros enteros porfavor. \n {NameError}")

       



  
 

  

      
      